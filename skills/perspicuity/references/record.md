# Keep one evolving record

The record preserves the intention, decision basis, authority, work and observed results across conversations.
It supplies an inspectable account of stated reasons and evidence, without establishing a model's internal computations.
Keep the decisive basis in the main account.
Link supporting detail instead of repeating it.
Keep the current stage accounts and timing entries consistent with the latest findings.
Replace superseded detail with exact revision links when version history preserves it.
Keep a brief change entry for each material amendment.
Retain earlier detail in the record when no recoverable version exists.

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

State the mode in progress under `Current position`: `Run` or `Plan`.
`Run` executes granted units and stops at the return.
`Plan` establishes frames, objectives, alternatives and selections, registers the work they authorize, and stops at ratified decisions and registered grants.
An opening planning run declares its mode before the first choice.
Change the mode only when the work's purpose changes, and keep the earlier mode with its reason.
A planning request stops at the boundary even when the authority to act already exists.
Neither mode supplies authority by itself.

The mode sets the stopping condition.
It does not remove a required element: planning still establishes the basis a decision needs, and execution still registers what it observed.
Keep a single unit short enough to pass through in `Run` without a planning stop.
Continue in `Run` when the record already holds the settled choice and the grant.

## Register before dependent work

Register a basis by saving its contents with the time and an exact revision reference.
Registration supplies no approval or additional authority.

| Before | Save |
| --- | --- |
| Alternative evaluation | Adopted frame, applicable values, fundamental objectives, material conditions and authority |
| Dependent action | Actual choice, comparison, decisive reason, decider and applicable grant |
| Implementation | Achievable results, inputs, dependencies, owners, timing and acceptance criteria |
| Relevant outcomes become known | Review criteria, evidence sources, review owner and observation window or trigger |

Give each objective an attributed source, measure, preferred direction and relevant horizon.
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
| granted | A registered grant with its includes, excludes and stop condition. |
| picked up | A registered pickup plan, the actual actor and the start time. |
| returned | The exact output revision, its checks, material failures and unresolved obligations. |
| accepted | An assessment against the original criteria, with the assessor named. |

Store the ratified basis and the grant in the unit's own row, so a state reached by assertion is visibly missing its reference rather than indistinguishable from a state reached by work.
A unit that inherits a parent's selection still records its own scope and basis revision.

Only a granted unit may be executed, and only within its stated scope.
A ratified decision without a grant permits none of the work it selects.
A grant is the one permission another actor may rely on without reading the whole parent account.

#### The grant

Write a grant for one unit and keep it beside that unit.
Name the actor, the work included, the work excluded and the stop condition.
A planner holding the selection authority may register it at planning time; otherwise the holder of that authority registers it.
A grant permits its own unit, and is not a general permission for the intention.
It supplies no authority to select, to change scope or to act outside the named work.
Amend a grant explicitly; a unit that needs more stops and returns to the decider.

#### Pickup and escalation

At pickup, register the pickup plan for that unit before implementing it.
Register the first unit's pickup plan at planning time and each later unit's at its own pickup, because the later plans depend on what the earlier units find.
A pickup plan states how the unit will be carried out and what will show it is done; adapting its route is the actor's call.
When the work changes the problem, the comparison or the selection, the unit returns to the decider.
That is escalation: the boundary is keyed to what changed, not to the actor's confidence, because unstated it produces drift and keyed to confidence everything escalates.
A unit stays inside its grant, and an adjoining improvement is a proposal rather than part of the return.

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
A scope that lists several results is complete only when each one is delivered, stopped or transferred.
Keep the next actor in `Next`, `Blocked` or `Waiting on` rather than implying it in prose.

The bundled dashboard reads these labels under `Current position`.
Retain that heading when using the dashboard.

### Review commitments

Assess delivery against its original criteria.
Add later observation when the task requires it or a useful learning question justifies it.
Do not create benefit reviews solely to fill the record.

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
Pass the parent basis, objectives, constraints, exact grant and return destination.
Name the output and acceptance criteria.
Distinguish the receiver's choices from prescribed rules and choices retained by the parent.
Point to guidance needed for that assignment.
Reuse settled context instead of imposing a fixed reading bundle.

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

## Compatibility

This format remains distinct from older Perspicuity `spec: 0.2` records.
Earlier `perspicuity-work/1` records may use `Dependency` for blocked work, or keep accepted delivery open for an unpromised later benefit.
Read those records as they were written.
Add `Blocked`, `Waiting on` or `in_review` when the record is next touched, and preserve the earlier wording.
An `in_review` record needs a machine-readable `review_due` date as well as `next_check`.
Preserve historical headings, identities, evidence and authority.
For an authorized migration, identify the source revision without silently relabeling it.
No database, graph or scheduler is required by this skill.
Existing project requirements still apply within their scope.

## Design basis

The design draws on [Fama and Jensen's decision responsibilities](https://ucema.edu.ar/~je49/organizacion/Fama_Jensen.pdf#page=5),
[Sutton's argument for scalable learning and search](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf),
and [OpenAI's guidance on skills for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
These sources inform the design without validating the skill or establishing identical behavior across models.
