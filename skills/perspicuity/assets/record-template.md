---
format: perspicuity-work/1
id: <stable identifier>
revision: 1
skill_version: 0.8.1
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

<This section is the principal's five-minute brief. Rewrite it at every stop. Each line at most 280 characters, the section at most 600 words. Gloss every identifier at first use, as in Objectives: `U1 short gloss · U2 short gloss`. Link detail; no tables here.>

Mode: <Plan, Run or Review, with the reason when it matters>

Principal and decider: <objectives owner / chooser>

Work owner: <actor>

Ask: <the principal's request, in their terms>

Objectives: <O1 phrase · O2 phrase …, or the objectives the work serves>

Options: <the alternatives compared, one phrase each; omit when none were compared>

Decision: <state and the decisive reason / basis revision / pending owner or no-choice reason; for an idea: pending, is it worth more time, and in what shape?>

Reconsider if: <the observation that reopens the choice; omit when nothing is chosen or recommended>

Work scope: <the delivery, named so a reader can tell whether it is finished>

Done when: <the criterion that shows this work is complete; checkable by its author>

Ship to: <where it must arrive, and who can verify that it did>

Work: <current finding>

Outcome: <observed result or unknown>

Needs from you: <each open question for the principal, two to four options, recommendation first; or nothing>

Next: <one actor / one action / trigger>

<Done is not shipped: the first is internal to the work, the second is a claim about a destination.>
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
<This table is optional where commits carry the Perspicuity-Record and Perspicuity-Unit trailers.>

## Frame and Decide

<Underlying problem, intended outcome, applicable values and authority.>

Given: <conditions taken as fixed> / Decide now: <this record's choices> / Decide later: <each becomes a planned decision unit>

| ID | Fundamental objective | Source / standing value | Measure, direction and horizon |
| --- | --- | --- | --- |
| O1 | <Valued end> | <Attributed source> | <Comparison measure> |

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

<Decisive tradeoff and preference source.>

Decided by: <person or agent, and the authority>

Reconsider if: <the observation that would reopen this choice>

<Save the choice or pending question, decider and exact basis revision before dependent action.>
<Add selected_at only for an actual selection.>
<A reversible choice inside a grant may use the three-line short form instead: Chose X over Y for <question>, because … / Decided by / Reconsider if.>

## Act

<Register the pickup plan and acceptance criteria before implementation: the first unit's plan at planning time, each later unit's at its own pickup. Complete prospective Review columns before relevant outcomes become known.>

| Result | Serves | Inputs / dependencies | Owner / accepted by / timing | Done when | Actual evidence |
| --- | --- | --- | --- | --- | --- |
| <Achievable unit> | <O#> | <Inputs> | <Actor / receiver / trigger> | <Criterion> | <Pending, then output revision, checks and trailer-tagged commits> |

<Give each unit a grant card before it runs. Fields already in Current position may read "as Current position".>

```
Grant <id>: <unit>
For: <actor>
Serves: <selected choice> → <O#>
Intent: <one sentence: what success lets the principal do>
Done when: <criterion the worker can check>
Ship to: <destination, and who verifies arrival>
Includes / Excludes: <scope>
Tolerances: <as the grantor states them, or "none set">; exceeding one stops the unit and escalates it
Escalate if: <the problem, comparison or selection changes; a tolerance is exceeded; an excluded target is needed>
Return to: <record or receiver, with the expected evidence>
Accepted by: <named receiver>
Granted by: <person or agent, time, basis revision>
```

<Commits made under a grant carry the trailers Perspicuity-Record: <this id> and Perspicuity-Unit: <unit id>.>

<Mark each result delivered, blocked or stopped before you stop. Account for every one in the scope.>
<Material failures, unresolved effects and delegated returns with their assessment.>

## Review

<Add actual findings against the registered criteria.>

| Criterion | Serves | Evidence source | Owner / window / trigger | Finding | Response |
| --- | --- | --- | --- | --- | --- |
| <Criterion or basis link> | <O#> | <Evidence> | <Assessor and timing> | <Pending, then dated result and limits> | <Action and owner> |

<Give every registered result one verdict: shipped with the observer's evidence, held with the reason and its owner, or abandoned with the reason.>
<Evidence that work shipped must come from outside the author's environment. Register anything the review finds as work with an owner, rather than leaving it in prose.>
<Keep delivery acceptance distinct from benefits. Add later observation only when useful or owed.>
<After obligations are resolved, record Closure with its actor, time, reason and evidence.>

## Review of a return

<Complete this section only in Review mode, receiving work another actor sent. Delete it otherwise.>

Received: <path and exact revision of what was received>

Giver: <actor and their record>

Verdict: <accepted / accepted with conditions / sent back, with the reason that must change>

| Claim | Question | Finding |
| --- | --- | --- |
| Arrival | Is the work here, complete and readable? | <Evidence, or the transport failure and its recovery owner> |
| Acceptance | Does it meet the giver's criteria, is it internally consistent and complete, and coherent with the project's direction? | <Evidence and limits> |

| Follow-up | Owner | Trigger |
| --- | --- | --- |
| <What the acceptance discovered> | <Actor> | <When or what resolves it> |

<State the receiver's standing to accept. A sibling unit or session may accept another's work; a receiver that produced the artifact or gains from accepting it has established arrival rather than acceptance, and says so.>
<Where the principal's ratification is owed, record that the work is ready for it, and do not substitute for it.>

## Changes

<Revision, time, change, source, reason and affected work. Link earlier bases and authority by exact revision.>
