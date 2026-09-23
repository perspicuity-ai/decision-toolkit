---
name: perspicuity
description: >-
  Plan a problem, compare choices, act, and review the result in one evolving record.
  Use for decision support, for a plan that stops at ratified choices and granted work, for executing that plan, or for reviewing returned work and finished plans.
---

# Perspicuity

Version: 0.6.0. Record format: `perspicuity-work/1`. Plan format: `perspicuity-plan/1`.

Advance the principal's intended outcomes through **Frame and Decide, Act, and Review**.
Let the decider's values guide the problem, alternatives and consequences.
Scale the method to the stakes, uncertainty, complexity and reversibility.
Repeat or overlap stages when evidence warrants.
Keep the shortest record that shows the decisive basis, current position and next action without the transcript.
The [record guide](references/record.md) explains each rule.

## Declare the working mode

Work in one mode at a time, written in Current position: `Plan`, `Run` or `Review`.
`Plan` frames, compares and selects, and stops at ratified decisions and registered grants.
`Run` carries granted units to their return and stops there.
`Review` judges work already done and stops at a registered verdict, on one return or on a whole plan.
A planning request stops at its boundary even when the authority to act exists.
A unit proceeds only under its registered grant. [Modes](references/record.md#declare-the-working-mode).

## Start or resume

Read the request and existing record, and identify the intended outcome, actual authority and next unresolved issue.
Reuse settled choices and permission within their scope.
For prescribed work, proceed in `Run` under its grant without inventing a decision; in `Plan`, register it as a unit.
For advice or inquiry, complete that scope without forcing a selection.
Ask for missing input that could materially change the work, and meanwhile continue independent work a current grant covers.

Keep the existing record identity; for a new one, adapt the [record template](assets/record-template.md).
Name at the start `Done when`, which the author checks, and `Ship to`, which someone outside the author's environment verifies; done is not shipped ([shipping](references/record.md#ship-to-a-named-destination)).
For units that must happen in an order or span repositories, write a [plan](assets/plan-template.md) that points at their records.
Read the `format` value first and apply that format's rules.
Record material events with [clock timestamps](references/record.md#timestamps).
Keep the finding, decision state and next actor visible: one actor and action in `Next`, and a line for each other pending actor.

## Who decides what

By default the principal owns the intent, frame, objectives, risk tolerance, hard-to-reverse choices and grants; the agent owns alternatives, evidence, reversible choices inside its grant, and the route.
A grant may move any of these ([default allocation](references/record.md#who-decides-what)).
Tag every consequential choice `Decided by:` with the person or agent and its authority.

## Frame and Decide

Apply decision analysis and value-focused thinking.
Test whether the frame addresses the underlying problem; propose a better one, and adopt it where the delegation gives you the frame.
Preserve explicit requirements, constraints and retained choices; record a material reframe and its reason.
Sort the problem into given, decide now and decide later; each later item becomes a planned decision unit.

Elicit fundamental objectives before developing alternatives, each with an identifier (O1, O2 …), source, measure, direction and horizon.
Reuse applicable objectives and [standing values](references/analysis.md#standing-values), attribute preferences to their sources, and distinguish ends from means.
Identify material givens, uncertainties and assumptions, with their basis and reconsideration trigger.
[Register the frame, objectives and conditions](references/record.md#register-before-dependent-work) before evaluating alternatives; preserve any later amendment and reassess what it affects.

Develop credible alternatives, including the feasible current course or the reason it is excluded.
Compare consequences under the decider's constraints and risk preferences, in native measures, with evidence, assumptions and explicit gaps.
Show the decisive consequences compactly and link the detail; see the [analysis guidance](references/analysis.md) for hard cases.
Inquire further when its likely value justifies the effort and delay.

Explain the decisive tradeoff and write `Reconsider if:` beside every selection.
If a missing preference prevents selection, keep a conditional recommendation or obtain the preference.
Keep the recommendation distinct from the authorized choice, and select only within delegated authority.
A reversible choice inside a grant takes the [short form](references/record.md#build-the-decision-chain); a hard-to-reverse one takes the full basis.
Save consequential choices and their basis before dependent action.

## Act

Apply project management to turn the choice into assessable work.
Decompose it into units, each with inputs, dependencies, owner, timing and the objectives it `Serves:`.
Give each unit a [grant card](references/record.md#the-grant) that a worker can act on without the parent's record.
For a batch, the principal ratifies the grants they own in one act at the end of `Plan`, citing each revision.
Register each unit's pickup plan at its pickup, the first at planning time, stating how the route serves the intent.
Register review criteria before observing the outcomes they assess.

Complete granted work against its pickup plan, adapting the route within the grant; amend the grant before work outside it.
Commit under a grant with `Perspicuity-Record:` and `Perspicuity-Unit:` [trailers](references/record.md#save-meaningful-changes); link outputs, checks and deviations to the pickup plan and choice revisions.
Escalate when the problem, comparison or selection changes, a tolerance is exceeded, or an excluded target is needed.
Check uncertain external effects before a retry, and preserve material failures and unresolved effects before correction.
Mark each result delivered, blocked or stopped before you stop; for a block, name the missing input, its owner and the resolving step.
To run a whole plan, follow [the run loop](references/record.md#run-a-plan).

## Delegate through this skill

Delegate with a grant card and the basis it cites.
An assignment carrying a consequential choice, or one another party depends on, gets the delegatee's own short record; otherwise the parent says why not.
The parent links that record, and assesses the return against the assignment before accepting it.
A worker sub-delegates only inside its own grant ([delegation](references/record.md#delegate-through-the-same-skill)).

## Review

Apply evaluation and adaptive management.
Assess output and consequences against the registered criteria, explain material differences, and check the work is consistent, complete and coherent with the project.
Delivery acceptance is not evidence of later benefit.
A receiver [reviewing a return](references/record.md#review-what-another-actor-sent) records arrival and acceptance separately.
At a plan's close-out, ask what was supposed to happen, what happened, why they differ and what changes, and compute the [delegation measures](references/record.md#review-a-plan).
Give every registered result one destination verdict: shipped, with outside evidence; held, with reason and owner; or abandoned, with reason.
Register what the review discovers as work with an owner.
Reconsider affected choices when evidence invalidates a material assumption, preserving the earlier basis.
Judge decision quality on the information available when choosing; a good outcome alone proves neither a good decision nor causation.
Distinguish self-checks, independent assessment and mechanical validation; use independent assessment when required or warranted.
Worker completion is not acceptance: a delivered result stays `submitted` until its receiver accepts it, then `in_review` while a check remains, else `accepted`.
Arrange later observation only for a decision, requested learning or existing commitment, with its owner, evidence and trigger ([commitments](references/record.md#review-commitments)).
Continue, correct, reconsider or close within the available authority.

## Close the commitment

Close the record once every result in its scope is accepted, stopped or transferred to a named owner.
Reconcile your scope, not another record's.

## Supporting views

Optional: [Jev guide](references/jev.md) for a requested experiment, [example](examples/pipeline.md) of an unobserved benefit, [dashboard runner](references/dashboard.md).
Keep each project's records in that project.
