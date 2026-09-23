---
format: perspicuity-work/1
id: example-client-pipeline
revision: 10
skill_version: 0.6.0
updated: 2026-10-16
record_status: open
work_status: accepted
next_check: 2026-10-23
---

# Build a usable client pipeline

Fictional teaching example. All scenario times, inputs, actions and observations are invented.
Times use America/Edmonton offsets. Source and snapshot labels denote no real files or Git versions.
No real work or model calls occurred. Prior revision notes remain as document history.

## Current position

Principal: Morgan, business owner. Decider: agent for the local pilot under Morgan's grant.

Mode: Review, because the pilot is delivered and its benefit reviews are open.

Decision: B at revision 2.

Work scope: Build a local pilot from ten supplied prospect records.

Done when: all ten records and their required fields remain, and Morgan finds each next action.

Ship to: Morgan's own copy of the tracker, verified by Morgan using it for her weekly review.

Work: local pilot T1 delivered and accepted by Morgan. Client benefit remains unknown.

Next: Morgan reviews unanswered approaches and responses on October 23, then O1 on November 26.

| Stage | began_at | registered_at / exact basis revision | finished_at |
| --- | --- | --- | --- |
| Frame and Decide | 2026-10-01T09:00:00-06:00 | 2026-10-01T09:10:00-06:00, F1 | 2026-10-01T10:00:00-06:00 |
| Act | 2026-10-01T10:00:00-06:00 | 2026-10-01T10:15:00-06:00, D2-plan | 2026-10-02T12:00:00-06:00 |
| Review, first check | 2026-10-16T09:00:00-06:00 | 2026-10-01T10:15:00-06:00, D2-plan | Unknown |

The retrospective review note lacks a finish time. Stage intervals include waits, not measured effort.

## Frame and Decide

Morgan's brief, S1, seeks two suitable new clients within eight weeks, less weekly administration and no additional software spending.

### Inputs and authority

Given: Morgan supplies S1, ten prospect records P1 and the administration estimate below.
S1 authorizes the agent to choose and build a local pilot with no spending and at most four hours of work.
Morgan retains live contact, service purchases and expansion.

| ID | Fundamental objective | Source / standing value | Measure, direction and horizon |
| --- | --- | --- | --- |
| O1 | Win suitable new clients | Morgan, S1 | Signed clients Morgan judges suitable; higher; eight weeks |
| O2 | Spend less time on administration | Morgan, S1 | Minutes of pipeline administration a week; lower; weekly |
| O3 | Add no software spending | Morgan, S1 | Additional software cost; lower; eight weeks |

Assumed: Morgan will use a weekly review, and visible next actions could reduce missed follow-ups.
Uncertain: prospects' responses, client yield and the pilot's effect on administration.
The agent frames the pilot around reliable follow-up within S1's objectives and limits.
Before alternative evaluation, F1 saves this frame, objectives, conditions and authority.

Alternative A continues scattered notes. B combines a local tracker, a visible next action and a weekly review.

### Consequences

Horizon: eight weeks. Estimates below are illustrative judgments, not measured results.

| Objective | A. Current notes | B. Tracker and review | Basis and limit |
| --- | --- | --- | --- |
| O1 suitable clients, higher preferred | Unknown | Unknown | No conversion evidence. Clear follow-up alone cannot establish client yield. |
| O2 administration, lower preferred | Estimated 60 minutes/week; range 45–90 | Forecast 40 minutes/week; range 20–100 | Morgan supplies A; agent supplies B. Overlap leaves improvement uncertain. |
| O3 software cost, lower preferred | $0 | $0 | Fixed by scenario and no-purchase authority. Setup time remains a separate cost. |

### Selection and review criteria

Morgan accepts up to four hours of setup to try reducing administration and missed follow-ups.

Chose B over A for how to track follow-up in the pilot, because it may lower O2 at no cost to O3 and the setup fits S1's four hours.
Decided by: agent, a reversible choice inside Morgan's grant S1.
Reconsider if: administration increases or next actions remain unclear.

`selected_at: 2026-10-01T10:00:00-06:00`. D2-choice saves F1, unchanged P1, the comparison and accepted setup cost at scenario revision 2.

Before execution, D2-plan saves the work plan below and delivery criteria: retain all ten records and required fields. Morgan can find each next action.
D2-plan registers Morgan's benefit reviews: time, omissions and replies on October 23, then suitable clients and their reasons on November 26.
No reminder was created.

## Act

| Result | Serves | Inputs / dependencies | Owner / accepted by / timing | Done when | Actual evidence |
| --- | --- | --- | --- | --- | --- |
| Build the tracker | B → O2 | [P1 under S1](#inputs-and-authority) | Agent / Morgan / October 2 | All ten identifiers and required fields remain | October 2: agent creates T1, `pipeline.csv`, then corrects an omitted next-action field. |
| Check and accept | B → O1, O2 | T1 and P1 | Agent checks T1 against P1; Morgan checks use / Morgan / October 2 | Checks pass. Morgan finds all ten next actions. | October 2: checks pass. Morgan completes the lookup and accepts T1 at Act's finish. |

```
Grant G1: build and check the local pilot
For: agent
Serves: B → O1, O2, O3
Intent: Morgan can see every prospect's next action in one place during her weekly review.
Done when: as Current position
Ship to: as Current position
Includes / Excludes: a local tracker built from P1 and its checks / live client contact, service purchases, spending and expansion
Tolerances: four hours of work and no spending, as S1 states them; exceeding one stops the unit and escalates it
Escalate if: the problem, comparison or selection changes; a tolerance is exceeded; an excluded target is needed
Return to: this record, with T1, the check results and the effort report
Accepted by: Morgan
Granted by: Morgan, S1, 2026-10-01T09:10:00-06:00, basis F1
```

Both results are delivered. The fictional effort report records three hours, inside G1's tolerance. A real record would link each input, output revision and check result.

## Review

October 16: Morgan reports 45 minutes of weekly administration, no missed planned follow-ups and no signed clients.
This does not establish causal improvement. Morgan keeps the pilot within its existing scope.

Verdict for T1: shipped. Morgan uses her own copy for the weekly review, which is evidence from outside the agent's environment.

| Criterion | Serves | Evidence source | Owner / window / trigger | Finding | Response |
| --- | --- | --- | --- | --- | --- |
| Does follow-up help without excessive effort? | O2 | Weekly time, omissions and replies | Morgan, October 23 | 45 minutes a week so far; no missed planned follow-ups | Inspect the next week's experience. |
| Did the work support two suitable clients? | O1 | Signed clients, Morgan's suitability judgment and their reasons over eight weeks | Morgan, November 26 | No clients yet | Keep the observation window open. |

Shipping T1 is not evidence of benefit; these reviews keep the record open.
The October 23 check precedes the eight-week outcome review.
If evidence challenges the assumptions about tracker use or client yield, revisit Frame and Decide.
Preserve F1, both D2 snapshots and the new evidence. The agent still lacks authority for spending or client contact.

## Changes

- Revision 1, October 1: Morgan supplies the objective and limits. Agent records alternatives and forecasts.
- Revision 2, October 1: agent selects B within the delegation.
- Revision 3, October 16: adds acceptance and first review. Client benefit remains unproven.
- Revision 4, October 16: distinguishes delivery state and review dates. No reminder exists.
- Revision 5, October 16: shortens the fictional example into Decide, Act and Review. Original forecasts and authority remain in Git.
- Revision 6, October 16: makes Frame explicit and illustrates broader analysis within the original delegation.
- Revision 7, October 16: removes routine Jev preparation while retaining the evidence and pilot basis.
- Revision 8, October 16: combines Frame and Decide, distinguishes inputs and adds fictional stage times, saved bases and a work plan with prior review criteria.
- Revision 10, October 16: brings the example to skill 0.6.0. It declares its mode, Done when and Ship to; gives the objectives identifiers, which renames the tracker from O1 to T1; records the selection in the short form with Decided by and Reconsider if; adds Serves and the acceptor to the Act table and the grant card G1; and gives T1 a shipping verdict. The scenario and its evidence are unchanged. Revision 9's note was not recorded.
