<p align="left">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/Rust-1.75%2B-orange" alt="Rust 1.75+">
    <a href="/LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg" alt="License: CC BY 4.0"/>
    </a>
</p>

<p align="left">
    <a href="https://discord.gg/J8DetsWcqU">
        <img src="https://img.shields.io/badge/Join-Discord-blue?logo=discord" alt="Discord Server"/>
    </a>
</p>

> [!NOTE]
>
> Need help? Join the [Discord Server](https://discord.gg/J8DetsWcqU) and get help with setup and usage.

An AI-powered media exploration application using Flask and Google Gemini.

## Why did I make this?

I wanted to create a media exploration tool that combines the power of Google's Gemini AI with an intuitive interface. Existing solutions were either too complex or lacked the features I needed.

The main goal was to provide two ways to interact with Gemini AI:
1. A web application for browser-based exploration
2. A CLI for terminal-based workflows

Harper brings both together in a single, easy-to-use package.

## Features

- AI-powered search using Google Gemini models
- Image generation with Gemini 2.5 Flash Image
- Interactive TUI for terminal-based workflows
- Email verification flow
- Responsive design with theme support
- OpenAI compatible API endpoints
- Dual interfaces: Web (Flask) and CLI (Rust)

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm
- Rust 1.75+ (for CLI)

### Web Application

```bash
# Clone the repository
git clone https://github.com/bniladridas/path.git
cd path

# Install dependencies
pip install -r requirements.txt
npm install

# Set up environment
cp .env.example .env
# Edit .env with your GEMINI_API_KEY

# Run the app
python run.py
```

Open your browser and navigate to `http://localhost:5000`

### CLI

```bash
# Build the Rust CLI
cd rust
cargo build --release
cp target/release/harper ~/.local/bin/harper

# Set up environment
cp .env.example .env
# Edit .env with your GEMINI_API_KEY
```

### Usage

```bash
# Web app - open http://localhost:5000

# CLI
harper tui           # Interactive TUI
harper search "query" # Command line search
harper image --prompt "a sunset" # Generate image
```

### Demo

https://github.com/user-attachments/assets/6e577b8c-4902-4c47-a161-e44ed56fc1e2

### TUI Controls

| Key | Action |
|:---|:---|
| Type | Start searching |
| Enter | Submit query |
| Esc | Clear or quit |

## API Reference

### Google Gemini

General: [Overview](https://ai.google.dev/docs) | [API Docs](https://ai.google.dev/api) | [Pricing](https://ai.google.dev/pricing)

Python: [PyPI](https://pypi.org/project/google-genai/) | [SDK Docs](https://googleapis.github.io/python-genai/)

JavaScript: [NPM](https://www.npmjs.com/package/@google/genai) | [Node](https://github.com/googleapis/js-genai)

### Supported Models

- Gemini 2.5 Flash
- Gemini 2.5 Flash Image

## Tech Stack

### Web Application
- Flask 3.1.2 - Web framework
- Google GenAI SDK - AI integration
- Gunicorn - WSGI server
- Playwright - E2E testing
- Vercel - Deployment

### CLI
- Rust - Programming language
- Crossterm - Terminal UI
- Ratatui - TUI library
- Reqwest - HTTP client

## API Key Setup

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey):

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

---

Contributions are welcome! Please feel free to submit a Pull Request.
