---
name: perspicuity
description: >-
  Plan a problem, compare choices, act, and review the result in one evolving record.
  Use for decision support, for a plan that stops at ratified choices and authorized work, or for executing that plan and returning the result.
---

# Perspicuity

Version: 0.5.0. Record format: `perspicuity-work/1`.

Advance the principal's intended outcomes through **Frame and Decide, Act, and Review**.
Let the decider's values guide the problem, alternatives and assessment of consequences.
Scale the method and effort to the stakes, uncertainty and complexity.
Repeat or overlap the stages when evidence warrants it.
Keep the shortest record that makes the decisive basis, current position and next action reviewable.

## Declare the working mode

Work in one mode at a time: `Run` or `Plan`.
`Run` carries a settled choice through its granted units and stops at the return.
`Plan` establishes frames, objectives, alternatives and selections, registers the work they authorize, and stops at ratified decisions and registered grants.
Write the mode in the active record's Current position with the reason when it matters.
A planning request stops at that boundary even when the authority to act exists.
A unit proceeds only under its registered grant.
Use [the record guide](references/record.md#declare-the-working-mode) when a mode, grant or pickup needs explanation.

## Start or resume

Read the request and existing record.
Identify the intended outcome, actual authority and next unresolved issue.
Reuse settled choices and permission within their scope.
For prescribed work, proceed in `Run` under its grant without inventing a decision.
In `Plan`, prescribed work supplies a registrable unit rather than immediate execution.
For advice or inquiry, complete that scope without forcing a selection.
Ask for missing input when it could materially change the work.
Continue independent work that a current grant already covers while an answer remains pending.

Maintain the existing record identity.
For a new record, adapt the [compact template](assets/record-template.md).
Record observed stage starts, saved bases and finishes with [clock timestamps](references/record.md#timestamps).
Read the relevant [record-guide section](references/record.md) when registration, metadata or resumption needs explanation.
Keep the current finding, decision state and next actor visible.
Name one actor and one action in `Next`. Give any further pending actor a separate line.
Link deliverables in their existing tools.

## Frame and Decide

Apply decision analysis and value-focused thinking.
Ask whether the frame addresses the right underlying problem.
Consider a broader formulation when it reveals solutions that better serve the decider's values.
Adopt a useful reframe within the delegation.
Preserve explicit requirements, constraints and retained choices.
Record a material frame change and its reason.

Elicit fundamental objectives before developing and evaluating alternatives.
Reuse applicable objectives and [standing values](references/analysis.md#standing-values).
Distinguish desired outcomes from proposed means.
Establish how achievement would be recognized.
Attribute objectives and preferences to their sources.
Ask for missing preferences when they could change the choice.

Identify material givens, uncertainties and assumptions.
Record their basis, affected work and conditions for reconsideration.
[Register the frame, objectives and conditions](references/record.md#register-before-dependent-work) before evaluating alternatives.
If later inquiry changes that basis, preserve the amendment and its reason.
Reassess affected alternatives against the revised basis.

Develop credible alternatives that could achieve the objectives.
Compare consequences under the decider's constraints and risk preferences.
Keep exact observations and calculations in their native measures.
Support material consequence claims with evidence, stated assumptions and explicit gaps.
Show the decisive consequences in a compact table or another suitable representation.
Link detailed evidence.
For difficult framing, estimates or tradeoffs, use the [analysis guidance](references/analysis.md).
Pursue further inquiry when its likely value to the decision justifies the effort and delay.

Explain the decisive tradeoffs and what would warrant reconsideration.
If a missing preference prevents selection, retain a conditional recommendation or obtain that preference.
Keep the recommendation distinct from the authorized final choice.
Use existing delegated authority to select, then register the grant for the units that follow.
Save consequential choices and their basis before dependent action.

## Act

Apply project management to turn the choice into assessable work.
Describe the intended implementation.
Decompose the work into units with useful results at the scale of the task.
Identify material inputs, dependencies, owners, timing and acceptance criteria.
Register the pickup plan for the first unit at planning time and for each later unit at its own pickup.
Register review criteria before observing the outcomes they assess.

Complete the work that a registered grant covers against its pickup plan.
Mark each planned result delivered, blocked or stopped before you stop. Add the actual evidence.
For a block, name the missing input, its owner and the resolving step.
Link outputs, checks and material deviations to the applicable pickup plan and choice revisions.
For delegation, provide the [bounded assignment and return](references/record.md#delegate-through-the-same-skill).
Assess returned work against that assignment.
Preserve material failures and unresolved effects before correction.
Check uncertain external effects before a retry.
Adapt the route within the registered grant.
Keep each unit inside its grant; amend the scope before work outside it.
Return to Frame and Decide when new evidence changes the problem, comparison or selection.
Seek additional authority only for changes or actions outside the registered grant.

## Review

Apply evaluation and adaptive management.
Assess the output and observed consequences against the registered criteria.
Keep delivery acceptance separate from evidence of later benefit.
Explain material differences between expected and observed results.
Reconsider affected choices when evidence invalidates a material assumption.
Preserve the earlier basis when recording a changed decision.
Assess decision quality using the information available when the choice was made.
A good outcome alone does not establish a good decision or causal success.
Distinguish self-checks, independent assessment and mechanical validation.
Use independent assessment when required or warranted by consequential uncertainty.
Continue, correct, reconsider or close within the available authority.
A delivered result with an outstanding check becomes `in_review`; with none, `accepted`, and the record closes.
Arrange later observation when it serves a useful decision, requested learning or an existing commitment.
For an owed later review, retain its owner, evidence and useful observation trigger.
Use the [review commitments](references/record.md#review-commitments) for delayed observation and resumption.
Keep unresolved work visible at every stop.

## Close the commitment

Leave nothing stopped in an unnamed state.
At every stop, account for each result in the work scope and its pickup plans: delivered, stopped with a reason, or blocked with its resolving step.
Close the record once every result is delivered, stopped or transferred to an identified owner.
Reconcile that scope, not another record's.
This applies whether you continue or stop, so committed work does not accumulate as an open queue.

## Supporting views

For an explicitly requested Jev experiment, use the [Jev guide](references/jev.md).
Use the [fictional example](examples/pipeline.md) when a completed output has an unobserved benefit.
For local record browsing, use the [dashboard runner](references/dashboard.md).
Select the user's project root.
Keep each project's records in that project.
