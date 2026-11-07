# FINOS Reference Tools (Community)

Independent, community-maintained reference tools for the FINOS AI Governance
Framework (AIGF), Common Domain Model (CDM), and FDC3. Not affiliated with or
endorsed by FINOS. Includes three guided skills and three read-only MCP servers.

## Requirements and installation

Install uv and Python 3.12 and make uv available on the client's PATH. In Claude Code:

```text
/plugin marketplace add vardhjain/finos-mcp-plugin
/plugin install finos-reference-tools@finos-reference-tools
```

Start a new session and check `/mcp`. Local servers work in Claude Code and
Cowork. They cannot run in claude.ai web chat. Claude Desktop chat can use
separately configured local MCP servers; see the repository's client setup guide.

The first launch downloads packages from public PyPI. The bundled pyproject.toml
and uv.lock pin the runtime and all transitive dependencies, including artifact
hashes. Launches use uv run --frozen from this standalone plugin directory.
There are no custom indexes, workspace source redirects, or registry overrides. Normal reference
lookups then work offline. No FINOS API key, database or hosted endpoint is needed.
All three servers share a runtime environment; their processes consume memory separately.

## Try the tools

- AIGF: use get_control with id mi-20 and return its citation URI.
- CDM: use describe_type for TradeState and return its schema URI.
- FDC3: use suggest_intent with an fdc3.instrument context and goal "show a chart".

## Data handling

Tools read bundled public standards. User tool arguments are processed locally;
there are no model calls or runtime requests to FINOS services. Startup package
downloads contact PyPI; uv may download Python if the required runtime is missing. Servers emit local audit metadata to stderr, including
method/tool names, argument sizes and hashes; client logging and retention are
controlled by the client. Do not supply credentials or private trade data in tests.

Privacy policy: [PRIVACY.md](PRIVACY.md). Includes audit settings, retention and third-party services.
Security reporting: [SECURITY.md](SECURITY.md).

Documentation: https://vardhjain.github.io/finos-mcp/
Support: https://github.com/vardhjain/finos-mcp-plugin/issues
License: Apache-2.0 (see LICENSE).

## Public directory submission

Repository: https://github.com/vardhjain/finos-mcp-plugin
Plugin path: leave empty (the plugin is at the repository root).
Branch: main. Submit as a Plugin bundle.
The directory still reviews fetched packages and may require human approval.

## Development and verification

Run `python checks/validate.py` for offline packaging checks.
Run `python checks/smoke.py` for six real stdio tool calls through both manifests.
Install uv first. The smoke test downloads the locked dependencies on first run.
Update dependencies with `uv lock`, review the diff and rerun both checks.

## Terms of use

See [Terms of use](TERMS.md). The code remains licensed under [Apache-2.0](LICENSE).

## Troubleshooting

If startup fails, confirm `uv --version` and `uv python find 3.12` work in the
same environment as your AI client, then check the client's MCP server errors.
The first dependency download needs network access. Run `uv sync --frozen` from
this repository to diagnose installation failures. Restart the client after
correcting PATH or installation issues. For an unknown identifier or invalid
JSON, use the returned error details and a published sample rather than retrying
unchanged input. Report persistent errors through the support link above.

## Directory reviewer setup

No testing account, credentials or private data are needed: all three servers
use bundled public standards. Install the requirements above and run the three
prompts under "Try the tools". Run `python checks/smoke.py` to verify both
manifests against the bundled examples. The tools provide standards reference
and structural validation; they do not execute trades, transfer assets, certify
compliance or provide personalized investment recommendations.

For the submission portal, use these public repository links:

- Privacy: https://github.com/vardhjain/finos-mcp-plugin/blob/main/PRIVACY.md
- Support: https://github.com/vardhjain/finos-mcp-plugin/issues
- Documentation: https://github.com/vardhjain/finos-mcp-plugin/blob/main/README.md
- Terms: https://github.com/vardhjain/finos-mcp-plugin/blob/main/TERMS.md

The publisher must complete contact verification in the portal. Repository
metadata does not establish verified publisher status. These policy changes
require a fresh submission; they do not change the rejected commit's verdict.
