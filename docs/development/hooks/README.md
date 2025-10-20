# Git Hooks

This directory contains documentation for the Git hooks used in the project.

## Available Hooks

- [Pre-commit Hooks](./pre-commit.md): Run before each commit
  - Ruff Linting
  - Code Formatting

## Configuration

Hooks are configured in `.pre-commit-config.yaml` in the project root. The configuration specifies which hooks to run and their settings.

## Adding New Hooks

To add a new hook:

1. Add the hook configuration to `.pre-commit-config.yaml`
2. Document the hook in a new markdown file in this directory
3. Update this README to include the new hook

## Best Practices

- Keep hooks fast - they should run in seconds, not minutes
- Document any configuration options
- Include instructions for bypassing if needed (though this should be rare)
- Test hooks in CI to ensure they catch the issues they're meant to catch
