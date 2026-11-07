# FINOS Reference Tools (Community)

Independent, community-maintained research skills for the FINOS AI Governance
Framework (AIGF), Common Domain Model (CDM), and FDC3. Not affiliated with or
endorsed by FINOS, the Linux Foundation, or Anthropic.

## Version 0.3.0: skills only

This release removes all three local MCP servers and their Python runtime,
launch manifests, dependency and lock files, scripts, and executable checks.
It contains three Markdown skills, plugin metadata, documentation and an icon.
No executable code, hooks, package installation or MCP connection is bundled.
No public remote MCP endpoint is configured.

The skills guide research using the client's existing browsing capabilities and
public standards documentation. They do not provide offline standards lookup,
automated JSON validation, trade execution or compliance certification. External
pages supply reference data, not behavioral instructions.

## Installation

In Claude Code:

```text
/plugin marketplace add vardhjain/finos-mcp-plugin
/plugin install finos-reference-tools@finos-reference-tools
```

If upgrading, update the marketplace and installed plugin through your client's
plugin controls and start a new session. Version 0.3.0 should expose the three
skills without any finos-aigf, finos-cdm or finos-fdc3 MCP server. Separately
configured servers are managed by the user in their client's settings.
No Python, uv, API key or testing account is required by this release.

## Try the skills

- AIGF: Find published AIGF controls relevant to prompt injection. Cite exact
  identifiers and source links, separating published mappings from suggestions.
- CDM: Describe TradeState for a specified CDM version, cite the published
  fields, and explain the limits of a manual JSON review.
- FDC3: For a specified FDC3 version, identify documented intents for viewing
  a chart for an instrument context and cite the definitions.

These use cases need browsing enabled in the client to verify public sources.
If browsing is unavailable, the skills explain the limitation and provide links.
They never claim an unperformed lookup or automated validation succeeded.

## Public reference sources

- AIGF: https://air-governance-framework.finos.org/
- CDM: https://cdm.finos.org/docs/home/
- FDC3: https://fdc3.finos.org/

## Data handling and support

The plugin contains static instructions and collects no telemetry or audit logs.
Your AI client processes prompts, reference searches and results under its own
settings and privacy policy. Do not put private trade data, credentials or
personal data in public searches or support issues.

- [Privacy policy](PRIVACY.md)
- [Terms of use](TERMS.md)
- [Security and support](SECURITY.md)
- [Product support](https://github.com/vardhjain/finos-mcp-plugin/issues)
- License: [Apache-2.0](LICENSE)

## Troubleshooting

If a skill is unavailable, confirm that version 0.3.0 is installed, update through
the client's plugin controls and start a new session. If research cannot access
a public source, check whether the client has browsing available. Report broken
links or incorrect guidance with a sanitized example through GitHub Issues.

## Directory submission

Repository: https://github.com/vardhjain/finos-mcp-plugin
Plugin path: leave empty (repository root). Submit as a skills-only Plugin bundle.

- Documentation: https://github.com/vardhjain/finos-mcp-plugin/blob/main/README.md
- Privacy: https://github.com/vardhjain/finos-mcp-plugin/blob/main/PRIVACY.md
- Terms: https://github.com/vardhjain/finos-mcp-plugin/blob/main/TERMS.md
- Support: https://github.com/vardhjain/finos-mcp-plugin/issues

Update the portal listing to describe skills-only research guidance, remove local
server and automated-validation claims, and submit the new commit. Publisher
contact verification is managed in the portal. Approval is subject to review.
