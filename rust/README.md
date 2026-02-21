# Harper CLI

Native CLI for Harper - AI-powered media exploration.

## Install

```bash
cd rust
cargo build --release
cp target/release/harper ~/.local/bin/harper
```

Set `GEMINI_API_KEY` in `.env`:
```bash
cp .env.example .env
# Edit .env with your API key from https://aistudio.google.com/app/apikey
```

## Usage

```bash
# TUI (interactive)
harper tui

# Command line search
harper search "best sci-fi movies"

# Generate image
harper image --prompt "a sunset"
```

## TUI Controls

- **Type** - Start searching
- **Enter** - Submit query
- **Esc** - Clear or quit
