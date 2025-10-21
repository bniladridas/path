#!/bin/bash

# Vercel Deployment Validation Script
# Run this locally before pushing to validate your code will work on Vercel

set -e

echo "🚀 Vercel Deployment Validation"
echo "==============================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "vercel.json" ]; then
    print_error "vercel.json not found. Please run this script from the project root."
    exit 1
fi

print_status "Checking project structure..."

# Validate vercel.json
print_status "Validating vercel.json..."
if python -m json.tool vercel.json > /dev/null 2>&1; then
    print_success "vercel.json is valid JSON"
else
    print_error "vercel.json is invalid JSON"
    exit 1
fi

# Check for api directory
if [ -d "api" ]; then
    print_success "api directory exists"
else
    print_error "api directory not found"
    exit 1
fi

# Check for Python files in api
if ls api/*.py > /dev/null 2>&1; then
    print_success "Python files found in api directory"
else
    print_error "No Python files found in api directory"
    exit 1
fi

# Test Python environment
print_status "Testing Python environment..."
python_version=$(python --version 2>&1)
print_success "Python version: $python_version"

# Install dependencies
print_status "Installing dependencies..."
if pip install -r requirements.txt > /dev/null 2>&1; then
    print_success "Dependencies installed successfully"
else
    print_error "Failed to install dependencies"
    exit 1
fi

# Test Flask app import
print_status "Testing Flask app import..."
cd api
if python -c "from index import app; print('Flask app imported successfully')" > /dev/null 2>&1; then
    print_success "Flask app imports correctly"
else
    print_error "Failed to import Flask app"
    cd ..
    exit 1
fi

# Test Flask app routes
print_status "Testing Flask app routes..."
python -c "
from index import app
with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200, f'Home route failed: {response.status_code}'

    response = client.get('/test')
    assert response.status_code == 200, f'Test route failed: {response.status_code}'

print('All routes working correctly')
" 2>/dev/null

if [ $? -eq 0 ]; then
    print_success "All routes tested successfully"
else
    print_error "Route testing failed"
    cd ..
    exit 1
fi

cd ..

# Check for common issues
print_status "Checking for common issues..."

# Check for debug mode
if grep -r "debug=True" api/ --include="*.py" > /dev/null 2>&1; then
    print_warning "debug=True found in code - this should be disabled for production"
fi

# Check for hardcoded secrets
if grep -r -i "api_key.*=" api/ --include="*.py" | grep -v "environ\|getenv" > /dev/null 2>&1; then
    print_warning "Potential hardcoded API keys found"
fi

# Check static files
if [ -d "static" ]; then
    print_success "Static files directory found"
    static_count=$(find static -type f | wc -l)
    print_status "Static files count: $static_count"
fi

# Check templates
if [ -d "templates" ]; then
    print_success "Templates directory found"
    template_count=$(find templates -name "*.html" | wc -l)
    print_status "Template files count: $template_count"
fi

# Performance test
print_status "Running basic performance test..."
cd api
python -c "
import time
from index import app

start_time = time.time()
with app.test_client() as client:
    response = client.get('/')
end_time = time.time()

response_time = (end_time - start_time) * 1000
print(f'Response time: {response_time:.2f}ms')

if response_time > 1000:
    print('Warning: Response time is slow')
else:
    print('Response time is acceptable')
" 2>/dev/null

cd ..

echo ""
print_success "🎉 All validation checks passed!"
print_status "Your code is ready for Vercel deployment."
echo ""
print_status "Next steps:"
echo "  1. git add ."
echo "  2. git commit -m 'your commit message'"
echo "  3. git push"
echo ""
print_status "Vercel will automatically deploy your changes."
