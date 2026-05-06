# AGENTS.md

## Commands
- **Install dependencies**: `uv sync`
- **Run development server**: `./scripts/run_dev.sh` (uses Podman)
- **Run tests**: `uv run pytest`
- **Run single test**: `uv run pytest path/to/test_file.py::test_function_name`
- **Build container**: `podman build -f dockerfile.dev -t pythentic .`
- **Lint**: `run black`
- **Format**: `run black`

## Code Style Guidelines
- **Python version**: >=3.10,<4.0
- **Imports**: Standard library first, then third-party, then local imports
- **Types**: Use type hints for function parameters and return values
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error handling**: Use try/except blocks, raise appropriate exceptions
- **Async**: Use async/await for FastAPI endpoints and MCP tools
- **Dependencies**: Use uv for dependency management, pin versions with ranges
- **Structure**: Keep business logic in agentics/ directory, main app in root