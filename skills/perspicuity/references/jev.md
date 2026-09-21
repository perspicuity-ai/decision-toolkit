# Jev experiments

Ordinary Jev use is paused.
Read this guide only for an explicitly requested Jev experiment.
Keep submitted data and calls within that experiment's authorization.
Use the [decision basis](analysis.md) for ordinary work.
Keep exact measurements and arithmetic in code.
The guiding agent owns objectives, alternatives, scales, evidence selection and the final decision within its authority.

## Frame a Score judgment

Define one consequence per question.
Specify the alternative, objective, conditions and horizon.
Use the same objective-specific scale across alternatives.
Describe two to ten distinct, ordered levels for a [Score](https://docs.typesafe.ai/primitives/score).
Make each level self-contained.
Include the full question in `instructions` because Jev cannot see question IDs.

Provide the relevant facts, source references, assumptions and material gaps in `state`.
Exclude unrelated history.
Check whether the evidence distinguishes the levels before using the result.
If evidence is insufficient, identify the missing fact that could change the choice.
Keep that consequence unknown until further evidence or a defensible conditional estimate supports it.
Do not encode missing evidence as a middle performance level.

For a useful diagnostic, ask an independent [Noul](https://docs.typesafe.ai/primitives/noul) question about a specific evidence requirement.
Prefer literal fact-presence questions when a broader sufficiency question combines several judgments.
Check that result against the evidence itself.
A returned distribution or high confidence does not establish evidence sufficiency.

## Call and retain

Batch independent questions against the same compact state.
Use [the stdlib caller](../scripts/jev.py) for direct HTTP without an SDK.
Supply `TYPESAFE_API_KEY` through the environment or an explicit environment file.
The loader reads the key as literal text without shell execution.

```bash
python <skill-directory>/scripts/jev.py request.json --validate-only
python <skill-directory>/scripts/jev.py request.json --env-file .env --output jev-run.json
```

Use a new output path for each attempt.
The caller preserves exact request and response text, model, usage, latency and checks.
It sends requests only to the [official endpoint](https://docs.typesafe.ai/api).
It refuses redirects and automatic retries.
Pin a model version when reproducing an evaluation.
The verified version on September 19, 2026 is `jev-1.13.0`.

When no usable result returns, state the actual cause.
Distinguish unavailable access, transport failure, invalid output, unsuitable question and insufficient evidence.
Repair the cause when that effort could affect the decision.
Use an attributed agent judgment or another suitable method when a fallback is warranted.
Keep unsupported consequences unknown.

## Read and display

Retain each Score's full distribution, legend, scalar and confidence in the linked run.
Show the decisive consequence and compact distribution in the main table.
For example, `editor autonomy: P[maintainer, shared, independent] = [0%, 20%, 80%]` preserves the scale meaning.
Add a short evidence reference and any material gap.
Use the stored probabilities directly for a later chart.

Treat the distribution as Jev's judgment over the stated descriptions.
Do not present it as a calibrated forecast of real-world outcomes without relevant validation.
[Confidence](https://docs.typesafe.ai/confidence) describes concentration of the returned distribution.
The scalar represents its mean level index.
It does not supply a raw outcome or an established value scale.

The caller rejects invalid distributions and mismatched questions.
It flags a scalar that differs from the returned probability mean.
Retain a valid distribution with that warning.
Avoid scalar arithmetic when the warning applies.
Do not silently normalize probabilities or infer an undocumented rounding guarantee.
Inspect a discrepancy's effect on the decision before choosing a repair.

## Select and evaluate

Use explicit preferences to interpret differences across objectives.
For [weighted scoring](https://docs.typesafe.ai/patterns/composite-scoring), state the scale meanings and weight sources.
Calculate the result in code.
Label an approximate ranking rule as a heuristic.
Check sensitivity when reasonable changes could reverse the choice.
Keep known constraint violations outside selectable alternatives.

For a suitable bounded selection, use [Choice](https://docs.typesafe.ai/primitives/choice) with eligible alternatives and an unresolved option.
Supply the actual criteria, preference basis, consequences and material gaps.
If Choice uses Score outputs, make a second request after those outputs arrive.
Questions within one request cannot consume each other's answers.
Record the authorized final choice and its decisive reason.

For an agent comparison, save the independent agent result before exposure to Jev.
Keep that result outside Jev's input.
For an evidence experiment, freeze packets and external reference answers before calls.
Compare missing, sufficient and distracting evidence on repeated cases.
Judge accuracy against those references, rather than confidence alone.
Measure input tokens, output tokens and elapsed time.
Include preparation and orchestration in any cost comparison.
Report listed-price estimates separately from actual billing.
