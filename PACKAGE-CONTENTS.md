# Package contents for 0.4.2-preview.1

This early preview contains one user-facing skill, `perspicuity`.
It supports a person or a delegated agent through Understand, Choose, Act and Review.
One evolving Markdown record carries the context between sessions.
Selected source revision: `e43a065e66b8773f9753685f847e1dcab9133fcf`.

## Skill and record

- Skill version: `0.2.0`.
- Record format: `perspicuity-work/1`.
- The format is documented Markdown. No JSON schema or database is required.
- The entrypoint links to analysis guidance, record guidance, a template, and a fictional example.
- The package requires no earlier Perspicuity skill, runtime, graph, or chain tool.

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
The earlier 0.4.0-preview.1 skill ZIP passed a Claude browser installation check on September 15, 2026.
That observation applies to the earlier archive, which contains the same five authored skill files as this package.
Browser installation and behavioral scenarios were not rerun for this documentation update.
Coaching, record download and reopening remain unverified for this package.
The pipeline example is fictional. It does not establish client acquisition or other observed benefits.
Apache License 2.0 applies under LICENSE and NOTICE.md.
The package supplies no hosted service or background execution.

## Component inventory

| Component | Version |
| --- | --- |
| glossary | 0.1.3 |
| licensing | 0.1.1 |
| skill:perspicuity | 0.2.0 |
