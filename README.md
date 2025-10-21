# harper

## Documentation

All minimal documentation files created:

* [API.md](API.md) — API endpoints and usage examples
* [docs/development/README.md](docs/development/README.md) — Main development documentation
* [docs/development/hooks/README.md](docs/development/hooks/README.md) — Git hooks overview
* [docs/development/hooks/ruff.md](docs/development/hooks/ruff.md) — Ruff configuration and usage
* [docs/development/hooks/pre-commit.md](docs/development/hooks/pre-commit.md) — Pre-commit hooks guide

## Demo

[https://github.com/user-attachments/assets/460a42b9-d2ea-42d3-8d1f-13bd8fb54565](https://github.com/user-attachments/assets/460a42b9-d2ea-42d3-8d1f-13bd8fb54565)

The codebase is a minimal Flask web application for AI-powered media exploration, structured as follows:

**Core Structure:**

* `app.py`: Main Flask app (in repo root) with routes for index, verify, search, terms, privacy, updates. Uses Google Gemini 2.0 Flash API for AI responses. Implements human verification, session management, and error handling.
* `templates/`: 5 HTML templates (index, verify, terms, privacy, updates) with semantic markup, accessibility features, and minimal inline JS.
* `static/css/style.css`: Theme system using CSS custom properties, responsive design.
* `requirements.txt`: Minimal dependencies (Flask, requests, python-dotenv).
* `tests/test_app.py`: Basic pytest tests.

**Code Style:**

* Clean, readable Python with type hints and docstrings.
* Semantic HTML5 with ARIA attributes for accessibility.
* Vanilla JavaScript with event listeners, no frameworks.
* Consistent indentation, lowercase responses, minimal comments.
* Error handling with user-friendly messages.
* No unnecessary complexity; focused on core functionality.

**Current State:**

* All routes functional, AI integration working.
* Responsive design with 5 theme options.
* Human verification with keyword matching.
* Privacy-focused (no conversation storage).
* Ready for deployment (Vercel/Docker support).

## Setup

### Prerequisites

* Python 3.8+
* Node.js 16+
* npm

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

* `e2e/`: End-to-end test files

  * `fixtures/`: Shared test fixtures and utilities
  * `navigation.spec.js`: Tests for navigation and static pages
  * `search.spec.js`: Tests for search functionality
  * `verification.spec.js`: Tests for user verification flow
* `tests/`: Unit tests

  * `test_app.py`: Basic route tests

The code is production-ready, maintainable, and follows best practices for a small web app. Comprehensive test coverage ensures reliability and prevents regressions.

## Conventional Commits

This project uses conventional commit standards to maintain a clean and consistent git history.

### Setup

```bash
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

### Usage

Commit messages must follow this format:

* Start with a type: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`
* First line lowercase and ≤60 characters
* Example: `feat: add user authentication`

### History Cleanup

```bash
./scripts/rewrite_msg.sh
git push --force-with-lease
```
