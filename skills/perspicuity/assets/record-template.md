---
format: perspicuity-work/1
id: <stable identifier>
revision: 1
skill_version: 0.5.0
updated: <date>
record_status: open
work_status: not_started
# work_status: not_started, active, waiting, submitted, in_review, accepted, stopped.
# Use accepted only when nothing further is owed, then close the record.
# Optional observed times: created_at, updated_at, closed_at. Quote ISO 8601 values.
# Add next_check for a timed obligation. Add review_due with the same date for in_review work.
---

# <Intention>

## Current position

Principal and decider: <objectives owner / chooser>

Work owner: <actor>

Decision: <state / basis revision / pending owner or no-choice reason>

Work scope: <the delivery, named so a reader can tell whether it is finished>

Work: <current finding>

Outcome: <observed result or unknown>

Next: <one actor / one action / trigger>

<Add Blocked, Waiting on or Review due when needed. Put the next_check date in the header for a timed obligation.>
<For blocked work: Blocked names the missing input, Waiting on names its owner, and Dependency names the resolving step.>
<For in_review work: name the check, its evidence source and owner. More work returns it to active.>
<Link supporting detail. Omit irrelevant tables. Use one row or a sentence for simple work.>

| Stage | began_at | registered_at / exact basis revision | finished_at |
| --- | --- | --- | --- |
| Frame and Decide | <time> | <time / revision> | <time or pending> |
| Act | <time> | <time / plan revision> | <time or pending> |
| Review | <time or pending> | <time / criteria revision> | <time or pending> |

<Use observed ISO 8601 times with time-zone offsets. Mark unavailable times unknown. Preserve dated amendments.>

## Frame and Decide

<Underlying problem, intended outcome, applicable values and authority.>

| Fundamental objective | Source / standing value | Measure, direction and horizon |
| --- | --- | --- |
| <Valued end> | <Attributed source> | <Comparison measure> |

| Material condition | Type | Basis | Affected choice or work | Change trigger and response |
| --- | --- | --- | --- | --- |
| <Condition> | <Given, uncertainty or assumption> | <Source or justification> | <Decision or unit> | <Change and response> |

<Save this basis before alternative evaluation. Preserve explicit requirements and resource limits.>
<Describe alternatives or link the inherited basis. Invent no choice for prescribed work.>

### Consequences

<Use this matrix or a clearer comparison.>

| Objective | Alternative A | Alternative B |
| --- | --- | --- |
| <Objective> | <Raw consequence / evidence / uncertainty> | <Raw consequence / evidence / uncertainty> |

<Decisive tradeoff, preference source and reversal condition.>
<Save the choice or pending question, decider and exact basis revision before dependent action.>
<Add selected_at only for an actual selection.>

## Act

<Register the pickup plan and acceptance criteria before implementation: the first unit's plan at planning time, each later unit's at its own pickup. Complete prospective Review columns before relevant outcomes become known.>

| Result | Inputs / dependencies | Owner / timing | Done when | Actual evidence |
| --- | --- | --- | --- | --- |
| <Achievable unit> | <Inputs> | <Actor and trigger> | <Criterion> | <Pending, then output revision and checks> |

<Mark each result delivered, blocked or stopped before you stop. Account for every one in the scope.>
<Material failures, unresolved effects and delegated returns with their assessment.>

## Review

<Add actual findings against the registered criteria.>

| Criterion | Evidence source | Owner / window / trigger | Finding | Response |
| --- | --- | --- | --- | --- |
| <Criterion or basis link> | <Evidence> | <Assessor and timing> | <Pending, then dated result and limits> | <Action and owner> |

<Keep delivery acceptance distinct from benefits. Add later observation only when useful or owed.>
<After obligations are resolved, record Closure with its actor, time, reason and evidence.>

## Changes

<Revision, time, change, source, reason and affected work. Link earlier bases and authority by exact revision.>
