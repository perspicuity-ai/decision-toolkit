# Changelog for 0.5.0-preview.13

Source revision: `8ccc2537ffc35d7c0f8b99ba6bf7c6b5642525ba`.
Comparison distribution: `0.4.2`.
Record format: `perspicuity-work/1` → `perspicuity-work/1`.

## Changes in this candidate

- Distribution `0.4.2` → `0.5.0` (breaking). Carry skill 0.5.0, which declares a working mode and makes a work unit executable only through a registered grant. The unit ladder and the grant boundary change how authorized work is recorded, so the distribution declares a breaking component change. The dashboard, its launcher and its Python requirements remain outside this package.
- glossary: `0.1.3` → `0.1.4` (patch). Record the working mode, ratified decision, pickup plan and escalation terms, and distinguish the unit grant from a host authorization record.
- skill:perspicuity: `0.2.0` → `0.5.0` (breaking). Declare a working mode, so a planning session stops at ratified decisions and registered grants while a run executes granted units and returns their results. Add the unit ladder, the grant with its includes, excludes and stop condition, pickup registration with its escalation boundary, and a disclosure threshold. Revise the terminology and bring the record template to the same revision. The dashboard is out of this package's scope. The package also carries the Jev comparison tool, which the guide links to and which needs no added dependency.

1 components retain their versions and files.

## Recorded version history

This history contains recorded entries only. Initial entries mark the start of version tracking.
Component entries do not establish which earlier distribution included each change.

### distribution

- `0.5.0` (breaking). Carry skill 0.5.0, which declares a working mode and makes a work unit executable only through a registered grant. The unit ladder and the grant boundary change how authorized work is recorded, so the distribution declares a breaking component change. The dashboard, its launcher and its Python requirements remain outside this package.
- `0.4.2` (patch). Add the preview download destination and distinguish the three release assets. Document local Codex installation, Linux verification and complete-folder installation for other compatible hosts. Keep skill 0.2.0 unchanged.
- `0.4.1` (patch). Clarify preview installation, attribution and evidence limits in package documentation. Remove internal publication workflow from user-facing descriptions. Keep skill 0.2.0 and its five authored files unchanged.
- `0.4.0` (breaking). Replace mandatory analysis methods and ordinal tables with required record criteria. Let the agent choose suitable methods, scores, weights, and presentation for the case.
- `0.3.1` (patch). Correct consequence scoring after the browser trial. Keep each score on its own objective and reserve compensation across objectives for tradeoffs.
- `0.3.0` (breaking). Replace the packaged skill chain and legacy record format with one standalone Perspicuity skill and one evolving Markdown work record. Preserve earlier candidates separately. Correct the browser upload layout by placing its build manifest inside the sole perspicuity directory.
- `0.2.5` (patch). Replace stale adapted-material permission holds with approval reported by David. Preserve attribution, unchanged LICENSE terms and separate public-release authority; original-prompt and third-party rights are not expanded.
- `0.2.4` (patch). Align README and installation instructions with the included ten procedures, lifecycle resources and manually resumed file workflow. No code or capability change.
- `0.2.3` (feature). Prepare an actual file-based workstream and conditional packaged entry for trial. Human initiation, authority and publication limits remain.
- `0.2.2` (patch). Include assessed consequence direction and record extraction corrections. Preserve provisional scope and publication hold.
- `0.2.1` (patch). Reject renamed private origins in the provisional profile and include its loader in the packaging digest. The comparison candidate was successfully built but returned by source-boundary review.
- `0.2.0` (breaking). Provisional B public profile excludes earlier search/summary and withdrawn weighted-rating components, adds portable lifecycle demonstration, and reconciles release lineage. This is not D5 selection or publication.
- `0.1.5` (feature). Add decision search and summary, adapt completion preservation, and prepare a curated public candidate with portable documentation and explicit sharing scope.
- `0.1.4` (feature). Add the selected Apache 2.0 licence to every package. Preserve attribution and the publication hold pending permission for Laura's adapted material.
- `0.1.3` (feature). Add the core glossary and a generated package contents summary. Include the authorship notice in every format.
- `0.1.2` (patch). Include a readable changelog in each candidate and package. Show the baseline comparison and recorded version history.
- `0.1.1` (patch). Add explicit component versions, consistency checks, and changelog metadata to release packages. Record format and coaching behavior remain unchanged.

### decision-summary-runtime

- `0.1.0` (initial). Include the accepted implementation and its portable dependencies. Retain private verification records outside the distribution.
- Removal entry. Excluded from this provisional B profile; no permanent adoption or retirement.

### glossary

- `0.1.4` (patch). Record the working mode, ratified decision, pickup plan and escalation terms, and distinguish the unit grant from a host authorization record.
- `0.1.3` (patch). Clarify that record criteria define the required account while analysis methods and presentation depend on the case.
- `0.1.2` (feature). Define the single-skill workflow and evolving work record while preserving historical terminology.
- `0.1.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.0` (initial). Add the completed core terminology from CONTEXT.md. Start independent glossary version tracking.

### licensing

- `0.1.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.0` (initial). Track the Apache 2.0 licence and authorship notice as committed source files.

### lifecycle-demo

- `0.1.1` (patch). Route orientation to the included portable work procedures.
- `0.1.0` (initial). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### portable-workflow

- `0.1.0` (initial). Add receiving-file convention, benefit template, packet guidance and starting route.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/alternatives/strategy-table.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/consequences/decision-research.md

- `0.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/consequences/pugh-matrix.md

- `1.2.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/consequences/value-of-information.md

- `1.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/tradeoffs/dominance-and-pruning.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.1` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/tradeoffs/even-swaps.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/references/tradeoffs/weight-and-rate.md

- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Excluded from this provisional B profile; no permanent adoption or retirement.

### procedure:skills/decide/steps/01-frame.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/02-objectives.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/03-alternatives.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/04-consequences.md

- `1.3.1` (patch). Route unresolved ordinal magnitude to the shared directional bounds.
- `1.3.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.2.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/05-tradeoffs.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.1` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/06-recommendation.md

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/07-dq-assessment.md

- `2.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `2.0.1` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/decide/steps/08-record.md

- `2.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `2.0.3` (patch). Adapt the accepted completion-preservation guidance to the preceding release. Preserve baseline authority and validation behavior.
- `2.0.2` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/dq-check/instrument/elements.md

- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### procedure:skills/dq-check/instrument/scoring-rule.md

- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:decide

- `1.5.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.4.1` (patch). Adapt the accepted completion-preservation guidance to the preceding release. Preserve baseline authority and validation behavior.
- `1.4.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:decide-agent

- `0.5.2` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.5.1` (patch). Adapt the accepted completion-preservation guidance to the preceding release. Preserve baseline authority and validation behavior.
- `0.5.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:decision-research

- `0.1.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:decision-search

- `0.1.1` (initial). Include the accepted implementation and its portable dependencies. Retain private verification records outside the distribution.
- Removal entry. Excluded from this provisional B profile; no permanent adoption or retirement.

### skill:decision-summary

- `0.1.0` (initial). Include the accepted implementation and its portable dependencies. Retain private verification records outside the distribution.
- Removal entry. Excluded from this provisional B profile; no permanent adoption or retirement.

### skill:decision-template

- `0.2.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.2.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:dq-check

- `1.1.1` (patch). Extract table objectives and review conditions; distinguish compact consequence matrices from their evidence tables.
- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.1` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:frame

- `1.1.0` (feature). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `1.0.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:implement

- `0.1.0` (initial). Add assessed portable procedure under the explicit file-based convention; no background service.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:initiative

- `0.1.0` (initial). Add assessed portable procedure under the explicit file-based convention; no background service.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:perspicuity

- `0.5.0` (breaking). Declare a working mode, so a planning session stops at ratified decisions and registered grants while a run executes granted units and returns their results. Add the unit ladder, the grant with its includes, excludes and stop condition, pickup registration with its escalation boundary, and a disclosure threshold. Revise the terminology and bring the record template to the same revision. The dashboard is out of this package's scope. The package also carries the Jev comparison tool, which the guide links to and which needs no added dependency.
- `0.4.1` (patch). Make delivered work close and show what is blocking it. This local source revision preceded the packaged candidate.
- `0.4.0` (breaking). Build three-stage guidance with prospective records. This local source revision preceded the packaged candidate.
- `0.3.1` (patch). Restore explicit framing with delegated initiative. This local source revision preceded the packaged candidate.
- `0.3.0` (breaking). Simplify Perspicuity to the Frame and Decide, Act and Review responsibilities. This local source revision preceded the packaged candidate.
- `0.2.5` (patch). Bundle a local dashboard with project-specific work records, tasks, workers and connections. Display arbitrary frontmatter and sanitized Markdown record bodies with bundled browser scripts. Keep private records outside the package. Preserve separately committed local skill revisions 0.2.1 through 0.2.4.
- `0.2.4` (patch). Build decision chains during delegated work. This local source revision preceded the dashboard candidate.
  Local source revision: `10a110725311f53ee715e6488bc60ac6a5c410a1`.
- `0.2.3` (patch). Connect standing values to material decision consequences. This local source revision preceded the dashboard candidate.
  Local source revision: `70f4c4aad36a0af83c11d26ea1fcbbb3cc47c755`.
- `0.2.2` (patch). Include standing values in the decision process. This local source revision preceded the dashboard candidate.
  Local source revision: `4a8fe440e3caad112c424c46e74a704e17a4a70e`.
- `0.2.1` (patch). Track due reviews in work records. This local source revision preceded the dashboard candidate.
  Local source revision: `09eeebba4eff3de04c21281264510de27fc5546d`.
- `0.2.0` (breaking). Make PrOACT, ordinal scoring, consequence tables, and weights optional. Preserve required decision and work-record criteria while allowing the agent to choose how to satisfy them.
- `0.1.1` (patch). Require each consequence score to use its own objective scale. Mark missing magnitudes unknown and assess compensation across objectives only in tradeoffs. Update template and example version headers.
- `0.1.0` (initial). Introduce one entrypoint for a person or delegated agent through preparation, commitment, work, and review, with a template and fictional pipeline example.

### skill:pugh-matrix

- `0.1.2` (patch). Keep supported consequence direction visible without inventing a central ordinal score.
- `0.1.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### skill:review

- `0.1.2` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.1` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### specification

- `0.2.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.2.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.

### toolkit-tools

- `0.1.1` (patch). Aggregate assessed source and public adaptation changes in this provisional profile. Preserve private source versions through exact text-edit provenance.
- `0.1.0` (initial). Baseline adoption from preview.2; preserves existing source version where declared. Unversioned components start at 0.1.0.
- Removal entry. Exclude this legacy component from the standalone Perspicuity candidate. Earlier candidates and toolkit source retain it.
