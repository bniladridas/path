[#50](https://github.com/bniladridas/path/pull/50) • Milestone: Gemini (closed)

# harper

## Demo

https://github.com/user-attachments/assets/460a42b9-d2ea-42d3-8d1f-13bd8fb54565



The codebase is a minimal Flask web application for AI-powered media exploration, structured as follows:

**Core Structure:**
- `app.py`: Main Flask app with routes for index, verify, search, terms, privacy, updates. Uses Google Gemini 2.0 Flash API for AI responses. Implements human verification, session management, and error handling.
- `templates/`: 5 HTML templates (index, verify, terms, privacy, updates) with semantic markup, accessibility features, and minimal inline JS.
- `static/css/style.css`: Theme system using CSS custom properties, responsive design.
- `requirements.txt`: Minimal dependencies (Flask, requests, python-dotenv).
- `tests/test_app.py`: Basic pytest tests.

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

## Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm

```bash
# Clone the repository
git clone https://github.com/bniladridas/path.git
cd path

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies for testing
npm install

# Install Playwright browsers
npx playwright install
```

## Running the Application

Start the development server:

```bash
GEMINI_API_KEY=your-key python app.py
```

## Testing

### Unit Tests
Run the Python unit tests:

```bash
pytest
```

### API Key Testing
To verify your Gemini API key and check available models:

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual key. This lists all available models.

### End-to-End Tests

Run the Playwright e2e tests:

```bash
# Run tests in headless mode
npm test

# Run tests in UI mode (interactive)
npm run test:ui

# Run tests in headed mode (visible browser)
npm run test:headed

# Run tests in debug mode
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
