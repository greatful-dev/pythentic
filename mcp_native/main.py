from fastmcp import FastMCP

mcp = FastMCP('pythentic')

@mcp.tool
def old_mcdonald_had_a_farm() -> str:
    return 'eyi eyi ohhhh'

mcp_app = mcp.http_app(path="/mcp")