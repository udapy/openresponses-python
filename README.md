# OpenResponses Python
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un-Official Python SDK for the **Open Responses** standard. This library provides Pydantic models, a client SDK, and utilities to build compliant servers/providers.

## Features

- **Standardized Data Models**: Strict Pydantic V2 definitions for `InputText`, `MessageItem`, `ReasoningItem`, `ToolCallItem`, etc.
- **Client SDK**: Sync and Async clients (`OpenResponsesClient`) with streaming support.
- **Provider Utilities**: Helpers to map OpenAI-compatible requests and generate SSE events for semantic streaming.
- **Agentic Support**: First-class support for reasoning, tool calls, and structured inputs.

## Installation

```bash
pip install openresponses-python
```

For development, we rely on [uv](https://github.com/astral-sh/uv) for dependency management and reproducibility.

```bash
git clone https://github.com/uday/openresponses-python.git
cd openresponses-python
make install  # Runs: uv sync
```

## Quick Start (Client)

```python
import asyncio
from openresponses.client import AsyncOpenResponsesClient

async def main():
    # Connect to a compliant provider (e.g., local proxy or native)
    client = AsyncOpenResponsesClient(base_url="http://localhost:8000")

    # Semantic Streaming Request
    stream = await client.create(
        model="deepseek/deepseek-r1",
        input="Explain quantum entanglement.",
        stream=True
    )

    async for event in stream:
        if event.event == "response.reasoning.delta":
             print(f"🧠 {event.data['delta']}", end="", flush=True)
        elif event.event == "response.text.delta":
             print(f"🤖 {event.data['delta']}", end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
```

## Examples

This repository contains proxy examples for various backends.

1.  **OpenRouter**: `make run-openrouter` (Port 8001)
2.  **OpenAI**: `make run-openai` (Port 8002)
3.  **Ollama**: `make run-ollama` (Port 8003)
4.  **LM Studio**: `make run-lmstudio` (Port 8004)
5.  **HuggingFace**: `make run-huggingface` (Port 8005)

## Development

Use the included `Makefile` (powered by `uv`) for common tasks:

```bash
make install   # Sync dependencies
make lint      # Run linters
make test      # Run tests
```

## License

MIT
