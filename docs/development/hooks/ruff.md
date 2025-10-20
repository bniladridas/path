# Ruff Hooks

This document outlines the Ruff hooks configured in the project and how to use them.

## Overview

Ruff is an extremely fast Python linter and code formatter. We use it to maintain consistent code style and catch potential issues early in the development process.

## Configuration

Ruff is configured in `pyproject.toml` with the following key settings:

```toml
[tool.ruff]
line-length = 127
target-version = "py311"

# ... other configurations ...
```

## Pre-commit Hooks

The following pre-commit hooks are configured:

1. **ruff**: Runs the linter with auto-fixing capabilities
   - Automatically fixes fixable issues
   - Exits with non-zero code if any issues remain

2. **ruff-format**: Formats Python code
   - Uses a line length of 127 characters
   - Applies consistent formatting rules

## Usage

### Manual Linting

To run the linter manually:

```bash
# Check for issues
ruff check .

# Fix fixable issues
ruff check --fix .

# Check a specific file
ruff check path/to/file.py
```

### Formatting Code

To format code using ruff-format:

```bash
# Format all Python files
ruff format .

# Check formatting without making changes
ruff format --check .
```

## Common Issues

### Disabling Rules

To disable specific rules, add a `# noqa: CODE` comment at the end of the line or use the `per-file-ignores` configuration in `pyproject.toml`.

### Integration with IDEs

Most modern IDEs have plugins or built-in support for Ruff. Refer to your IDE's documentation for setup instructions.

## Troubleshooting

- If you encounter issues with Ruff, try clearing its cache:
  ```bash
  ruff clean
  ```

- For verbose output, use the `-v` flag:
  ```bash
  ruff check -v .
  ```
