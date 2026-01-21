# Quickstart

This guide will help you send your first request using `openresponses-python`.

## 1. Setup a Provider

The SDK connects to any Open Responses compliant API. For this example, we will use the **OpenRouter Proxy** included in the package examples.

Ensure you have your API key set:

```bash
export OPENROUTER_API_KEY=sk-or-...
```

Run the example proxy in a separate terminal:

```bash
make run-openrouter
# Server starts at http://localhost:8001
```

## 2. Create the Client Application

Create a file `main.py`:

```python
import asyncio
from openresponses.client import AsyncOpenResponsesClient

async def main():
    # Connect to the local provider we started
    client = AsyncOpenResponsesClient(base_url="http://localhost:8001")

    print("Sending request...")

    # Send a request with streaming enabled
    stream = await client.create(
        model="deepseek/deepseek-r1",
        input="Why is the sky blue?",
        stream=True
    )

    print("\nResponse:")
    async for event in stream:
        if event.event == "response.reasoning.delta":
             # Print reasoning (thinking) in grey or italic
             print(f"\033[90m{event.data['delta']}\033[0m", end="", flush=True)
        elif event.event == "response.text.delta":
             # Print final answer
             print(event.data['delta'], end="", flush=True)

    print("\n\nDone!")

if __name__ == "__main__":
    asyncio.run(main())
```

## 3. Run It

```bash
python main.py
```

You should see the models "thinking" process (if supported) followed by the answer.
