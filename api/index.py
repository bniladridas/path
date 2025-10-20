# Ensure all dependencies are available
try:
    from app import app
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.in"])
    from app import app

# Import requests after ensuring app is available
import requests  # noqa: F401

# This file is required for Vercel to properly deploy the Python application
# It serves as the entry point for the Vercel Python runtime
application = app  # Make the app available as application for WSGI

# The application will be served at the root URL (/) as defined in vercel.json
