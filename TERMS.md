# Terms of use

Effective date: October 29, 2026

## Project and scope

FINOS Reference Tools is an independent, community-maintained open-source plugin
maintained by Vardh Jain. It provides local, read-only reference tools and guided
skills for AIGF, CDM, and FDC3. It is not affiliated with or endorsed by FINOS,
the Linux Foundation, or Anthropic. Product and organization names identify the
standards and clients supported; they do not imply sponsorship.

## Open-source license

The plugin code is distributed under the [Apache License, Version 2.0](LICENSE).
That license governs rights to use, copy, modify, and distribute the code, and
its warranty disclaimer and limitation of liability apply as written. This page
describes the project and does not replace or restrict rights granted by that
license. Bundled standards content and third-party dependencies remain subject
to their respective licenses and notices.

## Reference information

Tool output and generated explanations are reference information, not legal,
regulatory, investment, or other professional advice. Bundled standards reflect
specific upstream versions and may be incomplete or out of date. Check citations
and authoritative standards before relying on an answer. The plugin does not
certify regulatory compliance, validate business suitability, or approve trades.

## Local execution and data

The MCP servers run on your computer through Claude Code or Cowork; separately
configured local MCP servers can also be used in Claude Desktop. This plugin
provides no hosted endpoint. Initial installation downloads dependencies from
PyPI; ordinary reference lookups use locally bundled content. Servers process
tool arguments locally and emit audit metadata to stderr. Your AI client may
send conversation and tool data to its provider and may retain local logs under
its own settings and terms. Do not include credentials in tool arguments.

See the [Privacy policy](PRIVACY.md) for data handling, retention and operator logging settings.

## Availability and third-party services

The project offers no uptime guarantee, service-level agreement, or commitment
to continued maintenance or support. Claude, GitHub, PyPI, and other third-party
services are governed by their own terms and may have separate charges or
requirements. No FINOS API key or maintainer-hosted service subscription is
required by this plugin.

## Contact and updates

Report problems or ask questions through
[GitHub Issues](https://github.com/vardhjain/finos-mcp-plugin/issues).
Do not post secrets or private data in public issues. Changes to this page are
recorded in the repository history with an updated effective date; changes do
not revoke rights already granted under the applicable open-source license.
