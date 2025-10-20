"""
Vercel Python Serverless Function Entry Point.

This file is required for Vercel to properly deploy the Python application.
It serves as the entry point for the Vercel Python runtime.
"""

import sys
from pathlib import Path

# Local application imports
from api.app import app  # noqa: E402

# Add the current directory to Python path to ensure app.py can be found
CURRENT_DIR = str(Path(__file__).parent.absolute())
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Make the app available as application for WSGI
application = app
