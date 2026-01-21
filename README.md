# OpenResponses Python

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/openresponses-python.svg?style=flat-square)](https://pypi.org/project/openresponses-python/)
[![Python Versions](https://img.shields.io/pypi/pyversions/openresponses-python.svg?style=flat-square)](https://pypi.org/project/openresponses-python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/uday/openresponses-python/test.yml?branch=main&style=flat-square&label=tests)](https://github.com/uday/openresponses-python/actions)
[![Docs](https://img.shields.io/github/deployments/uday/openresponses-python/github-pages?label=docs&style=flat-square)](https://uday.github.io/openresponses-python/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**Un-Official Python SDK for the Open Responses standard.**

[Documentation](https://udapy.github.io/openresponses-python/) | [Source Code](https://github.com/udapy/openresponses-python) | [Bug Tracker](https://github.com/udapy/openresponses-python/issues)

</div>

---

**OpenResponses Python** provides a robust, typed interface for interacting with LLMs that adhere to the Open Responses standard. It includes a high-performance async client, Pydantic V2 models, and utilities for building compliant providers.

## ✨ Features

- **Standardization**: Strict Pydantic V2 models for `InputText`, `MessageItem`, `ReasoningItem`, `ToolCallItem`, ensuring type safety and validation.
- **High Performance**: Built on `httpx` with full async/await support and efficient streaming.
- **Semantic Streaming**: First-class support for streaming reasoning (thinking) and text deltas separately.
- **Provider Agnostic**: Seamlessly switch between OpenRouter, OpenAI, Ollama, LM Studio, and HuggingFace TGI.
- **Developer-First**: Fully typed, thoroughly tested, and ready for production.

## 📦 Installation

Install via pip:

```bash
pip install openresponses-python
```

We recommend using [uv](https://github.com/astral-sh/uv) for modern dependency management:

```bash
uv add openresponses-python
```

## 🚀 Quick Start

Here's how to send a request to a compliant provider (e.g., OpenRouter or a local proxy).

### 1. Simple Request

```python
import asyncio
from openresponses.client import AsyncOpenResponsesClient

async def main():
    # Initialize client (defaults to local proxy if base_url not set)
    # Ensure you have a provider running (see Examples below)
    client = AsyncOpenResponsesClient(base_url="http://localhost:8001")

    response = await client.create(
        model="deepseek/deepseek-r1",
        input="Explain semantic streaming.",
    )

    # Access the output items directly
    for item in response.output:
        if item.type == "message":
            print(f"Answer: {item.content}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Semantic Streaming

Stream reasoning ("thinking") and the final response in real-time.

```python
stream = await client.create(
    model="deepseek/deepseek-r1",
    input="Why is the sky blue?",
    stream=True
)

async for event in stream:
    if event.event == "response.reasoning.delta":
            print(f"🧠 {event.data['delta']}", end="", flush=True)
    elif event.event == "response.text.delta":
            print(f"🤖 {event.data['delta']}", end="", flush=True)
```

## 🔌 Supported Providers

This package includes proxy examples to adapt popular providers to the Open Responses standard.

| Provider        | Command                | Port   | Description                                            |
| :-------------- | :--------------------- | :----- | :----------------------------------------------------- |
| **OpenRouter**  | `make run-openrouter`  | `8001` | Access DeepSeek R1, Claude 3.5, Gemini via OpenRouter. |
| **OpenAI**      | `make run-openai`      | `8002` | Standard OpenAI API proxy.                             |
| **Ollama**      | `make run-ollama`      | `8003` | Local AI models (Llama 3, Mistral).                    |
| **LM Studio**   | `make run-lmstudio`    | `8004` | Local inference server.                                |
| **HuggingFace** | `make run-huggingface` | `8005` | TGI / Inference Endpoints.                             |

## 🛠️ Development

We use `uv` for dependency management and `make` for task automation.

```bash
git clone https://github.com/uday/openresponses-python.git
cd openresponses-python
make install      # Sync dependencies
make test         # Run tests
make lint         # Run linters
make docs-serve   # Preview documentation
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTION.md](CONTRIBUTION.md) for guidelines.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
