# Perspicuity terminology

Core terms for Perspicuity's skills, strategies, and decision records.
The definitions express usage across Perspicuity's skills and decision records.

## Scope and authority

**Perspicuity**:
The repository-wide system of skills, specifications, decision records, and supporting tools.
_Avoid_: Decide when referring to the entire system.

**Frame**:
The Perspicuity responsibility for establishing the intended outcome and problem worth resolving.
The delegated agent can challenge assumptions and adopt a better analytical frame within its grant.
A reframe preserves explicit requirements and does not enlarge execution authority.

**Decide**:
The current Perspicuity responsibility for developing objectives, alternatives, consequence comparison and selection within a frame.
Historical references to the separate Decide skill retain their original human-coaching meaning.

**Decide Agent**:
The Perspicuity skill that makes a decision within delegated authority.

**Perspicuity skill**:
The single entry for preparing a choice, selecting within authority, carrying out work and reviewing results in one evolving record.
Its three stages are Frame and Decide, Act, and Review.
The first stage keeps framing explicit and registers the basis and plans prospectively.
Frame and Decide draws on decision analysis and value-focused thinking.
Act draws on project management.
Review draws on evaluation and adaptive management.
Inquiry and iteration can occur across the stages.
The same skill supports human-retained and delegated choices.
It declares a working mode: `Plan` stops at ratified decisions and registered grants, `Run` executes granted units and returns their results, and `Review` judges a return or a finished plan and stops at a verdict.
It requires an inspectable decision basis while allowing any suitable analytical method.
The new `perspicuity-work/1` record convention remains distinct from historical `spec: 0.2` records.
Existing Decide and Decide Agent names retain their historical meanings.

**Principal**:
The person or organization that supplies the objectives and authority for a delegation.

**Decider**:
The person or agent with authority to select an alternative for the decision in scope.

## Objectives and their basis

**Objective**:
A desired outcome against which alternatives are assessed.

**Standing objective**:
An objective that a principal wants considered across decisions within a stated scope.
A values document identifies these objectives and their source of authority.
Standing objectives do not supply weights, constraints or execution permission unless their source establishes them.

**Fundamental objective**:
An objective valued as an end within the decision's scope.

**Means objective**:
An objective pursued because it contributes to another objective within the decision's scope.

**Performance measure**:
A defined way to assess an alternative's consequence for an objective.
Its preferred direction describes which measured outcomes the decider prefers.

**Constraint**:
A binding limit with an identified owner or governing source that restricts feasible alternatives.

**Evidence**:
An observation or artifact that exists independently of the current decision and can be inspected.

**Assumption**:
A claim treated as true without verification, with its status and basis made explicit.

**Given**:
An established fact or imposed condition used for a decision, with its source, scope and date made explicit.

**Uncertainty**:
A relevant fact or outcome that is not known, with its plausible possibilities and implications made explicit where useful.

**Judgment**:
An estimate or assessment supplied by a person or agent where the available evidence does not determine it.

## Alternatives and strategies

**Alternative**:
A complete course of action within the decision's scope that can be compared with other courses of action.
_Avoid_: Component option when referring to a complete course of action.

**Direct alternative**:
An alternative specified as a whole for comparison.

**Component decision**:
One part of a broader decision for which a strategy selects a component option.

**Component option**:
A possible answer to one component decision.
_Avoid_: Alternative when the option does not specify a complete course of action in the current scope.

**Strategy**:
A coherent combination of component options that forms a complete alternative.

**Assembled strategy**:
A strategy constructed by selecting compatible options across component decisions.

**Strategy table**:
A table of component decisions and their available options, used to construct strategies.
Each column represents a component decision; each completed strategy identifies its selected options.

**Status quo**:
The existing course of action used as the baseline, including its continuing costs and commitments.

**Consequence**:
An observed or estimated outcome of an alternative against an objective under specified conditions.

**Rubric distribution**:
A model's probabilities over defined descriptive levels for a consequence judgment.
It describes the model's assessment of the supplied evidence.
It is not a validated distribution of future outcomes without relevant calibration evidence.

**Tradeoff**:
A sacrifice on one objective accepted for a gain on another under the decider's preferences.

## Records and reuse

**Initiative**:
An outcome-directed collection of linked decisions, work and evidence across initiation, ratification, implementation and monitoring.
_Avoid_: Plan when naming this Perspicuity concept.

**Decision record**:
An account of a decision and its basis, including objectives, alternatives, consequences, choice, and conditions for reconsideration.

**Plan**:
An account of the units that must happen in an order, the relation that orders them, and the repositories they span, under `perspicuity-plan/1`.
A plan carries the frame its units share and points at each unit's record; it decides nothing itself and restates no unit's state.
It is the only place sequence is recorded: a work unit's eligibility is read from the plan's relations together with the records' own states.
A plan may span repositories and may describe moving content between them.
_Distinguish_: a single intention's work stays in its own record; the shared frame and the ordering across units belong here.

**Working mode**:
The declared purpose of the current work: `Plan` establishes and ratifies choices and registers the work they authorize; `Run` executes granted units and returns their results; `Review` judges work already done and records a verdict, either on one return another actor sent or on a whole plan at its close-out.
The mode sets the stopping condition, not the depth of analysis or the authority.
A planning request stops at its boundary even when permission to act already exists.
The mode is recorded in the active record's Current position.
The mode name `Plan` does not name an Initiative and is not a Work Plan interval; read those terms by their own entries.
A mode and a format are distinct: the mode is a session's purpose, the format is an artifact's header contract.
`Review` adds no format; a review of a return is a record that points at what it received, and a plan's close-out is part of the plan.
The `Review` mode is the Review stage carried out by a receiver or across a plan.
Records before skill 0.6.0 may declare `Accept`, which reads as `Review` of a return.

**Done when**:
The registered criterion that shows a unit of work is complete.
It is internal to the work and checkable by its author.
Done is not shipped: a thing can be done and verified without having reached anywhere.

**Ship to**:
The registered destination the work must reach, and whoever can verify that it arrived.
It is external to the work and cannot be checked by its author.
Evidence for a shipping claim comes from outside the author's environment; a commit message, a changelog or the author's own tests cannot establish it.
Where the destination is another actor, that actor's acceptance is the evidence, and until it exists the record names that actor as its outstanding dependency.

**Acceptance**:
A verdict by a receiving actor that work arrived and is acceptable, recorded in the receiver's own record.
It settles two claims separately: arrival, whether the work is present, complete and readable; and acceptance, whether it meets the criteria its giver registered, is internally consistent and complete, and is coherent with the project's direction.
It is held in `Review` mode, and its verdict is accepted, accepted with conditions, or sent back.
A sibling unit or session may accept another's work; that is the ordinary case.
A receiver that produced the artifact, or that stands to gain from accepting it, has established arrival rather than acceptance, and says so.
An acceptance does not substitute for the principal's ratification, which changes what may be done rather than where the work is.

**Ratified decision**:
A selection saved with its comparison, reason, decider and basis revision.
Ratification establishes what was chosen and why.
It permits no work by itself: a work unit becomes executable only when a grant names the actor and the included work.

**Pickup plan**:
The plan registered for one granted unit at the time that unit is taken up.
It states how the unit will be carried out, how that route serves the grant's intent, and what will show it is done.
The first unit's pickup plan is registered at planning time; each later one waits for its own pickup because the earlier units change what is known.
Adapting its route stays with the actor; a changed problem, comparison or selection escalates to the decider.

**Escalation**:
A granted unit's referral to the decider when the work changes the problem, the comparison or the selection, when a tolerance is exceeded, or when an excluded target is needed.
The boundary is keyed to what changed, not to the actor's confidence, because an unstated boundary produces drift and one keyed to confidence escalates everything.
Escalation changes no authority by itself; the unit waits inside its existing grant until the decider responds.

**Tolerance**:
A limit on a granted unit's wall time, attempts or spend, set by the grantor.
Exceeding it stops the unit and escalates it; it is a stop rule, not a budget the actor must use.

**Claim**:
An actor's registered hold on a unit at pickup, with `Claimed by:` and `since:`.
Without a time tolerance on the grant, only the grantor or the actor running the plan may take over a claim.
One actor writes a record at a time; a claim older than the grant's time tolerance, with no return, may be taken over after checking the earlier attempt's uncertain effects.

**Unit state**:
A work unit's position: planned, ratified, granted, active, submitted or accepted, with waiting and stopped as side states.
The words reuse `work_status` values where both exist; records before skill 0.6.0 may use `picked up` for active and `returned` for submitted.

**Short-form choice**:
A reversible choice inside a grant, recorded in three lines: what was chosen over what, for which question and why; `Decided by:`; and `Reconsider if:`.
A choice that is hard to reverse, commits the principal externally or would change a grant takes the full basis.

**Plan close-out**:
The `Review` of a whole plan: what was supposed to happen, what happened, why they differ and what changes, with the delegation measures computed from the unit records and one verdict, close, correct or reconsider.

**Commit trailer**:
The `Perspicuity-Record:` and `Perspicuity-Unit:` lines on a commit made under a grant, which let `git log` list what was built for a unit and when.

**Objective record**:
A detailed definition of an objective, including its meaning, possible assessment, contextual relationships, and source of agreement.

**Decision template**:
Reusable criteria and guidance for a recurring class of decisions, with current inputs supplied by each case.
_Avoid_: Decision record when referring to reusable criteria rather than an individual case.

**Decision corpus**:
A collection of decision records and associated definitions, evidence, assumptions, and review material.

**Decision tree**:
A representation of choices, uncertain events, and resulting outcomes.
_Avoid_: Objective hierarchy when referring to branching choices and events.

**Objective hierarchy**:
A representation of broader objectives and their narrower constituent objectives.
Contributions between objectives can require additional links rather than a single parent.

## Linked lifecycle evidence

**Decision chain**:
The linked account of an intention, authority, consequential choices, delegated work, evidence and review.
Agent delegation sits at its centre.
The chain supports governance and assessment of trust by connecting recorded claims to actual actions and outcomes.
Existing signed chains retain their own formats and historical evidence.

These terms describe linked evidence rather than decision statuses or automatic authority.
They describe linked evidence, not additional decision statuses or automatic authority.

**Grant**:
A source instruction that authorizes a named actor's operation on a target within stated limits.
Selection authority applies only when the source supplies it.
Within the Perspicuity skill, a grant is registered for one work unit as a grant card: the actor, the objectives it serves, its intent, done when, ship to, the work included and excluded, tolerances, escalation triggers, return destination, acceptor and grantor.
Done when, tolerances and escalation triggers together are its stop condition.
For a batch, the principal ratifies the grants they own in one act, at the end of `Plan`.
It is the one permission another actor may rely on without reading the whole parent account.
It supplies no authority to choose between the alternatives of the decision it implements, to make a hard-to-reverse choice, to change scope or to act outside the named work, and it is not a general permission for the intention.
Under the default allocation, its worker makes reversible choices inside its includes.
This skill use is distinct from a host authorization record, which carries its own terms.

**Task**:
A bounded unit of work with an existing identity, deliverable, actual actor, targets, prerequisites and original acceptance conditions.
Its evidence links the selected basis and applicable grant.
The current project instructions designate the source of task state.
_Avoid_: Decision status when describing task state.

**Attempt**:
An actual performance of an operation, with its performer, target, executed basis, result, observed time and exact outputs.
Attempts include failures and unknown effects.

**Artifact**:
An identifiable output or source with exact content, revision, locator and producer when known.
A locator supplies location rather than identity.

**Assessment**:
An inspection of exact evidence against original criteria, with an actual assessor, verdict and gaps.
Preserve applicable independence requirements.
A task assessment and a commitment assessment address different conditions.

**Commitment**:
An undertaking with parties, terms and establishment evidence.
Assess fulfilment against matching performance evidence.

**Outcome**:
A dated finding from evidence against an objective or falsifier.
Task acceptance alone establishes neither an outcome nor commitment fulfilment.
A desired outcome expresses the intended effect before such evidence exists.

The Initiative and Objective record definitions remain distinct from machine record kinds.
The current Initiative uses an ordinary root decision, Plan and benefit account.
An Objective record supplies an objective's detailed definition.
Neither term adds a new v0.2 frontmatter type.
Preserve original identities, parent relations, reference bases, authority and history when linking these records.
Broader type adoption and project-to-corpus ownership remain unresolved.

## Shared record foundations

These distinctions connect to the existing representations.
They add no universal fields or machine kinds.

**Object kind**:
The meaning of a represented thing, separate from its subject domain, storage location and current state.

**Corpus-qualified identity**:
The source corpus and its local identifier, interpreted under that source's identity rules.
Equal local identifiers in different corpora do not establish one object.

**Revision basis**:
The exact source version that supports a reference or judgment, separate from the object's current version.

**Participation**:
An object's involvement in a relationship, decision or work view.
Participation does not transfer ownership, establish a dependency or supply an execution grant.

**Retention disposition**:
A decision about preserving or removing material, with its applicable authority and evidence obligations.
Temporary use does not itself authorize deletion.

**Work Plan**:
An addressable view of intended results and proposed work arrangements for an interval.
Its references preserve existing identities and task authority across views.

## Current work tracking

These terms describe the current work-tracking convention.

**Record status**:
Whether the evolving record has an unresolved choice, delivery or promised review.
An accepted delivery can remain in an open record.

**Work status**:
The observed state of the delivery named in the record's Work scope.
It supplies neither execution permission nor evidence that an agent is currently running.

**Next check**:
The earliest date when an actor must inspect the record again.
It can precede the end of an outcome's observation window.
The record retains each review's criteria, evidence, owner and timing.
