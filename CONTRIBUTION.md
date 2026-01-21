# Contributing to Open Responses Python

Thank you for your interest in contributing! We welcome all contributions to help standardize AI responses.

## Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/uday/openresponses-python.git
   cd openresponses-python
   ```

2. **Install using uv:**
   We use `uv` for fast, reproducible dependency management.

   ```bash
   # Syncs dependencies and creates .venv
   make install
   # OR
   uv sync
   ```

3. **Verify installation:**
   ```bash
   make test
   ```

## Development Workflow

- **Linting:** Run `make lint` before committing to ensure code style compliance.
- **Formatting:** Run `make format` to auto-format code.
- **Testing:** Run `make test` to execute the test suite.

## Pull Request Guidelines

1. Fork the repository and create a feature branch.
2. Ensure all tests pass and code is linted.
3. Submit a Pull Request with a clear description of changes.
