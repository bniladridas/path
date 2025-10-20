# YAML Linting Troubleshooting Guide

This guide helps you resolve common YAML linting issues in the project.

## Common YAML Linting Issues

### 1. Indentation Errors
- **Error**: `wrong indentation: expected X but found Y`
- **Solution**: Ensure consistent indentation (2 spaces per level)
- **Example**:
  ```yaml
  # Bad
  key:
      nested: value  # 4 spaces

  # Good
  key:
    nested: value  # 2 spaces
  ```

### 2. Missing Newlines
- **Error**: `no new line character at the end of file`
- **Solution**: Always end YAML files with a single newline character

### 3. Bracket Spacing
- **Error**: `too many spaces inside brackets`
- **Solution**: Remove extra spaces inside brackets
- **Example**:
  ```yaml
  # Bad
  branches: [ "main", "develop" ]

  # Good
  branches: ["main", "develop"]
  ```

### 4. Line Length
- **Error**: `line too long (X > 120 characters)`
- **Solution**: Break long lines into multiple lines
- **Example**:
  ```yaml
  # Bad
  long_line: This is a very long line that exceeds the maximum allowed length of 120 characters and should be broken into multiple lines

  # Good
  long_line: >
    This is a very long line that exceeds the maximum allowed
    length of 120 characters and has been broken into multiple lines
  ```

## Running YAML Lint

To check for YAML linting issues:

```bash
# Install yamllint (if not already installed)
pip install yamllint

# Run yamllint on all YAML files
yamllint .

# Run with auto-fix for some issues
yamllint --fix .
```

## Common Fixes

### Fix All YAML Files
```bash
# Add newlines to end of files
find . -type f \( -name "*.yaml" -o -name "*.yml" \) -exec sh -c 'echo >> "$1"' _ {} \;

# Fix indentation and formatting
yamllint -f parsable . | while read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    line_num=$(echo "$line" | cut -d: -f2)
    # Apply fixes based on error type
    # ... (add specific fixes as needed)
done
```

## Editor Integration

### VS Code
1. Install the "YAML" extension by Red Hat
2. Add this to your VS Code settings:
   ```json
   {
     "yaml.format.enable": true,
     "yaml.format.bracketSpacing": false,
     "yaml.format.singleQuote": false,
     "yaml.format.proseWrap": "preserve",
     "yaml.validate": true,
     "yaml.schemas": {
         "https://json.schemastore.org/github-workflow.json": ".github/workflows/*.yml"
     }
   }
   ```

## Pre-commit Hook

To automatically check YAML files before committing, add this to your `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/adrienverge/yamllint.git
    rev: v1.30.0
    hooks:
    -   id: yamllint
        args: [--strict, --format, colored]
```
