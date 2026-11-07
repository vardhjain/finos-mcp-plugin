"""Start the locked, public-PyPI AIGF MCP server over stdio."""

from finos_mcp.aigf.server import create_server
from directory_metadata import run

if __name__ == "__main__":
    run(create_server)
