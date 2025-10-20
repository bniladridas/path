#!/bin/bash
set -e

# Install dependencies to a temporary directory
TMP_DIR=$(mktemp -d)
pip install -r requirements.txt --target $TMP_DIR

# Copy all files to the function directory
cp -R $TMP_DIR/* /var/task/

# Create a path file to ensure Python can find our modules
echo "/var/task" > /var/task/python_path.pth

# Make sure the script is executable
chmod +x /var/task/api/index.py
