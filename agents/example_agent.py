from typing import Any
from langchain.agents import create_agent
from langchain_core.language_models.chat_models import BaseChatModel
from tools.example import old_mcdonald_had_a_farm_tool


def create_example_agent(model: str | BaseChatModel) -> Any:
    """Create an example LangGraph-backed agent using shared tool definitions."""
    return create_agent(
        model=model,
        tools=[old_mcdonald_had_a_farm_tool],
        system_prompt=(
            "You are Pythentic's example agent. Use the available tools when "
            "the user asks about Old McDonald or the example farm response."
        ),
        name="pythentic_example_agent",
    )
