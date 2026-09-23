# Perspicuity

Perspicuity is one skill for carrying an intention through a decision, authorized work and outcome review.
It supports a person who retains the choice or an agent with delegated authority.
One evolving Markdown record keeps the reasons connected to the work and its results.

The skill asks the agent to make its decision basis inspectable.
The agent can choose a suitable analytical method.
The work moves through Frame and Decide, Act and Review, stages that can repeat as the work develops.
Each session works in one mode, Plan, Run or Review, and stops at that mode's boundary.
You can add specialist skills when the work needs them.

## Download

[Download a preview from GitHub Releases](https://github.com/perspicuity-ai/decision-toolkit/releases).
Open the preview release and choose an asset by its filename ending.

| Asset | Use |
| --- | --- |
| `-developer.zip` | Local skill files and the Python installer, including local Codex setup. |
| `-skill.zip` | Upload through a host's custom skill interface. |
| `-plugin.zip` | Install with a host that accepts `.codex-plugin/plugin.json` packages. |

## Try it

For Codex on Linux, use the developer ZIP and follow [INSTALL.md](INSTALL.md).
The installer was checked on Linux.
INSTALL.md also explains complete-folder installation for other compatible hosts.
Then give the agent an intention, your constraints and its authority.
For example, you could start with this request.

> Use Perspicuity to help me plan a community event within a budget of $500.
> I will make the final choice.
> Keep one record that I can save and bring to our next session.

For delegated work, specify which choices the agent can make and what actions it may take.
Supply the saved record when you resume in a new session.
Keep linked outputs accessible when the agent needs them for review.

The skill supplies guidance, a record template and an optional local dashboard.
Ask your agent to start the Perspicuity dashboard for the current project.
The dashboard shows that project's work records, tasks, workers and connections.
It reads local records without model calls.
Task and worker visibility requires supported host metadata, currently the local Codex adapter.
Read [the dashboard guide](skills/perspicuity/references/dashboard.md) for requirements and commands.

Execution and follow-up depend on the host's tools and your authorization.
The package includes no scheduler or hosted service.

## Early preview

Package checks verify the selected files, local links, isolated developer installation and repeatable archive bytes.
Behavioral evidence remains limited.
Improved decision quality and effort savings remain unmeasured.
The [contents summary](PACKAGE-CONTENTS.md) distinguishes package checks from earlier installation observations and checks not run for this package.

The bundled pipeline example is fictional.
It illustrates the record and does not demonstrate client acquisition or other benefits.

Read [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for licence terms and attribution.
Read [CHANGELOG.md](CHANGELOG.md) for version changes.
