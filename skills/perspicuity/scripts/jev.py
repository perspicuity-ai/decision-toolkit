#!/usr/bin/env python3
"""Call Jev once, retain the raw exchange, and check its structured answers."""

import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request


ENDPOINT = "https://api.typesafe.ai/v1/systemone"
NUMERIC_TOLERANCE = 1e-6


def load_json(raw):
    def reject_constant(_value):
        raise ValueError("JSON contains a non-finite number")

    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("JSON contains a duplicate key")
            result[key] = value
        return result

    return json.loads(raw, parse_constant=reject_constant, object_pairs_hook=unique_object)


def validate_request(request):
    if not isinstance(request, dict) or not {"state", "model", "questions"} <= request.keys():
        raise ValueError("Request needs state, model and questions")
    if not isinstance(request["state"], (str, dict, list)):
        raise ValueError("State must be text, an object or an array")
    if not isinstance(request["model"], str) or not request["model"]:
        raise ValueError("Model must be a nonempty string")
    questions = request["questions"]
    if not isinstance(questions, dict) or not questions:
        raise ValueError("Questions must be a nonempty object")
    for question in questions.values():
        if not isinstance(question, dict) or not question.get("instructions"):
            raise ValueError("Each question needs instructions")
        kind, criteria = question.get("type"), question.get("criteria")
        if kind == "score":
            if not isinstance(criteria, list) or not 2 <= len(criteria) <= 10:
                raise ValueError("Score requires two to ten descriptions")
        elif kind == "choice":
            if not isinstance(criteria, dict) or not 1 <= len(criteria) <= 255:
                raise ValueError("Choice requires one to 255 options")
        elif kind == "noul":
            if criteria is not None and (not isinstance(criteria, dict) or set(criteria) != {"true", "false"}):
                raise ValueError("Noul criteria must contain true and false")
        else:
            raise ValueError("This caller supports score, choice and noul questions")


def finite_between(value, minimum, maximum):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and minimum <= value <= maximum)


def validate_response(request, response):
    """Keep a valid distribution usable when only its displayed scalar differs."""
    result = {"errors": [], "warnings": [], "questions": {}, "usable_question_ids": [], "ok": False}
    if not isinstance(response, dict) or not isinstance(response.get("answers"), dict):
        result["errors"].append("Response needs an answers object")
        return result
    answers = response["answers"]
    if set(answers) != set(request["questions"]):
        result["errors"].append("Answer IDs differ from the request")
    model = response.get("model")
    if not isinstance(model, str) or not model:
        result["errors"].append("Response does not identify its model")
    elif re.fullmatch(r"jev-\d+\.\d+\.\d+", request["model"]) and model != request["model"]:
        result["errors"].append("Returned model differs from the pinned model")
    for qid, question in request["questions"].items():
        check = {"errors": [], "warnings": [], "usable": False}
        result["questions"][qid] = check
        answer = answers.get(qid)
        kind = question["type"]
        if not isinstance(answer, dict) or answer.get("type") != kind:
            check["errors"].append("Missing answer or incorrect type")
            continue
        if kind == "noul":
            if not finite_between(answer.get("noul"), 0, 1):
                check["errors"].append("Noul must be finite and within zero to one")
        else:
            criteria = question["criteria"]
            expected_keys = {str(i) for i in range(len(criteria))} if kind == "score" else set(criteria)
            probabilities = answer.get("probabilities")
            distribution_ok = isinstance(probabilities, dict) and set(probabilities) == expected_keys
            if not distribution_ok:
                check["errors"].append("Probability keys differ from the requested levels or options")
            elif not all(finite_between(value, 0, 1) for value in probabilities.values()):
                distribution_ok = False
                check["errors"].append("Probabilities must be finite and within zero to one")
            elif abs(sum(probabilities.values()) - 1) > NUMERIC_TOLERANCE:
                distribution_ok = False
                check["errors"].append("Probabilities do not sum to one within the declared tolerance")
            if not finite_between(answer.get("confidence"), 0, 1):
                check["errors"].append("Confidence must be finite and within zero to one")
            if kind == "score":
                if answer.get("legend") != {str(i): value for i, value in enumerate(criteria)}:
                    check["errors"].append("Score legend differs from the supplied descriptions")
                scalar_ok = finite_between(answer.get("score"), 0, len(criteria) - 1)
                check["scalar_usable"] = scalar_ok
                if not scalar_ok:
                    check["warnings"].append("Score scalar is missing or outside its range; use no scalar arithmetic")
                if distribution_ok:
                    mean = sum(int(key) * value for key, value in probabilities.items())
                    check["mean_from_returned_probabilities"] = mean
                    if scalar_ok and abs(answer["score"] - mean) > NUMERIC_TOLERANCE:
                        check["scalar_usable"] = False
                        check["warnings"].append("Score differs from its returned probability mean; retain both, use no scalar arithmetic")
            elif distribution_ok:
                choice = answer.get("choice")
                if choice not in probabilities or probabilities[choice] < max(probabilities.values()) - NUMERIC_TOLERANCE:
                    check["errors"].append("Choice does not select a greatest returned probability")
        check["usable"] = not check["errors"]
    usage = response.get("usage")
    if not isinstance(usage, dict) or any(type(usage.get(key)) is not int or usage[key] < 0 for key in ("input_tokens", "output_tokens")):
        result["warnings"].append("Usage is missing or invalid; do not estimate cost from it")
    if result["errors"]:
        for check in result["questions"].values():
            check["usable"] = False
    result["usable_question_ids"] = [qid for qid, check in result["questions"].items() if check["usable"]]
    result["ok"] = not result["errors"] and all(check["usable"] for check in result["questions"].values())
    return result


def load_key(env_file=None):
    """Read only TYPESAFE_API_KEY. Never execute or interpolate environment text."""
    key = os.environ.get("TYPESAFE_API_KEY", "")
    if env_file is not None:
        matches = []
        for line in Path(env_file).read_text().splitlines():
            match = re.match(r"^\s*(?:export\s+)?TYPESAFE_API_KEY\s*=\s*(.*?)\s*$", line)
            if match:
                value = match[1]
                if value.startswith(("'", '"')):
                    quote = value[0]
                    end = value.find(quote, 1)
                    if end < 0 or (value[end + 1:].strip() and not value[end + 1:].lstrip().startswith("#")):
                        raise ValueError("Invalid quoted TYPESAFE_API_KEY assignment")
                    value = value[1:end]
                else:
                    value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
                matches.append(value)
        if len(matches) != 1:
            raise ValueError("Explicit environment file must contain one TYPESAFE_API_KEY assignment")
        key = matches[0]
    if not key or any(char.isspace() for char in key) or "$" in key or "`" in key:
        raise ValueError("TYPESAFE_API_KEY is absent or is not a literal token")
    return key


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def call(request_raw, key, timeout=30):
    request = load_json(request_raw)
    validate_request(request)
    if key.encode() in request_raw:
        raise ValueError("Request contains the credential; request rejected")
    result = {"started_at": datetime.now(timezone.utc).isoformat(), "endpoint": ENDPOINT,
              "request_raw": request_raw.decode("utf-8"), "numeric_tolerance": NUMERIC_TOLERANCE}
    http_request = urllib.request.Request(ENDPOINT, data=request_raw,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"}, method="POST")
    started = time.perf_counter()
    try:
        with urllib.request.build_opener(NoRedirect()).open(http_request, timeout=timeout) as response:
            raw, status = response.read(), response.status
    except urllib.error.HTTPError as error:
        raw, status = error.read(), error.code
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        result.update(error=type(error).__name__, latency_seconds=time.perf_counter() - started)
        return result
    result.update(http_status=status, latency_seconds=time.perf_counter() - started)
    if key.encode() in raw:
        result["error"] = "Response contains the credential; raw response withheld"
        return result
    try:
        result["response_raw"] = raw.decode("utf-8")
    except UnicodeDecodeError:
        import base64
        result["response_raw_base64"] = base64.b64encode(raw).decode("ascii")
        result["error"] = "Response is not UTF-8"
        return result
    if status != 200:
        result["error"] = "HTTP request failed"
        return result
    try:
        parsed = load_json(raw)
        result["validation"] = validate_response(request, parsed)
        result["model"] = parsed.get("model") if isinstance(parsed, dict) else None
        result["usage"] = parsed.get("usage") if isinstance(parsed, dict) else None
    except (ValueError, TypeError):
        result["error"] = "Response is not valid structured JSON"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("--output", type=Path, help="New JSON file for the exact exchange and checks")
    parser.add_argument("--env-file", type=Path, help="Explicit environment file; no shell evaluation")
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--validate-only", action="store_true", help="Check the request without credentials or a call")
    args = parser.parse_args()
    try:
        raw = args.request.read_bytes()
        validate_request(load_json(raw))
        if args.validate_only:
            print("Request valid; no call made")
            return 0
        if args.output is None or not math.isfinite(args.timeout) or args.timeout <= 0:
            raise ValueError("A new output path and positive finite timeout are required")
        key = load_key(args.env_file)
        if key.encode() in raw:
            raise ValueError("Request contains the credential; request rejected")
        # Reserve the output before spending a request. Preserve a pending attempt if interrupted.
        fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w") as output:
            json.dump({"request_raw": raw.decode("utf-8"), "status": "started"}, output)
        result = call(raw, key, args.timeout)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        ok = result.get("validation", {}).get("ok", False)
        warnings = result.get("validation", {}).get("warnings", [])
        warnings += [item for check in result.get("validation", {}).get("questions", {}).values() for item in check["warnings"]]
        print(json.dumps({"output": str(args.output), "ok": ok, "warnings": len(warnings),
                          "latency_seconds": result.get("latency_seconds"), "usage": result.get("usage")}))
        return 0 if ok else 2
    except (OSError, ValueError, UnicodeDecodeError):
        print("Jev call could not start. Check the request, credential assignment and unused output path.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
