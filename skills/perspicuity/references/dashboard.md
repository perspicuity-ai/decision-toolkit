# Start a project's Operations dashboard

Use the bundled runner for local work inspection.
The dashboard retains the Work records, Tasks & workers, and Connections views.
It reads saved evidence without model calls.

## Start

1. Select the project root that contains the user's work.
2. Locate `scripts/dashboard.py` inside this skill's directory.
3. Use Python 3.10 or later.
4. If PyYAML is absent, install `scripts/requirements.txt` with that Python interpreter.
5. Run the following command with the actual script and project paths.

```sh
python /path/to/perspicuity/scripts/dashboard.py start --root /path/to/project
```

The launcher opens a browser at the project's address.
Use `--no-open` when the agent will open the returned address through its browser tool.
If `--root` is absent, the launcher uses the current directory.
Use the project root instead of the installed skill directory.

Each project receives a separate process and available port.
A repeated start returns the same address while that project's process remains available.
The page shows the project path.
The process continues after the command ends.
After a computer restart, run the start command again.

## Inspect the sources

Save work records as Markdown with the `perspicuity-work/1` header from the skill template.
Use the project's existing record locations.
The reader searches within the selected project.
It excludes nested Git projects, installed skills, dependencies, caches, historical copies, examples and symbolic links.
Read Sources & coverage for the observed scope and source issues.
Select a record to inspect every front-matter field and the complete rendered Markdown body.
Use Markdown source to inspect the original text.
If the source fails, use Retry record after checking the local file.
The body can use any headings or structure appropriate to the work.
The current work status describes delivery state; this dashboard adds no stage convention.

Tasks & workers reads local Codex metadata for the exact project directory.
The adapter uses `CODEX_HOME` or the user's `.codex` directory.
Use `--codex-home` at startup to select another Codex directory.
Stop the project dashboard before changing its port or Codex directory.
Top-level tasks remain visible while unarchived.
Workers remain visible for 24 hours after their latest saved update.
Parent relationships use explicit saved identifiers.
Saved events do not establish current execution or acceptance.

Other agent hosts need their own task adapter.
If Codex metadata is absent or incompatible, the page reports that limitation.
If safe session access is unsupported, task metadata remains visible with unknown turn state.
Work records and their connections remain available in both cases.

Connections follow direct inline Markdown links between current records.
Only a link in the current Dependency field receives a dependency label.
The task view separately shows saved worker parent relationships.
The dashboard infers no relationship from matching titles.

## Control the process

Use the same project path for each command.

```sh
python /path/to/perspicuity/scripts/dashboard.py status --root /path/to/project
python /path/to/perspicuity/scripts/dashboard.py stop --root /path/to/project
```

Use `serve` instead of `start` for a foreground process.
Use `--port` to request a specific available port.
The default selects an available port automatically.
Startup failures identify the local log path.
The launcher stores process details in the user's cache directory, outside the project and skill.

The server binds to `127.0.0.1`.
The viewer reads files without changing records or dispatching agents.
Finance and Experiments remain outside this package.
Python and PyYAML are runtime requirements, separate from the skill files.

## Renderer dependencies

The package includes Marked 18.0.13 and DOMPurify 3.4.15 with their licence files.
The files come from the corresponding npm release archives, verified against registry SHA-512 integrity values.
The browser loads these files locally.
The renderer permits document formatting and safe links.
It omits active HTML and embedded media.
Code fences remain code, including Mermaid source.
See [Marked](https://marked.js.org/) and [DOMPurify](https://github.com/cure53/DOMPurify) for their maintained documentation.
