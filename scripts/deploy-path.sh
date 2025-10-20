#!/bin/bash

# PATH Deployment Script
# Copies necessary files to /path directory for Vercel deployment
# Usage: ./scripts/deploy-path.sh

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_status "Starting PATH deployment preparation..."

# Ensure api directory exists
mkdir -p api

# Copy templates
print_status "Copying templates to path/templates/..."
rm -rf path/templates
cp -r templates path/templates

# Copy static files
print_status "Copying static files to path/static/..."
rm -rf path/static
cp -r static path/static

# Verify core API files exist
if [ ! -f "path/app.py" ]; then
    print_error "path/app.py not found! This is required for Vercel deployment."
    exit 1
fi

if [ ! -f "path/index.py" ]; then
    print_error "path/index.py not found! This is required for Vercel deployment."
    exit 1
fi

# Check if files were copied successfully
TEMPLATE_COUNT=$(find path/templates -name "*.html" | wc -l)
CSS_COUNT=$(find path/static -name "*.css" | wc -l)

print_status "Deployment preparation complete!"
print_status "  - Templates copied: $TEMPLATE_COUNT HTML files"
print_status "  - Static files copied: $CSS_COUNT CSS files"

# Verify critical files
print_status "Verifying API structure..."
if [ -d "path/templates" ] && [ -d "path/static" ] && [ -f "path/app.py" ]; then
    print_status "PATH directory structure is ready for Vercel deployment"
else
    print_error "PATH directory structure is incomplete"
    exit 1
fi

print_status "PATH deployment preparation successful!"
