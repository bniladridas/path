#!/bin/bash

# Cleanup script to find and optionally remove unused code
# Usage: ./scripts/cleanup.sh [--fix]

# Don't exit on errors, we want to run all checks
set +e

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

FIX_MODE=false
if [[ "$1" == "--fix" ]]; then
    FIX_MODE=true
    print_warning "Fix mode enabled - will attempt to remove unused code"
fi

print_status "Running unused code detection..."

# 1. Check with our custom script
print_status "1. Running custom unused code detector..."
python3 scripts/check-unused.py || true

# 2. Check with vulture (if available)
if command -v vulture &> /dev/null; then
    print_status "2. Running vulture (dead code detector)..."
    vulture . --exclude=venv,node_modules,.git --min-confidence 80
else
    print_warning "vulture not installed, skipping dead code detection"
fi

# 3. Check with unimport (if available)
if command -v unimport &> /dev/null; then
    print_status "3. Running unimport (unused import detector)..."
    if [[ "$FIX_MODE" == true ]]; then
        unimport --remove-all --exclude=venv,node_modules,.git .
    else
        unimport --check --exclude=venv,node_modules,.git .
    fi
else
    print_warning "unimport not installed, skipping unused import detection"
fi

# 4. Check with ruff for unused imports
print_status "4. Running ruff for unused imports..."
if [[ "$FIX_MODE" == true ]]; then
    ruff check --select F401 --fix .
else
    ruff check --select F401 .
fi

# 5. Find potentially unused files
print_status "5. Checking for potentially unused files..."
find . -name "*.py" -type f \
    -not -path "./venv/*" \
    -not -path "./.git/*" \
    -not -path "./node_modules/*" \
    -not -path "./.pytest_cache/*" \
    -exec sh -c 'if [ $(wc -l < "$1") -lt 5 ]; then echo "Small file: $1"; fi' _ {} \;

print_status "Cleanup analysis complete!"

if [[ "$FIX_MODE" == false ]]; then
    print_status "Run with --fix to automatically remove unused imports"
fi
