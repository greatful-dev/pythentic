from agents.example_agent import create_example_agent


A2A_AGENT_FACTORIES = {
    "example": create_example_agent,
}

__all__ = ["A2A_AGENT_FACTORIES", "create_example_agent"]
