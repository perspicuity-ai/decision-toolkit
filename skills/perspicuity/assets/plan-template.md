---
format: perspicuity-plan/1
id: <stable identifier>
revision: 1
skill_version: 0.8.1
updated: <date>
plan_status: not_started
# plan_status: not_started, active, waiting, in_review, accepted, stopped.
# Use accepted only when every Ships as check passes and every unit is accepted, stopped or transferred.
# Optional observed times: created_at, updated_at, closed_at.
# Add next_check for a timed obligation.
# An in_review plan needs review_due and a Review due line, as a record does.
---

# <Intention the units serve>

## Current position

<This section is the principal's five-minute brief. Rewrite it at every stop. Each line at most 280 characters, the section at most 600 words. Gloss every identifier at first use, as in Objectives: `U1 short gloss · U2 short gloss`. Link detail; no tables here.>

Mode: <Plan, Run or Review, with the reason when it matters>

Principal and decider: <objectives owner / chooser>

Plan owner: <actor>

Ask: <the principal's request, in their terms>

Objectives: <O1 phrase · O2 phrase …, or the objectives the work serves>

Options: <the alternatives compared, one phrase each; omit when none were compared>

Decision: <inherited / pending / selected, with the decisive reason and the basis revision>

Reconsider if: <the observation that reopens the plan's choice; omit when it is inherited>

Plan scope: <the units, named so a reader can tell when the plan is finished>

Ships as: <the finished product, as numbered checks, each `auto` (a command; exit 0 passes) or `observer` (a named actor outside the author's environment, and what they inspect)>
1. <auto: `command` — what passing shows>
2. <observer: actor — what they inspect>

Done when: every `Ships as` check passes, every unit is accepted, stopped or transferred, and the close-out is held.

Ship to: <where the plan's outcome must arrive, and who can verify that it did>

Pre-run gate: <each principal decision, credential or human-only step a check or unit needs: answered, with the answer, or moved to a named later plan. Held before Run.>

Work: <current finding across the units>

Outcome: <observed result or unknown>

Needs from you: <each open question for the principal, two to four options, recommendation first; or nothing>

Next: <one actor / one action / trigger>

Exit: <after a loop run: finished, parked or stopped, with the time; for parked, each missing input, its owner and the command that resumes the loop>

<Add Blocked, Waiting on or Dependency when needed, as a record does.>
<Decision, Plan scope and Next are what classify a plan for the tools: without them it reads as unclassified and takes no queue position.>
<Keep each unit's state in its own record; do not restate state here.>

## Frame

<The basis the units share: the problem, the intended outcome, applicable values and authority.>
<Each unit keeps its own basis for its own choice; this is only what they hold in common.>

| ID | Fundamental objective | Source / standing value | Measure, direction and horizon |
| --- | --- | --- | --- |
| O1 | <Valued end> | <Attributed source> | <Comparison measure> |

| Material condition | Type | Basis | Affected unit | Change trigger and response |
| --- | --- | --- | --- | --- |
| <Condition> | <Given, uncertainty or assumption> | <Source or justification> | <Unit> | <Change and response> |

## Units

<One row per unit. Leave the record cell empty while a unit is intended but undecided.>
<Point at records rather than describing their content.>

Grants ratified: <the principal ratifies the grants they own in one act, at the end of Plan: who, when, and each grant's record and revision>

| Unit | Kind | Serves | Record | Waits on | Repository | Owner | Accepted by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <Short name> | <decision, work, evidence, move or gate> | <O#> | <repo:path#anchor, or empty> | <Unit names, or empty> | <alias or local> | <Actor> | <Receiver whose acceptance counts> |

## Later

<Checks and ideas outside this plan's Ships as, each with where it will go: a named later plan, a review commitment, or nowhere. Ideas that arrive during a run go here.>

## Order

<State the order as relations, not as a numbered list, because several units may run together.>

| Unit | Eligible when | What it unblocks |
| --- | --- | --- |
| <Unit> | <Each unit it waits on is accepted, and its grant covers the actor> | <Units, or nothing> |

<Name a condition that is not a simple prerequisite.>

## Repositories

<Declare every repository the plan touches. Omit when all units are local.>

| Alias | Repository | Access |
| --- | --- | --- |
| <alias> | <qualified repository name> | <read or change> |

<Keep every path repository-relative. No absolute path belongs in a plan.>

## Moves

<Include only when content changes repository. Record both sides and what must still resolve.>

| Move | From | To | Must remain reachable | Reference handling | Accepted when |
| --- | --- | --- | --- | --- | --- |
| <What moves> | <alias and path> | <alias and path> | <What readers still need> | <How cross-boundary references are handled> | <Both sides verified> |

## Review

<Add the criteria for the plan as a whole, not for a unit. Unit criteria belong in the unit's record.>

| Criterion | Serves | Evidence source | Owner / window / trigger | Finding | Response |
| --- | --- | --- | --- | --- | --- |
| <Plan-level criterion> | <O#> | <Evidence> | <Assessor and timing> | <Pending, then dated result and limits> | <Action and owner> |

<Destination finding: whether each `Ships as` check passed at the destination this plan named, with the observer's evidence. The plan's one verdict is given at the close-out below.>

### Close-out

<Hold in Review mode as the last step of a finished loop, or when the principal ends the plan early.>

| Question | Answer |
| --- | --- |
| What was supposed to happen? | <From the frame and the units> |
| What happened? | <From the unit records and trailer-tagged commits> |
| Why do they differ? | <Causes, with evidence> |
| What changes next time? | <Each change registered as work with an owner> |

| Delegation measure | Value |
| --- | --- |
| Choices made outside a grant, found at acceptance | <n> |
| Units whose basis and grant are recoverable without the transcript | <n of N> |
| Principal interruptions per delivered unit | <n> |
| Units that served the ratified decision | <n of N> |
| Escalations raised / warranted | <n / n> |
| Grant amendments / units sent back | <n / n> |

Verdict: <close / correct / reconsider>
<Where a unit's destination was another actor, that actor's acceptance is the evidence; name it as a dependency until it exists.>
<After every `Ships as` check passes and every unit is accepted, stopped or transferred, record Closure with its actor, time, reason and evidence. While a review commitment remains, keep the plan `in_review`.>

## Changes

<Revision, time, change, source, reason and affected units. Link earlier bases by exact revision.>
