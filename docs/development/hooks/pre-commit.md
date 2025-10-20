# Pre-commit Hooks

This document describes the Git pre-commit hooks configured in the project.

## Overview

Pre-commit hooks are scripts that run automatically before each commit to ensure code quality and consistency. This project uses the [pre-commit](https://pre-commit.com/) framework to manage these hooks.

## Available Hooks

### Ruff

- **Purpose**: Lint and format Python code
- **Configuration**: See [Ruff Hooks](./ruff.md)
- **Runs**: On every commit for Python files

### Ruff Format

- **Purpose**: Automatically format Python code
- **Configuration**: Uses project's `pyproject.toml`
- **Runs**: On every commit for Python files

## Installation

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install the git hook scripts:
   ```bash
   pre-commit install
   ```

## Usage

- Hooks run automatically on `git commit`
- To run manually on all files:
  ```bash
  pre-commit run --all-files
  ```
- To run a specific hook:
  ```bash
  pre-commit run ruff --all-files
  ```

## Skipping Hooks

To skip hooks for a commit:
```bash
git commit --no-verify -m "Your commit message"
```

> **Note**: Only skip hooks when absolutely necessary, as they help maintain code quality.

## Troubleshooting

- If a hook is failing, it will show you the error output
- Most hooks can fix issues automatically - try committing again after the first run
- To see verbose output:
  ```bash
  pre-commit run -v
  ```
