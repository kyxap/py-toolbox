# Gemini CLI Project Context: py-toolbox

This is a Python library managed by `uv` for storing reusable scripts and utilities.

## Architectural Patterns
- **Layout**: Standard `src-layout` with `src/py_toolbox` as the main package.
- **Submodules**: Tools are organized into submodules (e.g., `src/py_toolbox/bitwarden`).
- **Imports**: Preferred import style is `from py_toolbox import BitwardenManager`.
- **Tests**: Mirror the source structure in `tests/` (e.g., `tests/bitwarden/test_manager.py`).

## Coding Standards
- **Language**: All code comments and docstrings must be in **English**.
- **Formatting**: Use `ruff` for linting and formatting.
- **Style Preference**: Simple exception classes should NOT have extra blank lines after docstrings (e.g., keep `pass` on the next line).
- **Dependencies**: Use `uv` for all dependency management.

## CI/CD
- GitHub Actions are configured in `.github/workflows/` for both `main` branch pushes and pull requests.
- Both workflows run linting and tests using `uv`.

## Key Commands
- `uv run pytest`: Run tests.
- `uv run ruff check .`: Run linter.
- `uv run ruff format .`: Format code.
