# Open Responses Python - Makefile

.PHONY: install install-dev lint format test build clean help
.PHONY: run-openrouter run-openai run-ollama run-lmstudio run-huggingface run-client

# --- Installation & Setup ---

install: ## Install package dependencies using uv (includes dev deps)
	uv sync

install-all: ## Install package with all optional extras
	uv sync --all-extras

lock: ## Update lock file
	uv lock

# --- Quality Assurance ---

lint: ## Run linting (ruff)
	uv run ruff check .

format: ## Run formatting (ruff)
	uv run ruff format .

test: ## Run tests (pytest)
	uv run pytest tests/

# --- Build ---

build: ## Build distribution packages
	uv run hatch build

clean: ## Clean build artifacts and cache
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

# --- Examples ---

run-openrouter: ## Run OpenRouter Proxy Example (Port 8001)
	uv run python examples/openrouter_proxy.py

run-openai: ## Run OpenAI Proxy Example (Port 8002)
	uv run python examples/openai_proxy.py

run-ollama: ## Run Ollama Proxy Example (Port 8003)
	uv run python examples/ollama_proxy.py

run-lmstudio: ## Run LM Studio Proxy Example (Port 8004)
	uv run python examples/lmstudio_proxy.py

run-huggingface: ## Run HuggingFace Proxy Example (Port 8005)
	uv run python examples/huggingface_proxy.py

run-client: ## Run the Demo Client
	uv run python client.py

# --- Documentation ---

docs-serve: ## Serve documentation locally
	uv run mkdocs serve

docs-build: ## Build documentation
	uv run mkdocs build

# --- Help ---

help: ## Show this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
