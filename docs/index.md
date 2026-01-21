# Welcome to OpenResponses Python

The official Python SDK for the **Open Responses** standard.

`openresponses-python` provides typed Pydantic models, a flexible client SDK, and utilities for building compliant providers.

## Key Features

- **Strict Typing**: Standardized models for `MessageItem`, `ReasoningItem`, `ToolCallItem`, etc.
- **Async & Sync Support**: Built on `httpx` for high performance.
- **Semantic Streaming**: First-class support for streaming reasoning and text deltas.
- **Provider Agnostic**: Proxy examples for OpenRouter, OpenAI, HuggingFace, Ollama, and more.

## Installation

```bash
pip install openresponses-python
```

!!! tip "For Development"
We recommend using [uv](https://github.com/astral-sh/uv) for dependency management.

    ```bash
    make install
    ```

## Next Steps

- Check out the [Quickstart](quickstart.md) guid.
- Browse the [API Reference](api.md).
- See ready-to-use [Examples](examples.md).
