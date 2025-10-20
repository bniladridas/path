#!/bin/bash
set -e

# Create the target directory if it doesn't exist
mkdir -p /var/task

# Install dependencies directly to the target directory
pip install -r requirements.txt --target /var/task

# Create a .pth file to ensure Python can find our modules
echo "/var/task" > /var/task/site-packages.pth

# Copy our application code
cp -r . /var/task/

# Make sure the API handler is executable
chmod +x /var/task/path/index.py
