#!/bin/bash
set -e

# Create a temporary directory for dependencies
TMP_DIR=$(mktemp -d)

# Install all dependencies
pip install -r requirements.txt --target $TMP_DIR

# Copy all dependencies to the function directory
cp -R $TMP_DIR/* /var/task/ || true

# Create a path file to ensure Python can find our modules
echo "/var/task" > /var/task/python_path.pth

# Install dependencies directly to the function directory
pip install -r requirements.txt --target /var/task
