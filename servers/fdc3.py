"""Start the locked, public-PyPI FDC3 MCP server over stdio."""

from finos_mcp.fdc3.server import create_server
from directory_metadata import run

if __name__ == "__main__":
    run(create_server)
