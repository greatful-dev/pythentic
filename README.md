# Pythentic

Pythentic is a FastAPI application that exposes the same agentic capabilities through multiple interfaces:

- Traditional HTTP API routes.
- MCP tools for external tool clients.
- A2A-facing agent registrations for agent-to-agent workflows.

## Directory Structure

```text
.
├── agents/        # LangGraph ReAct agents and A2A registration
├── models/        # LLM model references and model configuration
├── routes/        # Traditional FastAPI API interfaces
├── tools/         # Shared agent tool definitions and MCP configuration
├── main.py        # FastAPI app composition
├── dockerfile     # Production container build
└── dockerfile.dev # Development container build
```

## Components

### `agents/`

Contains distinct LangGraph ReAct agents. Each agent should compose shared tools from `tools/` rather than duplicating business logic or calling MCP internally.

`agents/main.py` is the registration point for A2A-facing agent interfaces. New agents should be added to the exported registry there.

### `models/`

Contains LLM model references, model definitions, and cost/configuration metadata used by agents.

### `routes/`

Contains traditional FastAPI routes. These endpoints are for direct HTTP API access and should stay thin, delegating reusable logic to `tools/` or agent orchestration to `agents/`.

### `tools/`

Contains canonical agent tool definitions. These are plain Python functions first, with protocol adapters layered on top.

`tools/main.py` owns the FastMCP server setup and registers shared tools for MCP exposure. Internal agents should import tools directly from this package instead of self-calling the MCP server.

## Development

Install dependencies:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

Run the development server:

```bash
./scripts/run_dev.sh
```
