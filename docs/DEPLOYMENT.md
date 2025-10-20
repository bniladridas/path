# Deployment Guide

This project supports multiple deployment targets with automated file preparation.

## Deployment Targets

### 1. Vercel (Serverless)
- **Entry Point**: `path/index.py`
- **Static Files**: Copied to `path/static/`
- **Templates**: Copied to `path/templates/`

### 2. Docker (Containerized)
- **Entry Point**: `app_local.py` via `app.py`
- **Static Files**: Root `static/`
- **Templates**: Root `templates/`

### 3. Local Development
- **Entry Point**: `app_local.py`
- **Static Files**: Root `static/`
- **Templates**: Root `templates/`

## File Structure

```
project/
├── app_local.py          # Main Flask app (local/Docker)
├── app.py               # Docker entry point
├── templates/           # Source templates
├── static/              # Source static files
├── path/
│   ├── app.py          # Vercel Flask app
│   ├── index.py        # Vercel entry point
│   ├── templates/      # Generated (ignored by git)
│   └── static/         # Generated (ignored by git)
└── scripts/
    ├── deploy-api.sh           # Bash deployment script
    └── prepare-deployment.py   # Python deployment script
```

## Deployment Scripts

### Quick Deploy (Bash)
```bash
# Prepare for Vercel deployment
./scripts/deploy-api.sh
```

### Advanced Deploy (Python)
```bash
# Prepare for specific target
python scripts/prepare-deployment.py vercel
python scripts/prepare-deployment.py docker
python scripts/prepare-deployment.py local

# Prepare for all targets
python scripts/prepare-deployment.py all
```

## Automated Deployment

### Vercel
- **Trigger**: Push to main branch
- **Build Command**: `python scripts/prepare-deployment.py vercel`
- **Files**: Automatically copies templates and static files to `/path`

### Docker
- **Trigger**: GitHub Actions on push/PR
- **Build**: Uses root files directly
- **Registry**: Pushes to GHCR and Docker Hub

## Manual Deployment

### Vercel CLI
```bash
# Prepare files
python scripts/prepare-deployment.py vercel

# Deploy
vercel --prod
```

### Docker
```bash
# Build image
docker build -t path-app .

# Run locally
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key path-app
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment
export GEMINI_API_KEY=your_key

# Run app
python app_local.py
```

## File Synchronization

The deployment scripts ensure that:
- **Source of truth**: Root `templates/` and `static/` directories
- **Generated files**: `path/templates/` and `path/static/` (git ignored)
- **No duplication**: Files are copied during deployment, not stored twice

## Environment Variables

All deployment targets require:
- `GEMINI_API_KEY`: Google Gemini API key for AI functionality

## Troubleshooting

### Missing Files Error
```bash
# Regenerate API files
python scripts/prepare-deployment.py vercel
```

### Template Not Found
- Ensure root `templates/` directory exists
- Run deployment preparation script
- Check file permissions

### Static Files Not Loading
- Verify `static/css/style.css` exists in root
- Run deployment preparation script
- Check Vercel static file routing
