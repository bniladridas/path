# Harper [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

An AI-powered media exploration web application using Flask and Google Gemini.

## Sharing
- [Share on Twitter](http://twitter.com/home?status=http://github.com/bniladridas/path)
- [Share on Facebook](http://www.facebook.com/sharer/sharer.php?u=http://github.com/bniladridas/path)
- [Share on Google Plus](http://plus.google.com/share?url=http://github.com/bniladridas/path)
- [Share on LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=http://github.com/bniladridas/path)

## Table of Contents

### AI Services
- [AI Search](#ai-search)

## AI Services

<h2 id="ai-search">AI Search / Generative AI</h2>

### Google Gemini
General: [Overview](https://ai.google.dev/docs) | [API Docs](https://ai.google.dev/api) | [Pricing](https://ai.google.dev/pricing)

Python: [PyPI](https://pypi.org/project/google-genai/) | [SDK Docs](https://google.github.io/python-genai/)

JavaScript: [NPM](https://www.npmjs.com/package/google-genai) | [Node](https://github.com/google/generative-ai-js)

- Generate responses based on natural language queries
- Contextual understanding of user intent
- Real-time API integration for search functionality

Supported models: Gemini 2.0 Flash, Gemini 1.5 Pro, Gemini 1.5 Flash

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
```

### Run
```bash
# Set your API key and run the app
GEMINI_API_KEY=your-key python run.py
```

### Testing
```bash
pytest
npm test
```

### API Key Verification
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

## Tech Stack

### Backend
- Flask 3.1.2 - Web framework
- Google Genai SDK - AI integration
- Gunicorn - WSGI server
- Python Dotenv - Environment variables

### Frontend
- HTML/CSS/JavaScript - User interface
- Playwright - E2E testing

### Deployment
- Vercel - Cloud platform
- Docker - Containerization

## Project Structure

```
path/
├── path/
│   ├── app.py           # Flask application and routes
│   └── __init__.py      # Package initialization
├── templates/            # Jinja2 templates
├── static/              # Static assets (CSS, images)
├── shared/              # Shared utilities
├── tests/               # Unit tests
├── e2e/                 # End-to-end tests
├── run.py               # Application entry point
├── requirements.txt     # Python dependencies
└── package.json         # Node.js dependencies
```

## Features

- AI-powered search using Google Gemini
- Email verification flow
- Static page routing
- Responsive design
- Theme support

## License
[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

---

Contributions are welcome! Please feel free to submit a Pull Request.
