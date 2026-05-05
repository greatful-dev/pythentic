from fastmcp import FastMCP

from tools.example import old_mcdonald_had_a_farm


mcp = FastMCP("pythentic")
mcp.tool(old_mcdonald_had_a_farm)
mcp_app = mcp.http_app(path="/mcp")

__all__ = ["mcp", "mcp_app"]
