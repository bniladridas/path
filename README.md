<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Rust-1.75%2B-orange?style=for-the-badge&logo=rust" alt="Rust 1.75+">
  <img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=for-the-badge" alt="License: CC BY 4.0">
</p>

<p align="center">
  <a href="https://discord.gg/J8DetsWcqU">
    <img src="https://img.shields.io/badge/Join-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Server"/>
  </a>
  <a href="https://github.com/bniladridas/path/issues">
    <img src="https://img.shields.io/badge/Issues-Find%20Help-gray?style=for-the-badge&logo=github" alt="GitHub Issues"/>
  </a>
</p>

# Path: AI-Powered Media Exploration 🚀

An intelligent media exploration ecosystem powered by **Google Gemini 2.5**. Path bridges the gap between high-level web exploration and low-level terminal efficiency.

> [!TIP]
> **New to Path?** Join our [Discord Server](https://discord.gg/J8DetsWcqU) for instant setup support and community tips.

---

## 🌟 Why Path?

Most AI tools are either purely web-based or strictly CLI. **Path** provides a unified experience:

- **Web App**: For visual, browser-based deep dives.
- **Harper CLI**: A high-performance Rust TUI for developers who live in the terminal.

### Key Features

- **Contextual Search**: Powered by Gemini 2.5 Flash for lightning-fast, accurate results.
- **Media Generation**: Integrated Image Generation using Gemini 2.5 Flash Image.
- **Harper TUI**: Interactive terminal interface built with `ratatui` for maximum speed.
- **Hybrid Architecture**: Flask-based backend with a standalone Rust binary.

---

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.8+** | **Node.js 16+** | **Rust 1.75+**

### 1. Web Application (The Core)

```bash
# Clone and enter
git clone https://github.com/bniladridas/path.git
cd path

# Install dependencies
pip install -r requirements.txt
npm install

# Environment Config
cp .env.example .env
# Open .env and add your GEMINI_API_KEY

```

### 2. Harper CLI (Global Installation)

To run `harper tui` from any directory, follow these steps:

```bash
# Build the optimized binary
cd rust
cargo build --release

# Install to local bin
mkdir -p ~/.local/bin
cp target/release/harper ~/.local/bin/
chmod +x ~/.local/bin/harper

# Sync your API key for global use
echo "GEMINI_API_KEY=$(grep GEMINI_API_KEY ../.env | cut -d '=' -f2)" > ~/.harper.env

```

_Note: Ensure `~/.local/bin` is in your `$PATH`. If not, add `export PATH="$HOME/.local/bin:$PATH"` to your `.zshrc` or `.bashrc`._

---

## 🚀 Usage

### Terminal Workflows (Harper)

| Command                       | Action                               |
| ----------------------------- | ------------------------------------ |
| `harper tui`                  | Open the **Interactive Terminal UI** |
| `harper search "..."`         | Quick terminal-based search          |
| `harper image --prompt "..."` | Generate imagery directly from CLI   |

### Web Exploration

Run `python run.py` and navigate to `http://localhost:8000`.

---

## 🧰 Tech Stack

### Backend & AI

- **Flask 3.1.2**: Core web framework.
- **Google GenAI SDK**: Powering the Gemini 2.5 integration.
- **Gunicorn**: Production-grade WSGI server.

### CLI (Harper)

- **Rust**: High-performance core logic.
- **Ratatui**: Advanced terminal UI rendering.
- **Crossterm**: Cross-platform terminal manipulation.

---

## 🤝 Community & Support

- **Discord**: [Join the conversation](https://discord.gg/J8DetsWcqU)
- **Issues**: [Report a bug or request a feature](https://github.com/bniladridas/path/issues)
- **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

<p align="center">
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel" alt="Vercel">
<img src="https://img.shields.io/badge/CircleCI-343434?style=for-the-badge&logo=circleci" alt="CircleCI">
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions" alt="GitHub Actions">
</p>
