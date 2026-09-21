# Install Perspicuity

Choose the format that your agent host supports.
The host is the application that loads the skill and runs the agent.

## Download

[Download a preview from GitHub Releases](https://github.com/perspicuity-ai/decision-toolkit/releases).
Open the preview release and choose an asset by its filename ending.

| Asset | Use |
| --- | --- |
| `-developer.zip` | Local skill files and the Python installer, including the Codex route below. |
| `-skill.zip` | Upload through a host's custom skill interface. |
| `-plugin.zip` | Install with a host that accepts `.codex-plugin/plugin.json` packages. |

## Codex local installation

Use the developer ZIP for local Codex setup.
The installer was checked on Linux.
Scripted installation on other operating systems remains unverified.
The installer requires Python 3.
It verifies the package before copying the complete skill directory.
It stops if a Perspicuity installation already exists at the destination.

1. Extract the developer ZIP into a directory you control.
2. Open a terminal in the extracted directory that contains this file.
3. Run `python3 tools/install.py`.
4. Start a new Codex session.
5. Ask Codex to use Perspicuity.

The default destination is `~/.agents/skills/perspicuity`.
Codex reads this personal skill directory, as described in the [official skills documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
For a different directory, run `python3 tools/install.py --skills-dir DIRECTORY`.
Replace `DIRECTORY` with the host's skill directory.
The installer creates a `perspicuity` directory inside it.

If the installer reports an existing installation, retain that copy until you choose how to replace it.

## Local project dashboard

The complete skill includes the dashboard server, interface and launcher.
The dashboard requires Python 3.10 or later and PyYAML.
The interface requires no JavaScript build.

After installation, ask your agent to start the Perspicuity dashboard for your project.
The launcher uses that project's records and a separate local address.
Read [the dashboard guide](skills/perspicuity/references/dashboard.md) for setup and launcher commands.
Keep the skill's complete directory when you move or install it.

Task and worker visibility requires local Codex metadata.
Other hosts can display the project's work records and their connections.
Browser skill uploads require a host that can execute Python and expose a local server to use this optional dashboard.

## Manual installation for other hosts

If your host supports local skill directories, copy the complete `skills/perspicuity` directory from the developer ZIP.
Place it in the skill directory specified by your host.
Preserve every file and subdirectory.
The installed copy has no dependency on the extracted developer directory.

## Browser skill

If the host supports custom skill uploads, upload the skill ZIP through its skill interface.
The archive contains one `perspicuity` directory with `SKILL.md` and its supporting subdirectories.
Preserve the archive's directory structure.
Availability and upload controls depend on the host.

## Plugin

Use the plugin ZIP only with a host that supports `.codex-plugin/plugin.json` packages.
Follow that host's package installation instructions.
The archive contains the same skill under `skills/perspicuity` and the plugin manifest under `.codex-plugin`.
This format requires a compatible host.

## Verify and resume

After installation, ask the agent to use Perspicuity for a small decision.
Check that it can read the record guidance and save a record in your environment.
Package checks do not establish those host capabilities.
Read `PACKAGE-CONTENTS.md` for the tested scope and remaining limits.
That file accompanies the skill in every format.

Save the working record before you end the session.
Provide that record when you resume.
Keep linked outputs accessible when later assessment depends on them.
