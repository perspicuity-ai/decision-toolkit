# Keep one evolving record

The record carries the intention, decision basis, authority, work and observed results across conversations.
It supplies an inspectable account of stated reasons and evidence.
It does not establish which internal computations caused a model's conclusion.

## Evidence at the relevant time

Establish the decision basis before a material selection.
Establish applicable authority before external commitment or execution.
Attribute delegated selections to the agent and its actual grant.
Record actual work evidence after the action.
Keep later observations separate from the forecasts that preceded them.

Identify sources and checks that a reviewer can inspect.
Connect them to the conclusions they support.
Label explanations added after a choice with their actual date and available basis.
Do not reconstruct missing evidence as if it existed before the action.
Record a material frame change beside the original request and its reason.

## Identity and state

Use the user's existing destination and record identity when available.
For a new record, choose a stable name such as `2026-09-15-client-pipeline.md`.
Keep that name through ordinary revisions and reconsideration of the same work.
Add sections only when needed; mark material unresolved content as pending.

Use three different identifiers:

- `format: perspicuity-work/1` identifies this record convention.
- `revision` is an increasing integer for meaningful saved revisions of this record.
- `skill_version` identifies the actual skill version used for the latest update.

Keep the current decider, responsible actor, decision state, work state, outcome state and next action near the top.
Use plain state descriptions that reflect the evidence.
For example, a choice can be selected, delivery accepted and benefits still awaiting observation.

## Save meaningful changes

Save a revision when the basis or authority changes, a choice is made, work produces a material result, or review changes the next action.
Keep small drafting edits within the current working revision.
Before a context transfer, save enough current detail for another agent to resume.

Use Git or the document tool's version history when available and authorized.
Keep original submitted outputs before material corrections.
Record the revision used for a choice or assessment.
Reference exact artifacts by path and commit, native version or another resolvable identifier.
A path alone locates a file; it does not identify earlier contents.

Add one short dated change entry for each meaningful revision.
Include what changed, why, who supplied it and the previous revision.
Keep historical selections, authority and material forecasts inspectable.
When revising an objective, preserve the original criterion used to assess earlier work.
Use a small history entry with the old basis and replacement reason when no external history exists.
Retain the material values and conditions needed to compare the earlier choice with later outcomes.
Do not claim exact earlier bytes when only a summary survives.

For browser-only work, provide the current record as a downloadable file when supported.
Otherwise provide a complete copyable record and state that persistent storage is unavailable.
Ask the user to retain the current record for the next session when the host cannot preserve it.
Avoid additional status, plan, judgment and handoff documents for the same ordinary work.

## Resume safely

Read the current position, latest change entry, applicable choice and authority before continuing.
Check whether supplied files or observed external state supersede the saved position.
Treat uncertain prior actions as unresolved until their effects are checked.
Keep source gaps explicit.
Preserve both versions if concurrent edits conflict.
Reconcile their meaning before overwriting either version.

Continue from the next unresolved action without repeating settled analysis.
Use targeted retrieval for a large record rather than requiring the full conversation history.
When shortening a record, preserve the decision basis, authority, unresolved effects and next actor.

## Split only when needed

Keep deliverables and external evidence in their appropriate tools.
Link them from the record without copying them into a second record store.
A distinct intention or independently owned decision can justify a linked record.
Different workflow stages alone do not justify a split.
Retain parent links and original identities when work splits.

## Compatibility

This lightweight format is separate from the older Perspicuity `spec: 0.2` decision format.
Read older records as supplied evidence with their original identities and authority.
If migration is requested, preserve the original and identify the new record's source revision.
Do not silently relabel an old record or discard its dependencies.
No database, graph, ledger chain or scheduler is required by this skill.
Existing project requirements still apply within their scope.

## Design basis

The design draws on [Fama and Jensen's decision responsibilities](https://ucema.edu.ar/~je49/organizacion/Fama_Jensen.pdf#page=5),
[Sutton's argument for scalable learning and search](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf),
and [OpenAI's guidance on skills for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
These sources inform the design.
They do not validate this skill or establish identical behavior across models.
