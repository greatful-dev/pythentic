from langchain_core.tools import StructuredTool


def old_mcdonald_had_a_farm() -> str:
    """Return the example farm refrain."""
    return "eyi eyi ohhhh"


old_mcdonald_had_a_farm_tool = StructuredTool.from_function(
    old_mcdonald_had_a_farm,
    name="old_mcdonald_had_a_farm",
    description="Return the example Old McDonald farm refrain.",
)
