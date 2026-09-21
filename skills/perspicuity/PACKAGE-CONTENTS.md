# Package contents for 0.5.0-preview.13

This early preview contains one user-facing skill, `perspicuity`.
It supports a person or a delegated agent through Understand, Choose, Act and Review.
One evolving Markdown record carries the context between sessions.
Selected source revision: `8ccc2537ffc35d7c0f8b99ba6bf7c6b5642525ba`.

## Skill and record

- Skill version: `0.5.0`.
- Record format: `perspicuity-work/1`.
- The format is documented Markdown. No JSON schema or database is required.
- The entrypoint links to analysis guidance, record guidance, a template, and a fictional example.
- The optional dashboard shows the selected project's records, tasks, workers and connections.
- The dashboard requires Python 3.10 or later and PyYAML. Its interface requires no JavaScript build.
- Marked and DOMPurify render record bodies offline. Their licence files accompany the browser scripts.
- The Codex adapter reads local task metadata when available. Other hosts can use the record views.
- Each project retains its own records. The package contains no personal work records.

## Formats

| Format | Contents |
| --- | --- |
| Developer ZIP | `skills/perspicuity/`, release documents, and a local installer. |
| Skill ZIP | `perspicuity/SKILL.md` with its supporting files and subdirectories. |
| Plugin ZIP | `skills/perspicuity/` and `.codex-plugin/plugin.json`. |

Each skill directory includes the glossary, licence, authorship notice, component versions, and changelog.
The installer copies this complete directory without overwriting an existing installation.
Each archive includes a build manifest with exact file hashes.

## Evidence and limits

Package checks verify source membership, local references and repeatable archive bytes for all three formats.
An isolated installation check verifies the developer installer and complete copied resources.
These checks do not establish host compatibility, decision quality or effort savings.
Browser installation and behavioral scenarios require observations for this candidate.
Coaching, record download and reopening remain unverified for this package.
The pipeline example is fictional. It does not establish client acquisition or other observed benefits.
Apache License 2.0 applies under LICENSE and NOTICE.md.
The dashboard runs locally when started. The package supplies no hosted service or model runtime.

## Component inventory

| Component | Version |
| --- | --- |
| glossary | 0.1.4 |
| licensing | 0.1.1 |
| skill:perspicuity | 0.5.0 |
