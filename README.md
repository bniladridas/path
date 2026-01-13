# Harper

## Purpose: Package Migration

This repository primarily documents and validates a **package migration** for Harper. The goal of this change is to modernize dependencies, reduce maintenance risk, and keep the application aligned with supported SDKs—**without changing user‑visible behavior**.

> **TL;DR**: Harper was migrated from the deprecated `google.generativeai` package to the modern `google.genai` SDK. All imports, API calls, and dependencies were updated while preserving functionality, routes, and behavior.

---

## Why This Migration

* **Deprecation risk**: `google.generativeai` is deprecated and no longer recommended.
* **Forward compatibility**: `google.genai` is the supported SDK going forward.
* **Maintenance & security**: Supported SDKs receive fixes, improvements, and security updates.
* **No feature churn**: The migration intentionally avoids product or UX changes.

---

## Scope of Changes

### What Changed

* Replaced all `google.generativeai` imports with `google.genai`
* Updated client initialization and request patterns to match the new SDK
* Adjusted dependency versions in `requirements.txt`
* Verified all AI-backed routes continue to work as before

### What Did *Not* Change

* Application behavior and responses
* Flask routes and URL structure
* Templates, CSS, and frontend behavior
* Test coverage and CI expectations
* Deployment model (Vercel / Docker compatible)

---

## Migration Summary

| Area           | Before                | After              |
| -------------- | --------------------- | ------------------ |
| Gemini SDK     | `google.generativeai` | `google.genai`     |
| Support status | Deprecated            | Actively supported |
| API surface    | Legacy                | Current / stable   |
| Behavior       | —                     | Unchanged          |

The migration was performed as a **mechanical, low‑risk refactor**, focusing on correctness and parity.

---

## Validation & Verification

To ensure migration safety:

* All existing unit tests pass (`pytest`)
* End‑to‑end Playwright tests pass
* Manual verification of AI search, verification flow, and static routes
* No runtime warnings or SDK deprecation notices

This confirms functional equivalence before and after the migration.

---

## Documentation Index

Minimal documentation relevant to the migration and maintenance:

* [API.md](API.md) — API endpoints and usage examples
* [docs/development/README.md](docs/development/README.md) — Development workflow
* [docs/development/hooks/README.md](docs/development/hooks/README.md) — Git hooks overview
* [docs/development/hooks/ruff.md](docs/development/hooks/ruff.md) — Ruff configuration
* [docs/development/hooks/pre-commit.md](docs/development/hooks/pre-commit.md) — Pre‑commit hooks

---

## Codebase Context (Post‑Migration)

Harper remains a minimal Flask web application for AI‑powered media exploration.

### Core Structure

* `path/app.py`: Flask app and routes, now using `google.genai`
* `templates/`: Jinja templates for all static and dynamic pages
* `static/css/style.css`: Theme system and responsive styles
* `requirements.txt`: Updated, minimal dependencies
* `tests/`: Unit tests validating route behavior

The migration does **not** introduce architectural changes.

---

## Setup (Unchanged)

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

### Run

```bash
GEMINI_API_KEY=your-key python path/app.py
```

---

## Testing

```bash
pytest
npm test
```

API key sanity check:

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

---

## Related Refactors (Non‑Blocking)

While outside the core package migration, the repository also includes a completed **Jinja template refactor**:

* 800+ lines of hardcoded HTML removed from JavaScript
* Content moved to proper Jinja templates
* AJAX loading via Flask routes
* Improved security, maintainability, and separation of concerns

This refactor is **orthogonal** to the SDK migration and can be reviewed independently.

---

## Commit Discipline

This migration follows **conventional commits** to keep history reviewable and safe for backports.

Example:

```
refactor: migrate gemini sdk to google.genai
```

---

## Migration Guarantee

This change is:

* ✅ Backward‑compatible
* ✅ Behavior‑preserving
* ✅ Safe to roll back
* ✅ Required for long‑term maintenance

No product decisions were made as part of this work—**only dependency hygiene**.
