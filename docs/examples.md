# Examples

The `openresponses-python` repository includes several proxy implementations to adapt popular LLM providers to the Open Responses standard.

All examples are located in the `examples/` directory.

## OpenRouter

Proxies requests to [OpenRouter](https://openrouter.ai). Perfect for accessing models like DeepSeek R1, Claude 3.5, etc.

**Run:**

```bash
make run-openrouter
```

**Port:** `8001`
**Env:** `OPENROUTER_API_KEY`

## OpenAI

Proxies requests to [OpenAI](https://openai.com).

**Run:**

```bash
make run-openai
```

**Port:** `8002`
**Env:** `OPENAI_API_KEY`

## Ollama (Local)

Proxies to a local [Ollama](https://ollama.com) instance running on `localhost:11434`.

**Run:**

```bash
make run-ollama
```

**Port:** `8003`

## LM Studio (Local)

Proxies to local [LM Studio](https://lmstudio.ai) running on `localhost:1234`.

**Run:**

```bash
make run-lmstudio
```

**Port:** `8004`

## HuggingFace (Inference API / TGI)

Proxies to HuggingFace Inference Endpoints or TGI.

**Run:**

```bash
make run-huggingface
```

**Port:** `8005`
**Env:** `HF_API_KEY` (Optional), `HF_BASE_URL` (Defaults to public API)
