---
format: perspicuity-work/1
id: example-client-pipeline
revision: 9
skill_version: 0.5.0
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

Decision: B at revision 2.

Work scope: Build a local pilot from ten supplied prospect records.

Work: local pilot from ten records, accepted after checks. Client benefit remains unknown.

Next: Morgan reviews unanswered approaches and responses on October 23, then the client objective on November 26.

| Stage | began_at | registered_at and exact saved basis | finished_at |
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

Assumed: Morgan will use a weekly review, and visible next actions could reduce missed follow-ups.
Uncertain: prospects' responses, client yield and the pilot's effect on administration.
The agent frames the pilot around reliable follow-up within S1's objectives and limits.
Before alternative evaluation, F1 saves this frame, objectives, conditions and authority.

Alternative A continues scattered notes. B combines a local tracker, a visible next action and a weekly review.

### Consequences

Horizon: eight weeks. Estimates below are illustrative judgments, not measured results.

| Objective | A. Current notes | B. Tracker and review | Basis and limit |
| --- | --- | --- | --- |
| Suitable clients, higher preferred | Unknown | Unknown | No conversion evidence. Clear follow-up alone cannot establish client yield. |
| Administration, lower preferred | Estimated 60 minutes/week; range 45–90 | Forecast 40 minutes/week; range 20–100 | Morgan supplies A; agent supplies B. Overlap leaves improvement uncertain. |
| Additional software cost, lower preferred | $0 | $0 | Fixed by scenario and no-purchase authority. Setup time remains a separate cost. |

### Selection and review criteria

Morgan accepts up to four hours of setup to try reducing administration and missed follow-ups.
`selected_at: 2026-10-01T10:00:00-06:00`: agent selects B under S1.
At that time, D2-choice saves F1, unchanged P1, the comparison and accepted setup cost at scenario revision 2.

Before execution, D2-plan saves the work plan below and delivery criteria: retain all ten records and required fields. Morgan can find each next action.
D2-plan registers Morgan's benefit reviews: time, omissions and replies on October 23, then suitable clients and their reasons on November 26.
If administration increases or next actions remain unclear, reconsider B within the grant.
No reminder was created.

## Act

| [D2-plan](#selection-and-review-criteria), from D2-choice | Input and actor | Done when | Fictional execution evidence |
| --- | --- | --- | --- |
| Build the tracker | Agent uses [P1 under S1](#inputs-and-authority) | All ten identifiers and required fields remain | October 2: agent creates O1, `pipeline.csv`, then corrects an omitted next-action field. |
| Check and accept | Agent checks O1 against P1. Morgan checks use. | Checks pass. Morgan finds all ten next actions. | October 2: checks pass. Morgan completes the lookup and accepts O1 at Act's finish. |

The fictional effort report records three hours. A real record would link each input, output revision and check result.

## Review

October 16: Morgan reports 45 minutes of weekly administration, no missed planned follow-ups and no signed clients.
This does not establish causal improvement. Morgan keeps the pilot within its existing scope.

| Question | Evidence and window | Owner and due | Finding and response |
| --- | --- | --- | --- |
| Does follow-up help without excessive effort? | Weekly time, omissions and replies | Morgan, October 23 | Inspect the next week's experience. |
| Did the work support two suitable clients? | Signed clients, Morgan's suitability judgment and their reasons over eight weeks | Morgan, November 26 | No clients yet. Keep the observation window open. |

Delivery stays accepted while these reviews keep the record open.
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
