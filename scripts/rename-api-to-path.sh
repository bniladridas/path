#!/bin/bash

# Rename API directory to PATH
# This script renames the api/ directory to path/ and updates all references
# Usage: ./scripts/rename-api-to-path.sh

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

print_status "Starting rename from 'api' to 'path'..."

# Check if api directory exists
if [ ! -d "api" ]; then
    print_error "api/ directory not found!"
    exit 1
fi

# 1. Rename the directory
print_status "1. Renaming api/ directory to path/..."
mv api path

# 2. Update vercel.json
print_status "2. Updating vercel.json..."
sed -i.bak 's|api/|path/|g' vercel.json
sed -i.bak 's|/api/index|/path/index|g' vercel.json

# 3. Update scripts/deploy-api.sh
print_status "3. Updating scripts/deploy-api.sh..."
sed -i.bak 's|/api directory|/path directory|g' scripts/deploy-api.sh
sed -i.bak 's|api/|path/|g' scripts/deploy-api.sh

# 4. Update scripts/prepare-deployment.py
print_status "4. Updating scripts/prepare-deployment.py..."
sed -i.bak 's|/api directory|/path directory|g' scripts/prepare-deployment.py
sed -i.bak 's|api/|path/|g' scripts/prepare-deployment.py
sed -i.bak 's|self\.api_dir|self.path_dir|g' scripts/prepare-deployment.py
sed -i.bak 's|api_dir|path_dir|g' scripts/prepare-deployment.py
sed -i.bak 's|api_templates|path_templates|g' scripts/prepare-deployment.py
sed -i.bak 's|api_static|path_static|g' scripts/prepare-deployment.py

# 5. Update .gitignore
print_status "5. Updating .gitignore..."
sed -i.bak 's|api/templates/|path/templates/|g' .gitignore
sed -i.bak 's|api/static/|path/static/|g' .gitignore

# 6. Update docs/DEPLOYMENT.md
print_status "6. Updating docs/DEPLOYMENT.md..."
sed -i.bak 's|api/|path/|g' docs/DEPLOYMENT.md
sed -i.bak 's|/api|/path|g' docs/DEPLOYMENT.md

# 7. Update README.md
print_status "7. Updating README.md..."
sed -i.bak 's|`api/`|`path/`|g' README.md

# 8. Update vercel_build.sh
print_status "8. Updating vercel_build.sh..."
sed -i.bak 's|/api/|/path/|g' vercel_build.sh

# 9. Rename the deploy script itself
print_status "9. Renaming deploy-api.sh to deploy-path.sh..."
mv scripts/deploy-api.sh scripts/deploy-path.sh

# 10. Update the renamed script's internal references
print_status "10. Updating deploy-path.sh internal references..."
sed -i.bak 's|API Deployment Script|PATH Deployment Script|g' scripts/deploy-path.sh
sed -i.bak 's|API deployment|PATH deployment|g' scripts/deploy-path.sh
sed -i.bak 's|API directory|PATH directory|g' scripts/deploy-path.sh
sed -i.bak 's|deploy-api.sh|deploy-path.sh|g' scripts/deploy-path.sh

# 11. Clean up backup files
print_status "11. Cleaning up backup files..."
find . -name "*.bak" -delete

# 12. Verify the changes
print_status "12. Verifying the rename..."
if [ -d "path" ] && [ ! -d "api" ]; then
    print_status "✓ Directory renamed successfully"
else
    print_error "✗ Directory rename failed"
    exit 1
fi

# Check if key files exist
if [ -f "path/app.py" ] && [ -f "path/index.py" ]; then
    print_status "✓ Core path files exist"
else
    print_error "✗ Core path files missing"
    exit 1
fi

# Test the deployment script
print_status "13. Testing deployment preparation..."
python3 scripts/prepare-deployment.py vercel

if [ -d "path/templates" ] && [ -d "path/static" ]; then
    print_status "✓ Deployment preparation works"
else
    print_error "✗ Deployment preparation failed"
    exit 1
fi

print_status "🎉 Successfully renamed 'api' to 'path'!"
print_status ""
print_status "Changes made:"
print_status "  - Renamed api/ directory to path/"
print_status "  - Updated vercel.json routing"
print_status "  - Updated all deployment scripts"
print_status "  - Updated documentation"
print_status "  - Updated .gitignore"
print_status "  - Renamed deploy-api.sh to deploy-path.sh"
print_status ""
print_status "Next steps:"
print_status "  1. Test locally: python app_local.py"
print_status "  2. Test deployment: python scripts/prepare-deployment.py all"
print_status "  3. Commit changes: git add . && git commit -m 'refactor: rename api directory to path'"
