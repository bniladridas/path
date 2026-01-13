# PATH

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/bniladridas/path)

A Flask web application that helps people find their way home through media exploration using Google's Gemini 2.5-flash AI model.

## Core Philosophy
- **Authentic discovery**: No manipulation, just honest responses
- **Human longing**: Honoring deeper needs behind every search
- **Time is precious**: Cutting through noise to find what matters
- **Coming home**: Helping people reconnect with themselves

## Features
- AI-powered media recommendations using Gemini 2.5-flash
- Human verification to ensure authentic interactions
- Clean, distraction-free interface
- Session-based verification for privacy
- OpenAPI documentation for API access
- Deployable on Vercel

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bniladridas/path.git
cd path
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key_here
FLASK_DEBUG=1  # for development
```

## Usage

### Local Development
```bash
python app.py
```
Open http://127.0.0.1:8000 in your browser.

### API Endpoints
- `GET /` - Main application interface
- `POST /search` - AI-powered search
- `GET /status` - Health check
- `GET /terms`, `/privacy`, `/updates` - Static pages

### Human Verification
Users must complete a simple verification challenge before accessing the search functionality.

## Deployment
This application is configured for deployment on Vercel. The `index.py` file serves as the serverless function entry point.

## Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.

## License
[Specify your license here]

## Author
Niladri Das (@bniladridas)
