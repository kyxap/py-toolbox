# py-toolbox

A collection of useful Python scripts and utilities for various tasks. 

This library is designed to store reusable scripts and subprojects to avoid code duplication across different projects. You can import modules from `py_toolbox` and use them in your own workflows.

## Features
- **Centralized Utilities**: A single place to store your Python helpers.
- **Easy Imports**: Import what you need directly from `py_toolbox`.
- **uv-Powered**: Managed with [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.
- **CI/CD Ready**: Automated testing and linting via GitHub Actions.

## Usage
If you find these scripts useful, feel free to use them! 
If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

As the collection grows and if certain tools gain enough popularity or complexity, they may be migrated into their own dedicated libraries.

### Example: Bitwarden Manager
```python
from py_toolbox import BitwardenManager

bw = BitwardenManager()
# bw.unlock("your_master_password")
# password = bw.get_password("MyItemName")
```

## Development
To set up the development environment:

1. Install [uv](https://github.com/astral-sh/uv).
2. Clone the repository and run:
   ```bash
   uv sync
   ```
3. Run tests:
   ```bash
   uv run pytest
   ```
4. Run lint checks:
   ```bash
   uv run ruff check .
   ```

---
Happy coding!
