## Documentation

All minimal documentation files created:

- [docs/development/README.md](docs/development/README.md) — Main development documentation
- [docs/development/hooks/README.md](docs/development/hooks/README.md) — Git hooks overview
- [docs/development/hooks/ruff.md](docs/development/hooks/ruff.md) — Ruff configuration and usage
- [docs/development/hooks/pre-commit.md](docs/development/hooks/pre-commit.md) — Pre-commit hooks guide

## Demo

[https://github.com/user-attachments/assets/460a42b9-d2ea-42d3-8d1f-13bd8fb54565](https://github.com/user-attachments/assets/460a42b9-d2ea-42d3-8d1f-13bd8fb54565)

The codebase is a Flask web application for AI-powered media exploration with comprehensive CI/CD and deployment infrastructure, structured as follows:

**Core Structure:**

- `app_local.py`: Main Flask app with routes for index, verify, search, terms, privacy, updates. Uses Google Gemini 2.0 Flash API for AI responses. Implements human verification, session management, and error handling.
- `app.py`: Docker entry point that imports from `app_local.py` for Gunicorn compatibility.
- `templates/`: 5 HTML templates (index, verify, terms, privacy, updates) with semantic markup, accessibility features, and minimal inline JS.
- `static/css/style.css`: Theme system using CSS custom properties, responsive design.
- `requirements.txt`: Production dependencies including Flask, Google Generative AI, Gunicorn, and security packages.
- `tests/test_app.py`: Basic pytest tests.

**Development Infrastructure:**

- `.github/workflows/`: Automated CI/CD with Python 3.8-3.12 matrix testing, security scanning, Docker builds, and semantic releases.
- `scripts/`: Unused code detection and cleanup tools.
- `path/`: Vercel deployment structure with API endpoints.
- `requirements-dev.txt`: Development dependencies including testing, linting, and security tools.
- `requirements-py38.txt`: Python 3.8 compatible dependencies for legacy support.

**Code Style:**

- Clean, readable Python with type hints and docstrings.
- Semantic HTML5 with ARIA attributes for accessibility.
- Vanilla JavaScript with event listeners, no frameworks.
- Consistent indentation, lowercase responses, minimal comments.
- Error handling with user-friendly messages.
- No unnecessary complexity; focused on core functionality.

**Current State:**

- All routes functional, AI integration working.
- Responsive design with 5 theme options.
- Human verification with keyword matching.
- Privacy-focused (no conversation storage).
- Ready for deployment (Vercel/Docker support).

## Python Path and Module Structure

The project uses a modular structure with proper Python path management for different deployment environments:

### Directory Structure

```
path/
├── path/                    # Main application module
│   ├── app.py              # Flask application with all routes
│   ├── index.py            # Vercel entry point
│   ├── templates/          # HTML templates
│   ├── static/             # CSS and static assets
│   └── requirements.txt    # Module-specific dependencies
├── shared/                 # Shared utilities
│   └── requests_fallback.py # HTTP client fallback implementation
├── templates/              # Root templates (copied to path/ for deployment)
├── static/                 # Root static files (copied to path/ for deployment)
└── scripts/                # Deployment and utility scripts
```

### Python Path Management

The application handles Python path configuration for different environments:

**Local Development:**
```python
# Uses root directory structure
PROJECT_ROOT = str(Path(__file__).parent.parent)
sys.path.insert(0, PROJECT_ROOT)
```

**Vercel Deployment:**
```python
# Robust import handling with fallbacks
try:
    from shared.requests_fallback import setup_requests_fallback
    setup_requests_fallback()
except ImportError:
    # Graceful fallback if shared modules unavailable
    pass
```

**Docker Deployment:**
```python
# Uses PYTHONPATH environment variable
ENV PYTHONPATH="."
```

### Module Import Strategy

1. **Path Setup First**: Add project root to `sys.path` before imports
2. **Graceful Fallbacks**: Handle missing modules without crashing
3. **Environment Awareness**: Different import strategies for different deployment targets
4. **Shared Utilities**: Common code in `shared/` directory accessible across modules

This structure ensures the application works consistently across local development, Vercel serverless functions, and Docker containers while maintaining clean separation of concerns.

## Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm

```bash
git clone https://github.com/bniladridas/path.git
cd path
pip install -r requirements.txt
npm install
npx playwright install
```

### Running the Application

```bash
GEMINI_API_KEY=your-key python app.py
```

## Testing

### Unit Tests

```bash
pytest
```

### API Key Testing

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

### End-to-End Tests

```bash
npm test          # headless
npm run test:ui   # interactive
npm run test:headed
npm run test:debug
```

### Test Structure

- `e2e/`: End-to-end test files

  - `fixtures/`: Shared test fixtures and utilities
  - `navigation.spec.js`: Tests for navigation and static pages
  - `search.spec.js`: Tests for search functionality
  - `verification.spec.js`: Tests for user verification flow

- `tests/`: Unit tests

  - `test_app.py`: Basic route tests

The code is production-ready, maintainable, and follows best practices for a small web app. Comprehensive test coverage ensures reliability and prevents regressions.

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and consistency. The configuration is defined in `.pre-commit-config.yaml`.

### Setup

1. Install pre-commit:

   ```bash
   pip install pre-commit
   ```

2. Install the git hooks:
   ```bash
   pre-commit install
   ```

### Available Hooks

- **Python Linting**: Uses `ruff` for code quality and formatting
- **YAML Linting**: Validates YAML syntax and style using `yamllint`
- **End of File Fixer**: Ensures files end with a newline
- **Trailing Whitespace**: Removes trailing whitespace
- **YAML Syntax Check**: Validates YAML files for syntax errors

### Running Hooks Manually

To run all hooks on all files:

```bash
pre-commit run --all-files
```

To run a specific hook (e.g., yamllint):

```bash
pre-commit run yamllint --all-files
```

### YAML Linting

YAML files are linted using `yamllint` with the configuration in `.yamllint`. Common issues and fixes are documented in [docs/development/troubleshooting/yaml-linting.md](docs/development/troubleshooting/yaml-linting.md).

To check YAML files without committing:

```bash
yamllint .
```

### Updating Hooks

To update to the latest versions of the hooks:

```bash
pre-commit autoupdate
```

## Conventional Commits

This project uses conventional commit standards to maintain a clean and consistent git history.

### Setup

```bash
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

### Usage

Commit messages must follow this format:

- Start with a type: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`
- First line lowercase and ≤60 characters
- Example: `feat: add user authentication`

### History Cleanup

```bash
./scripts/rewrite_msg.sh
git push --force-with-lease
```
