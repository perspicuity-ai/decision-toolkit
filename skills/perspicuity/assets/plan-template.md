---
format: perspicuity-plan/1
id: <stable identifier>
revision: 1
skill_version: 0.6.0
updated: <date>
plan_status: not_started
# plan_status: not_started, active, waiting, in_review, accepted, stopped.
# Use accepted only when every unit is accepted, stopped or transferred.
# Optional observed times: created_at, updated_at, closed_at.
# Add next_check for a timed obligation.
# An in_review plan needs review_due and a Review due line, as a record does.
---

# <Intention the units serve>

## Current position

Mode: <Plan, Run or Review, with the reason when it matters>

Principal and decider: <objectives owner / chooser>

Plan owner: <actor>

Decision: <inherited / pending / selected, with the basis revision>

Plan scope: <the units, named so a reader can tell when the plan is finished>

Done when: <the criterion that shows the plan is complete: every unit accepted, stopped or transferred>

Ship to: <where the plan's outcome must arrive, and who can verify that it did>

Work: <current finding across the units>

Outcome: <observed result or unknown>

Next: <one actor / one action / trigger>

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

<Destination finding: whether every unit arrived at the destination this plan named, with the observer's evidence. The plan's one verdict is given at the close-out below.>

### Close-out

<Hold in Review mode when every unit is accepted, stopped or transferred, or the plan stops early.>

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
<After every unit is accepted, stopped or transferred, record Closure with its actor, time, reason and evidence.>

## Changes

<Revision, time, change, source, reason and affected units. Link earlier bases by exact revision.>
