"""
Vercel Python Serverless Function Entry Point.

This file is required for Vercel to properly deploy the Python application.
It serves as the entry point for the Vercel Python runtime.
"""

import sys
from pathlib import Path

# Add the current directory to Python path to ensure app.py can be found
current_dir = str(Path(__file__).parent.absolute())
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from app import app  # noqa: E402

# Make the app available as application for WSGI
application = app
