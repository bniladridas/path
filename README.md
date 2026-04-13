<p align="left">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/Rust-1.75%2B-orange" alt="Rust 1.75+">
    <a href="https://github.com/bniladridas/path/actions/workflows/ci-cd.yml">
        <img src="https://github.com/bniladridas/path/actions/workflows/ci-cd.yml/badge.svg" alt="CI/CD Pipeline">
    </a>
    <a href="https://codecov.io/gh/bniladridas/path">
        <img src="https://codecov.io/gh/bniladridas/path/branch/main/graph/badge.svg" alt="codecov">
    </a>
    <a href="/LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg" alt="License: CC BY 4.0"/>
    </a>
</p>

The project opens with badges highlighting support for Python 3.10+, Rust 1.75+, and the Creative Commons BY 4.0 license, giving a quick overview of compatibility and licensing at a glance. Harper is introduced as an AI-powered media exploration application built with Flask and Google Gemini, designed to combine powerful AI capabilities with an intuitive interface. The motivation behind the project was to create a media exploration tool that leverages Gemini while staying simple and practical, since many existing solutions were either too complex or lacked essential features. The core idea was to offer two ways to interact with Gemini AI: a browser-based web application and a CLI for terminal-based workflows, bringing both together in one easy-to-use package. ✨

Harper includes features such as AI-powered search using Gemini models, image generation with Gemini 2.5 Flash Image, an interactive terminal-based TUI, a CAPTCHA-like human verification flow, OpenAI-compatible API endpoints, and dual interfaces through Flask for the web and Rust for the CLI. These features allow users to explore media flexibly, whether working visually in the browser or efficiently from the terminal. 🚀

To get started, users need Python 3.10+, Node.js 16+, and npm. The web application setup involves cloning the repository, installing dependencies, configuring the `.env` file with a `GEMINI_API_KEY`, and running the app with `python run.py`, after which it is accessible at `http://localhost:8000`. The CLI is built by navigating to the `rust` directory, compiling in release mode, copying the binary to `~/.local/bin`, and configuring the same environment variables. Once installed, users can launch the interactive TUI, run searches, or generate images directly from the command line. 🛠️

The TUI controls are intentionally minimal: typing starts a search, Enter submits the query, and Escape clears input or exits. The documentation also references Google Gemini resources, lists supported models such as Gemini 2.5 Flash and Gemini 2.5 Flash Image, and outlines the tech stack. The web layer uses Flask, Google GenAI SDK, Gunicorn, Playwright, and Vercel, while the CLI is built in Rust using Crossterm, Ratatui, and Reqwest. 🔧

After obtaining an API key from Google AI Studio and configuring it in the environment, users can fully enable AI functionality. The project is licensed under Creative Commons Attribution 4.0, and contributions are welcome through pull requests, encouraging collaborative improvements and community-driven development. 🤝
