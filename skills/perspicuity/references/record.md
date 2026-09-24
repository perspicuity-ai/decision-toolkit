# Keep one evolving record

The record preserves the intention, decision basis, authority, work and observed results across conversations.
It supplies an inspectable account of stated reasons and evidence, without establishing a model's internal computations.
Keep the decisive basis in the main account.
Link supporting detail instead of repeating it.
Keep the current stage accounts and timing entries consistent with the latest findings.
Replace superseded detail with exact revision links when version history preserves it.
Keep a brief change entry for each material amendment.
Retain earlier detail in the record when no recoverable version exists.

## Two formats, told apart by their header

A record accounts for one intention through its choice, work and review: `format: perspicuity-work/1`.
A plan accounts for the order of several units across one or more repositories: `format: perspicuity-plan/1`.
Read the `format` value before anything else, and apply the matching rules below.
Treat any other value as a document this convention does not govern, including earlier `spec: 0.2` records.
A plan never replaces the records its units point to.

### Which one to write

Write a **record** when the work is one intention: a choice, the work it authorizes, and the review of what came back.
Write a **plan** when several units must happen in an order, when a unit waits on a different repository, or when something moves between repositories.
Write a plan first when the frame is shared and the units do not yet exist; the units become records as they are decided.
Keep both when a plan's unit is itself consequential: the plan then points at that unit's record instead of restating it.

### What each format owns

| Concern | Record | Plan |
| --- | --- | --- |
| Decision basis, alternatives, selection | Yes | Only the frame the units share |
| Authority for a unit | The unit's own grant | Names the repository and the unit; no grant |
| Unit state | Its own `work_status` | Points at the record; restates no state |
| Order and prerequisites | No | Yes, and only here |
| Cross-repository scope | No | Yes, through the `repos` map |
| Evidence and review | Yes | Only whether the plan as a whole is finished |

Sequence belongs to the plan alone.
Do not add an ordering field to a record, and do not copy `work_status` into a plan.
A unit is eligible when every unit it waits on is accepted in its own record; resolve that from the plan's relations and the records' states.

## Write the useful account

Use **Frame and Decide, Act, and Review** for new records.
The first stage establishes the problem, valued outcomes, comparison and selection within the delegation.
These stages can overlap or repeat.
Adapt headings to the work.
Retain historical headings when resuming an existing record.

| Stage | Useful content |
| --- | --- |
| Frame and Decide | Frame, values, fundamental objectives, material conditions, alternatives, consequences and selection or unresolved question |
| Act | Execution plan, acceptance criteria, exact outputs, checks, material failures and unresolved effects |
| Review | Prospective criteria, evidence, observation window, actual findings and next response |

Consider standing values through [the analysis guidance](analysis.md#standing-values).
For prescribed work, link the inherited basis.
For evidence-only work, identify who retains the choice.
Neither case requires invented alternatives.
Expand only where detail changes the choice, authority, assessment or next action.
Omit irrelevant tables from the template.
Use one row or a sentence for simple work.

### Declare the working mode

State the mode in progress under `Current position`: `Plan`, `Run` or `Review`.
`Plan` establishes frames, objectives, alternatives and selections, registers the grants they authorize, and stops at ratified decisions and registered grants.
`Run` executes granted units and stops at the return.
`Review` judges work already done against what was registered for it, and stops at a registered verdict.
It has two scopes: a return, meaning one received artifact or handover ([review what another actor sent](#review-what-another-actor-sent)), and a plan at its close-out ([review a plan](#review-a-plan)).
An opening planning run declares its mode before the first choice.
Change the mode only when the work's purpose changes, and keep the earlier mode with its reason.
A planning request stops at the boundary even when the authority to act already exists.
No mode supplies authority by itself.

The mode sets the stopping condition.
It does not remove a required element: planning still establishes the basis a decision needs, execution still registers what it observed, and review still records its evidence and its verdict.
Keep a single unit short enough to pass through in `Run` without a planning stop.
Continue in `Run` when the record already holds the settled choice and the grant.

A mode and a format are different things.
The mode is the session's purpose and is written in the body; the format is the artifact's header contract and is read from the frontmatter.
`Review` adds no format: a review of a return is a record under `perspicuity-work/1` that points at what it received, and a plan's close-out is part of the plan.
The `Review` mode shares its name with the Review stage because it is that stage carried out by a receiver, or across a whole plan.
Records written before 0.6.0 may declare `Accept`; read it as `Review` of a return.

## Register before dependent work

Register a basis by saving its contents with the time and an exact revision reference.
Registration supplies no approval or additional authority.

| Before | Save |
| --- | --- |
| Alternative evaluation | Adopted frame, applicable values, fundamental objectives, material conditions and authority |
| Dependent action | Actual choice, comparison, decisive reason, decider and applicable grant |
| Implementation | Achievable results, inputs, dependencies, owners, timing, acceptance criteria, the completion criterion and the destination |
| Relevant outcomes become known | Review criteria, evidence sources, review owner and observation window or trigger |

Give each objective an identifier (O1, O2 …), an attributed source, a measure, a preferred direction and a relevant horizon.
Units, grants and review criteria cite the objectives they serve with `Serves:`.
Link inherited objectives and authority instead of copying them.

Keep material givens, uncertainties and assumptions explicit.
A given is a supplied or verified condition with an identified source.
An uncertainty is a relevant fact or future outcome that remains unknown.
An assumption is an unverified claim treated as true for the current analysis or work.
Identify the choice or work each condition affects.
Record a meaningful change trigger and response where needed.

Divide the undertaking into achievable results when coordination requires it.
Add actual evidence after the work.
If relevant outcomes are already known, label the criteria retrospective.

### Ship to a named destination

Name both the completion criterion and the destination when the work is registered, in `Current position`.

| Field | Answers | Who can check it |
| --- | --- | --- |
| `Done when` | Is the work complete against its criteria? | Its author, by test or inspection |
| `Ship to` | Where must it arrive, and who can verify that it did? | The destination's observer, or the receiver |

Done is not shipped, and the four claims are separate: built, verified, shipped, effective.
Any one can be true while another is false.

Evidence for a shipping claim must come from outside the author's environment.
A commit message, a changelog, a passing test on the author's machine and a summary written by the author cannot establish that anything shipped.
This is the same distinction as a self-check against independent assessment, applied to delivery rather than to quality.

Name the destination in terms that fix what would count as arrival.
The destinations in ordinary use, and the evidence each accepts:

| Destination | What it means | Evidence of arrival |
| --- | --- | --- |
| A live surface | The public reaches it | An anonymous request to the real address, or a read of the deployed store |
| The shared revision | Later work builds on it | The commit is an ancestor of the remote's main branch |
| Another unit or session | Another owner now depends on it | That owner's acceptance record, naming what it now holds |
| An external recipient | A message, post or submission left the organisation | A delivery receipt from the platform |
| A fixed artifact | Someone can install it | A download by someone other than its author, with a matching hash |
| The principal's decision | A person with authority gives their word | That person's words, recorded by whoever heard them |

The last row is ratification, not shipping.
Ratification changes what may be done; shipping changes where the work is.
Record them separately.

Where the destination is another actor, the record names that actor as its outstanding dependency until their acceptance exists, so a handover cannot become a silent stall.

### State the shippable unit as checks

Name a plan's finished product in `Ships as`, in `Current position`, when you register the plan.
`Ships as` is a numbered list of checks that together show the product is at its destination.
Give each check one kind.

| Kind | What the check is | Who runs it |
| --- | --- | --- |
| `auto` | A command; exit status 0 passes | The loop, in every iteration |
| `observer` | A named actor outside the author's environment, and what that actor inspects | That actor; the loop records their words |

Write the plan's `Done when` so that it cites `Ships as`: every check passes, every unit is accepted, stopped or transferred, and the close-out is held.
A `Done when` that counts units alone describes a ledger, not a product, because stopped and transferred units satisfy it when nothing has shipped.
Keep effects out of `Ships as`.
An effect, such as people understanding a page or a behaviour changing, needs time or people the work does not control; register it as a [review commitment](#review-commitments).
Keep ratification out of `Ships as`.
Put a principal's decision that a check needs in the [pre-run gate](#run-a-plan).
Size the shippable unit to what the loop can reach under its grants.
Move a check that the loop cannot reach to a named later plan, and list it under `Later`.
After Run begins, change `Ships as` only by an amendment the principal ratifies, with the reason in Changes.

### Review what another actor sent

A review of a return exists because the author of a change cannot observe that the world received it.
The receiver can, and the receiver's acceptance is the evidence that a shipping claim is true.

An acceptance settles two claims, and keeping them apart stops it becoming a second opinion on quality alone.
It is held in `Review` mode.

| Claim | The receiver's question | When it fails |
| --- | --- | --- |
| Arrival | Is the work here, complete, and readable by me? | A transport failure; name the failure and a recovery owner |
| Acceptance | Does it meet the criteria the giver registered, is it internally consistent and complete, and is it coherent with the project's direction? | A correction, not a rejection of the whole |

An acceptance is a record in the receiver's own repository, under the receiver's own identity.
It is not an edit to the giver's document and not a separate format.
Record:

- what was received, by path and exact revision, because a path alone does not identify a revision;
- the verdict: accepted, accepted with conditions, or sent back with the reason that must change;
- the arrival evidence, and the acceptance evidence against the giver's registered criteria;
- every follow-up the acceptance discovers, each with an owner;
- the receiver's standing to accept, because mechanical completion does not establish sound judgment;
- where the principal's ratification is owed, that the work is ready for it, without substituting for it.

A sibling unit or session may accept another's work; that is the ordinary case and needs no extra approval.
Independence is measured against the work, not against the org chart: a receiver that produced the artifact, or that stands to gain from accepting it, has established arrival rather than acceptance, and says so.
Treat sibling acceptance as the starting assumption and revisit it if acceptance starts passing work that later proves unsound.

Where the giver's criteria are absent or unregistered, the receiver cannot accept: the verdict is that acceptance is blocked for want of a criterion, and the follow-up is registered against the giver.

### Review a plan

Hold a plan's close-out in `Review` mode as the last step of a `finished` loop, or when the principal ends the plan at `stopped`.
Answer four questions: what was supposed to happen, what happened, why the two differ, and what changes next time.
Then compute the delegation measures from the unit records.

| Measure | Direction |
| --- | --- |
| Choices made outside a grant, found at acceptance | Lower is better |
| Units whose decisive basis and grant a reader recovers without the transcript | Higher is better |
| Principal interruptions per delivered unit during the run | Lower is better |
| Units that served the ratified decision | Higher is better |
| Escalations raised, and how many were warranted | Report both |
| Grant amendments, and units sent back | Report both |

Give the plan one verdict: close; correct, meaning more work within the existing grants; or reconsider, meaning a return to Frame and Decide.
Register each finding that should change a skill, a template, a standing value or a later plan as work with an owner.
The close-out judges the plan; each unit's own criteria stay in its record.

### Show consequences compactly

Use a table when it makes alternatives easier to compare.
Keep factual and calculated measures in their original units.
Keep material unknowns and source limits beside the affected consequence.
Link detailed research or calculations when they support the comparison.

## Evidence at the relevant time

Establish applicable authority before execution or external commitment.
Attribute delegated selections to the actor and actual grant.
Connect conclusions to inspectable sources and checks.
Keep forecasts distinct from later observations.
Label retrospective explanations with their actual date and evidence.
Record material frame changes beside the original request and their reason.

## Build the decision chain

Keep smaller choices inside the continuing record when they serve the same intention.
A consequential choice has credible alternatives that materially affect outcomes, behavior, authority, dependencies or review obligations.
This includes research choices, such as an evidence rule that changes a conclusion.
Distinguish supplied rules from rules selected by the agent.
An evidence interpretation alone does not require preferences about which facts are true.

Give each consequential choice a stable section or direct link.
Save its question, comparison, reason, decider, authority and basis revision before dependent action.
Write the decider as `Decided by:`, naming the person or agent and the authority, and the reversal condition as `Reconsider if:` beside the selection.

A choice that is cheap to reverse and sits inside a grant may use the short form:

```
Chose: <X> over <Y, Z> for <question>, because <decisive reason, citing O#>
Decided by: <agent or person> under <grant or authority>
Reconsider if: <observation>
```

A choice that is hard to reverse, commits the principal externally or would change a grant takes the full basis.
Link applicable parent findings instead of copying them.
Connect the output to the choice it implements.
Keep routine edits in the action account.

For several dependent choices, use a compact index of owners, states and dependencies.
Mark anticipated choices as planned until selection occurs.
A planned branch supplies no execution grant.
Add a diagram only when relationships need it.
Keep direct record links beside the diagram.

A work unit moves through these states, and a unit may skip none of them by asserting a later one.
Keep each unit's current state in the index, with the reference that the state requires.

| Unit state | What it requires |
| --- | --- |
| planned | A question or intended result, its owner and its dependencies. The unit's own choice is not yet selected. |
| ratified | The choice saved with its comparison, reason, decider and basis revision. |
| granted | A registered [grant card](#the-grant). |
| active | A registered pickup plan, a claim naming the actual actor, and the start time. |
| submitted | The exact output revision, its checks, material failures and unresolved obligations. |
| accepted | An assessment against the original criteria, with the assessor named. |

A unit may also be `waiting`, with its missing input named, or `stopped`, with its reason.
These words reuse the header's `work_status` values where both exist.
In an Act table, a result marked delivered has reached at least `submitted`, and one marked blocked is `waiting`.
Records written before 0.6.0 may use `picked up` for active and `returned` for submitted; read them as written.

Store the ratified basis and the grant in the unit's own row, so a state reached by assertion is visibly missing its reference rather than indistinguishable from a state reached by work.
A unit that inherits a parent's selection still records its own scope and basis revision.

Only a granted unit may be executed, and only within its stated scope.
A ratified decision without a grant permits none of the work it selects.
A grant is the one permission another actor may rely on without reading the whole parent account.

#### Who decides what

This is the default allocation between the principal and the agent.
A grant or the principal's instruction may move any row.

| Element | Default owner | The other party's part |
| --- | --- | --- |
| Intent, frame, and what is given, decided now or decided later | Principal | Agent drafts, challenges and proposes a reframe |
| Fundamental objectives and risk tolerance | Principal | Agent elicits and proposes measures |
| Alternatives and consequence estimates | Agent | Principal adds |
| Choices that are hard to reverse or commit the principal externally | Principal | Agent recommends |
| Reversible choices inside a grant | Agent, in the short form | Principal sees them at review |
| Grants, tolerances and acceptors | Principal ratifies | Agent drafts |
| Route and pickup plan | Agent | |
| Acceptance of a unit | The receiver the grant names | |
| Shipping verdict | An observer outside the author's environment | |
| Plan close-out | Principal | Agent drafts the measures |

#### The grant

Write a grant for one unit, as a card beside that unit, so a worker can act on it without the parent's record.

```
Grant <id>: <unit>
For: <actor>
Serves: <selected choice> → <objective IDs>
Intent: <one sentence: what success lets the principal do>
Done when: <criterion the worker can check>
Ship to: <destination, and who verifies arrival>
Includes / Excludes: <the work included and the work excluded>
Tolerances: <wall time, attempts, spend>; exceeding one stops the unit and escalates it
Escalate if: <the problem, comparison or selection changes; a tolerance is exceeded; an excluded target is needed>
Return to: <record or receiver, with the expected evidence>
Accepted by: <named receiver>
Granted by: <person or agent, time, basis revision>
```

`Done when`, `Tolerances` and `Escalate if` together are the unit's stop condition.
A unit inside one record may write "as Current position" for a field its Current position already holds.
Set a tolerance only as the grantor states it; where none is stated, write that none is set.
A planner holding the selection authority may register a grant at planning time; otherwise the holder of that authority registers it.
For a batch, the principal ratifies the grants they own in one act, at the end of `Plan`, citing each grant's revision.
A grant permits its own unit, and is not a general permission for the intention.
It supplies no authority to choose between the alternatives of the decision it implements, to make a hard-to-reverse choice, to change scope or to act outside the named work.
Under the [default allocation](#who-decides-what), the worker makes reversible choices inside its includes and records them in the short form.
Amend a grant explicitly; a unit that needs more stops and escalates to the decider.
A worker may sub-delegate only inside its own grant's includes.

#### Pickup, claims and escalation

At pickup, register the pickup plan for that unit before implementing it.
Register the first unit's pickup plan at planning time and each later unit's at its own pickup, because the later plans depend on what the earlier units find.
A pickup plan states how the unit will be carried out, how that route serves the grant's intent, and what will show it is done; adapting its route is the actor's call.
A worker that cannot connect its route to the intent has found that the problem or the selection may have changed, and escalates before starting.

Claim the unit at pickup with `Claimed by:` and `since:`.
One actor writes a record at a time; another actor records its work in its own record and links it.
A claim older than the grant's time tolerance, with no return, may be taken over after the new actor checks the uncertain external effects of the earlier attempt.
Where the grant sets no time tolerance, only the grantor or the actor running the plan may take over a claim, after the same check.

Escalate, referring the unit to the decider, when the work changes the problem, the comparison or the selection, when a tolerance is exceeded, or when an excluded target is needed.
The boundary is keyed to what changed and to limits set in advance, not to the actor's confidence, because unstated it produces drift and keyed to confidence everything escalates.
A unit stays inside its grant, and an adjoining improvement is a proposal rather than part of the return.

## Write a plan

A plan lists the units that must happen in an order, the relation that orders them, and the repositories they span.
It carries the frame the units share and points at each unit's record; it decides nothing itself.
Keep it thin: what a reader cannot get from the units belongs here, and what they can does not.

### Header fields

| Header field | Meaning |
| --- | --- |
| `format: perspicuity-plan/1` | This plan convention |
| `repos` | The alias map described below; omit when every unit is in the plan's own repository |

Use `id`, `revision`, `skill_version`, `updated`, `created_at` and `updated_at` as a record does.
Use `plan_status` in place of `work_status`, with `not_started`, `active`, `waiting`, `in_review`, `accepted` or `stopped`.
A plan is `accepted` only when every `Ships as` check passes and every unit is accepted, stopped or transferred to a named owner.
Set `next_check` for a timed obligation, exactly as a record does.

### Units

Give every unit one row.

| Column | Content |
| --- | --- |
| Unit | A short name, and the record that owns it when one exists |
| Kind | `decision`, `work`, `evidence`, `move` or `gate` |
| Waits on | The units that must be accepted first, by name; empty when none |
| Repository | The alias from `repos`, or `local` for the plan's own repository |
| Owner | One actor |
| Serves | The objective IDs the unit serves |
| Accepted by | The receiver whose acceptance counts; required for a unit that may run without the principal present |

Name a unit's record by repository-qualified path and, when the unit's basis is a section, its anchor.
Leave the record cell empty while a unit is intended but undecided, and fill it when the unit's record is registered.
Do not restate a unit's state: read it from the record, and read `intended` only where no record exists yet.

### Order

State the order once, as relations rather than as a numbered list, because several units may run together.
A unit is eligible when each unit it waits on is accepted in its own record, and when its own grant covers the actor.
Where an order is not a simple prerequisite, say what the real condition is.
A gate is a unit whose acceptance is another unit's condition; a move is a unit that changes a repository's content.

### Run a plan

Hold the pre-run gate before `Run` begins.
List every principal decision, credential, account action and human-only step that a `Ships as` check or a granted unit needs.
For each item, record the answer, or move the check or unit that needs it to a named later plan.
Do not start a plan in a loop while a check or unit waits on an item from this list.
An input that arises during the run is an escalation, not a gate failure.

An actor running a plan in `Run` repeats one loop.

1. Find the eligible units.
2. Dispatch each with its grant card.
3. Have each return reviewed by the receiver its grant names, which accepts it, accepts it with conditions or sends it back.
4. Close each record whose results its receiver accepted in this iteration and that has no open review commitment.
5. Run the `auto` checks in `Ships as`, and record the result.
6. Recompute eligibility.

End the loop at one of three exits, and write the exit and its time in the plan's `Current position` as `Exit:`.

| Exit | Condition | `plan_status` | What the loop writes |
| --- | --- | --- | --- |
| `finished` | Every `Ships as` check passes, every unit is accepted, stopped or transferred, and the close-out is held | `accepted`, or `in_review` while a review commitment remains | The close-out, and the closure of each unit record that has no open review commitment |
| `parked` | The remaining work needs an input that no grant supplies | `waiting` | Each missing input, its owner, and the exact command that resumes the loop |
| `stopped` | A tolerance the principal set is reached; escalations block every remaining unit; or no unit remains eligible while a `Ships as` check fails | `waiting`; `stopped` when the principal ends the plan | The tolerance, the escalations or the failing check, and who decides next |

A `parked` exit is not a success.
Report it as the shippable unit not reached, and name the gate item that was missing, or the escalation that arose.
Resume a parked plan with the same plan and loop file.
Do not write a new plan or loop file around the remainder.
An escalation on one unit does not stop units that do not depend on it.
Hold the plan's close-out in `Review` ([review a plan](#review-a-plan)) as the last step of `finished`, and when the principal ends a plan at `stopped`.
The [loop template](../assets/loop-template.md) is one way to write the loop's instructions.
Adapt it to the project.
No scheduler is required: the loop describes what the running actor does.

### Repositories

Keep every path inside the plan repository-relative.
Resolve a link against the plan's own directory, so the depth matches where the plan sits; a plan one level deeper than the record it cites needs one more step up.
A link that does not resolve creates no edge, so a broken reference is invisible to the reader rather than reported by it.
Declare each repository the plan touches in `repos`, mapping a short alias to the repository's qualified name, so no absolute path enters a document.
State which repositories the plan may change and which it may only read.

### Moving work between repositories

A plan may describe moving content out of one repository into others.
For a move, record both sides: what leaves, and where it arrives.
Name the source, the destination, what must remain reachable afterwards, and what happens to references that crossed the boundary.
A move is complete when the destination holds the content, the source no longer does, and the references that crossed still resolve.
Keep the migration evidence in the move's own record, not in the plan.

### One plan for each destination

Keep one active plan for each destination.
Before you write a plan whose `Ship to` names a destination that an open plan already names, close the open plan with a close-out, or absorb its units into the new plan with a transfer table.
Put an idea that arrives during a run in the plan's `Later` list, not in `Ships as`.

### Where a plan lives

Put the plan in the repository that owns the intention, and name the others.
When no repository owns it, put it in a coordinating repository rather than inventing one, and say so in the frame.
Never place a plan inside a repository it only reads.

## Identity and state

Reuse the user's destination and stable record identity through revision or reconsideration.

| Header field | Meaning |
| --- | --- |
| `format: perspicuity-work/1` | This record convention |
| `id` | Stable record identifier |
| `revision` | Increasing integer for meaningful saved revisions |
| `skill_version` | Actual skill version used for the latest update |
| `updated` | Date of the latest update, retained for existing readers |
| `created_at` | Optional observed time when the record was created |
| `updated_at` | Optional observed time when the current revision was saved |
| `closed_at` | Optional observed time when the record's obligations were closed |

Keep the decider, work owner, current state and next action near the top.
Separate the visible fields with blank lines so Markdown preserves their layout.
Use a `Decision` statement with `pending`, `recommended`, `selected`, `inherited` or `none`.
Link its basis and revision when available.
For a pending choice, name the unresolved question and owner.
For `none`, explain whether the work supplies evidence or applies a prescribed basis.
Distinguish local choices from the parent's retained choice.

### Timestamps

Use an ISO 8601 timestamp with `Z` or a numeric time-zone offset for each known event time.
Quote timestamp values in YAML.
Read the available clock for current events.
Keep `updated` consistent with the update date in the record's calendar.

| Field | Event |
| --- | --- |
| `began_at` | Work in the named stage begins |
| `registered_at` | The prospective basis is saved, with its exact revision reference |
| `finished_at` | The named stage's work finishes for this increment |
| `selected_at` | The decider makes the selection |

Keep stage times in the stage account or a compact timing table.
The table is optional where commits carry [trailers](#save-meaningful-changes), because commit times and the decision timestamps then give a more exact account.
Save the selection separately with `selected_at` and the choice revision.
For Review, registration can precede `began_at` because criteria precede assessment.
Preserve each material recurrence or amendment with its own revision and time.
Leave future events pending.
Omit unavailable times or mark them unknown.
Label retrospective estimates and their evidence.
Keep the time of documentation distinct from the event time.

Stage intervals measure elapsed time, including waits.
They do not establish active effort, token use or cost.
Keep overlapping intervals distinct instead of adding them into a work total.
Timestamp material events rather than every reasoning step.
Keep selection, delivery completion and record closure distinct.

### Find open work

Use these fields for new or resumed records.
Classify historical records only after inspecting their evidence.
Leave uninspected records visibly unclassified in derived views.

| Field | Values | Meaning |
| --- | --- | --- |
| `record_status` | `open`, `closed` | Whether a choice, delivery or promised review remains unresolved |
| `work_status` | `not_started`, `active`, `waiting`, `submitted`, `in_review`, `accepted`, `stopped` | State of the delivery named in `Work scope` |
| `next_check` | ISO date, `YYYY-MM-DD`; omit without a timed obligation | Earliest date an actor must inspect the record again |

Name the delivery in `Work scope`.
Give one actor and one action in `Next`.
List any further pending actor or action on its own line, so a reader can identify the current move.
If work waits, name the missing input in `Blocked`, the resolving actor in `Waiting on`, and the step that resolves it in `Dependency`.
For partial delivery, name each registered result as delivered, blocked or stopped.
Use `submitted` while delivery awaits acceptance.
Use `in_review` when the delivery is complete and an accepted check, decision or observation remains.
Its card records the check date and evidence; more work returns the delivery to `active`.
Use `accepted` when no further obligation remains, and close the record.
A later benefit with no promised check does not keep delivery open.
Use `stopped` when the owner discontinues it, with the reason.
An `active` state describes recorded work, without proving that an agent currently runs.
A state or due date supplies no authority to act.
Preserve earlier acceptance when a new increment begins.
Name that increment before changing its work state.

State the scope so a reader can tell whether it is finished.
A scope that lists several results is complete only when each one is accepted, stopped or transferred.
Keep the next actor in `Next`, `Blocked` or `Waiting on` rather than implying it in prose.

The bundled dashboard reads these labels under `Current position`.
Retain that heading when using the dashboard.

### Review commitments

Assess delivery against its original criteria.
Check that the work is internally consistent and complete, and coherent with the project's direction.
Add later observation when the task requires it or a useful learning question justifies it.
Do not create benefit reviews solely to fill the record.

Give every registered result one verdict, and record it in the Review table rather than in prose.

| Verdict | Meaning | What it needs |
| --- | --- | --- |
| Shipped | It arrived at its registered destination | The observer's evidence, from outside the author's environment |
| Held | It is complete but not yet at its destination | The reason, and the owner who resolves it |
| Abandoned | It is not going to arrive | The reason, and who decided |

A review that finds work outside the registered results registers it as work with an owner at that moment.
Findings left in prose are the residue that keeps records open without anyone owning them.

A criterion that was never registered cannot be assessed: record the gap and who owns it rather than accepting the work against a criterion invented afterwards.

For each promised review, record its question, evidence source, observation window, owner and due date or event.
An `in_review` delivery needs its check date and evidence source; otherwise it is blocked waiting on them.
For an uncertain event, give a fallback check date.
Keep different owners or dates distinguishable.
Summarize outstanding reviews near the current position.
Set `next_check` to the earliest outstanding checkpoint.
Use the project's calendar, with a time zone for a specified time.
Distinguish a recorded commitment from an actual scheduled reminder.
A record alone does not wake an agent.

At a checkpoint, record the finding and response before advancing the date.
An early check can establish evidence collection without establishing the later outcome.
Keep overdue reviews visible until resolved or changed by their owner.
Keep accepted delivery at `accepted` while promised observation keeps its record `open`.
Remove `next_check` only when no timed obligation remains.
Use the host's authorized scheduling method for unattended checks.

### Close or reopen

Close only after every obligation is fulfilled, explicitly cancelled or transferred to an identified receiving record.
Account for each result in the work scope, including stopped or superseded ones.
Set delivery to `in_review`, `accepted` or `stopped` before closure.
Use `accepted` only when no further obligation remains, so completed delivery does not stay in the open queue.
Close a record in the step where its receiver accepts its last result, unless a review commitment remains open.
Do not leave the closure for a later session.
A record whose results are all accepted and whose `Next` reads none is ready to close, not active.
Record `Closure` with its actor, date, reason and evidence.
Add `closed_at` when the closure time is known.
Preserve unknown benefits if the owner ends observation without resolving them.
If the same intention needs more work, reopen the same identity.
Record the trigger in Changes.
Preserve the earlier closure time in history before removing the current `closed_at`.
Thread archival remains separate.

## Save meaningful changes

Save a revision when the basis, authority, selection, material result or review response changes.
Keep small drafting edits within the current working revision.
Use authorized Git or document history to preserve earlier versions.
Keep submitted outputs before material corrections.
Reference exact artifacts by path and commit, native version or another resolvable identifier.
A path alone does not identify earlier contents.

Every commit made under a grant carries the record trailer and one unit trailer for each unit it serves, so a unit's build history is one query:

```
Perspicuity-Record: <record id>
Perspicuity-Unit: <unit id>
```

`git log --all-match --grep='^Perspicuity-Record: <record id>$' --grep='^Perspicuity-Unit: <unit id>$' --format='%h %aI %s'` lists what was built for that unit, and when.
A return still names its exact output revision; the trailers find every commit behind it.
A commit that only updates the record carries the record trailer alone.

Record each material change with its actor, time, source, reason, previous revision and affected work.
Preserve historical selections, authority and assessment criteria.
Amend a registered basis when new evidence or authorized direction warrants it.
Apply the amended basis consistently across the affected alternatives or work units.
Retain results against the criteria that governed them at the time.
Keep any later assessment under amended criteria separately attributable.
An amendment supplies no authority beyond the applicable grant.
When version history is unavailable, retain the earlier material basis in the change entry.
Do not claim exact earlier bytes when only a summary survives.
For sessions without persistent storage, supply a downloadable or copyable record with that limitation stated.

## Keep the record disclosive

The record carries the decisive basis, the grant, the acceptance criteria and the stop condition.
Evidence, research, calculations and source extracts live in their native source and are linked.
Put a table in the record only when the comparison itself changes the choice.
A reader should reach the current position and the next action without reading the supporting material.
Disclose further detail on demand, so an inspection can go deeper without making every reader carry it.
This threshold is a rule rather than a preference, because brevity loses to thoroughness whenever an uncertain agent chooses between them.

### Write the brief

The principal reads `Current position` first, and often reads nothing else.
Write it as the brief: what was asked, what matters, what was compared, what was chosen and why, and what the principal owes next.
Rewrite it at every stop, in every mode, so that it agrees with the sections below it.
Summarizing a record for a reader means rewriting this section, not writing a second summary elsewhere.

| Slot | Content | When |
| --- | --- | --- |
| `Ask` | The principal's request, in their terms | Always |
| `Objectives` | The fundamental objectives by identifier, one phrase each | Always; for prescribed work, the objectives the work serves |
| `Options` | The alternatives compared, one phrase each | When alternatives were compared |
| `Decision` | The state, the choice and its decisive reason | Always |
| `Reconsider if` | The observation that reopens the choice | When a choice is selected or recommended |
| `Needs from you` | Each open question for the principal, or `nothing` | Always |
| `Next` | One actor and one action | Always |

The state fields of the template (`Mode`, owners, scope, `Done when`, `Ship to`, `Work`, `Outcome` and any `Blocked` or `Waiting on`) stay in the brief.
Keep each line to at most 280 characters, counted as rendered: a link counts its text and not its address.
Keep the whole section to at most 600 words, which a reader covers in about five minutes.
Give a slot one line; a slot that holds a list, such as `Ships as` or several questions, counts each item as a line.
Link detail rather than carry it, and keep tables out of the brief.
Give every identifier a short gloss where the brief first uses it, as `Objectives` does: `U4 re-measure sitewalk's error rate`, not `U4`.
A bare identifier points at detail the reader has not read, so a list of units, criteria or choices tells the reader nothing about what the work was decomposed into.
Write each question under `Needs from you` in the form the skill asks it: two to four options, the recommendation first and marked, each with its consequence.

`python3 scripts/brief_check.py <record or directory>` checks records and plans with `skill_version` 0.8.0 or later.
It reports each missing required slot, each line over 280 characters, each section over 600 words and each identifier whose first use has no gloss, and exits 1 when any record fails.
The gloss check is a heuristic: it flags an identifier followed at first use by punctuation, a joining word or another identifier, and accepts one that closes a parenthesis after its description.

## Resume safely

Read the current position, latest change, applicable choice and authority before continuing.
Check whether supplied evidence supersedes the saved position.
Verify uncertain prior effects before dependent action.
Reconcile concurrent versions before overwriting either account.
Continue the unresolved action without repeating settled analysis.
Use targeted retrieval for large records.
When shortening a record, preserve the decisive basis, authority, unresolved effects and next actor.

## Split only when needed

Keep deliverables and external evidence in their appropriate tools.
A distinct intention or independently owned decision can justify a linked record.
Different responsibilities alone do not justify a split.
Retain parent links and original identities when work splits.

### Delegate through the same skill

Use delegation when an independent assignment justifies its cost.
Pass the parent basis, objectives and constraints with the unit's [grant card](#the-grant), which carries the return destination.
Name the output and acceptance criteria.
Distinguish the receiver's choices from prescribed rules and choices retained by the parent.
Point to guidance needed for that assignment.
Reuse settled context instead of imposing a fixed reading bundle.

An assignment that carries a consequential choice, or on which another party will depend, gets its own record from the delegatee, in this skill, however short.
A delegated record is a record like any other: it declares its mode, registers what it must become, and returns its own evidence.
Where an assignment is too small to warrant its own record, the parent says so, and names why, so the omission is deliberate rather than an accident of the moment.
This applies to a sub-agent, a sibling unit and a person alike; the delegated work does not become more visible by being summarised into the parent.

Require the return's local decision basis or explicit no-new-choice account.
Include its exact output revision, checks, material failures and unresolved obligations.
Make the assignment accessible to the receiving runtime.
If transport fails, identify the failure and recovery owner.

Assess the return against the original assignment and actual output.
Check the basis and authority for consequential choices.
Save acceptance or required correction beside the return link.
Keep worker completion distinct from acceptance.
Identify the assessor and any required independence.
Mechanical completion does not establish sound judgment or sufficient evidence.

Where the parent must accept the return, it may do so in `Run` by assessing against the assignment it registered.
Where the return is substantial enough to need its own arrival and acceptance evidence, the parent names a receiver and the verdict is recorded under [review what another actor sent](#review-what-another-actor-sent).

## Compatibility

This format remains distinct from older Perspicuity `spec: 0.2` records.
Earlier `perspicuity-work/1` records may use `Dependency` for blocked work, or keep accepted delivery open for an unpromised later benefit.
Read those records as they were written.
Add `Blocked`, `Waiting on` or `in_review` when the record is next touched, and preserve the earlier wording.
An `in_review` record needs a machine-readable `review_due` date as well as `next_check`.
Records and plans written before 0.6.0 may declare `Accept`, use `picked up` or `returned` as unit states, record the verdict `returned`, or lack `Decided by`, `Reconsider if`, grant cards and an `Accepted by` column.
Read them as written, and use the 0.6.0 words and fields when the record is next touched.
Plans written before 0.7.0 may lack `Ships as` and `Exit`, and may define `Done when` by units alone.
Read them as written, and add `Ships as` and hold the pre-run gate before the plan next enters `Run`.
Records and plans written before 0.8.0 may lack the brief's slots and limits.
Read them as written, and write the brief when the record is next touched.
Preserve historical headings, identities, evidence and authority.
For an authorized migration, identify the source revision without silently relabeling it.
No database, graph or scheduler is required by this skill.
Existing project requirements still apply within their scope.

## Design basis

The design draws on [Fama and Jensen's decision responsibilities](https://ucema.edu.ar/~je49/organizacion/Fama_Jensen.pdf#page=5),
[Sutton's argument for scalable learning and search](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf),
and [OpenAI's guidance on skills for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
These sources inform the design without validating the skill or establishing identical behavior across models.
