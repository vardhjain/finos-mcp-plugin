# Privacy policy

Effective date: November 6, 2026

## Scope and maintainer

This policy covers FINOS Reference Tools, the independent community plugin
maintained by Vardh Jain: https://github.com/vardhjain/finos-mcp-plugin.
It covers the plugin and its three local MCP servers, not your AI client,
GitHub, PyPI, or other third-party services.

## Data processed and purpose

The servers process the tool arguments explicitly sent by your AI client to
look up bundled public AIGF, CDM and FDC3 standards or validate supplied JSON.
Arguments can contain user-provided data. Use public or synthetic examples;
do not supply credentials or confidential trade or personal data.
The plugin does not independently access your conversation history, memory,
contacts, or uploaded files. Tool results return to the calling AI client.
The client may send arguments and results to its provider under its own policy.

## Local logs and retention

By default, the servers write request audit metadata to standard error: timestamps,
server and method/tool names, request/session identifiers, input sizes and SHA-256
hashes, outcome, timing and, when available, result sizes. Hashes are not a
guarantee of anonymization. Request statistics are also held in process memory.
The plugin does not send these logs to the maintainer or an analytics service.

The upstream runtime supports FINOS_MCP_AUDIT_PATH to append logs to a local file
and FINOS_MCP_AUDIT_RAW_ARGS=1 to include raw arguments. These are operator
settings, not enabled by the plugin manifests. Leave raw-argument logging off.
The plugin has no automatic log expiry. Your client controls capture and retention
of standard error. Operators control any configured audit files; delete those
files and client logs using their respective controls when no longer needed.
In-memory request data and statistics end when the server process exits.

## Network and third parties

Startup uses uv to obtain locked Python dependencies from PyPI and its package
hosting infrastructure. If Python 3.12 is unavailable, uv may also download a
managed Python runtime. Download services receive ordinary network request
metadata, such as your IP address. Package caches remain on your machine until
you remove them using uv's cache controls. Normal standards lookups and JSON
validation use local bundled content and require no FINOS hosted API or account.
Opening documentation or support links contacts those sites separately.

See [Claude's privacy policy](https://www.anthropic.com/legal/privacy),
[GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement),
and [PyPI's privacy notice](https://policies.python.org/pypi.org/Privacy-Notice/).
Other AI clients have their own policies.

## Support information and your choices

The maintainer receives no tool arguments or audit logs automatically. If you
open a public GitHub issue, the information you submit becomes public and is
stored by GitHub. Share only a minimal, sanitized reproduction. GitHub controls
retention of issue content; contact the maintainer through the repository for
help with information you submitted there. Uninstall the plugin to stop future
plugin use; uninstalling does not erase client logs, audit files or package caches.

For privacy and product questions, use
[GitHub Issues](https://github.com/vardhjain/finos-mcp-plugin/issues).
For security concerns, follow [SECURITY.md](SECURITY.md). Do not post secrets or
vulnerability details in a public issue. Policy changes are recorded in repository
history with an updated effective date.
