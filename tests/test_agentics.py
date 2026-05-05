from langchain_core.language_models.fake_chat_models import FakeListChatModel

from agents.main import A2A_AGENT_FACTORIES
from agents.example_agent import create_example_agent
from tools.example import old_mcdonald_had_a_farm


def test_example_tool_returns_shared_value() -> None:
    assert old_mcdonald_had_a_farm() == "eyi eyi ohhhh"


def test_example_agent_builds_with_shared_tool() -> None:
    agent = create_example_agent(FakeListChatModel(responses=["ok"]))

    assert agent.name == "pythentic_example_agent"


def test_example_agent_is_registered_for_a2a() -> None:
    assert A2A_AGENT_FACTORIES["example"] is create_example_agent
