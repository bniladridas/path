"""
Vercel Python Serverless Function Entry Point.

This file is required for Vercel to properly deploy the Python application.
It serves as the entry point for the Vercel Python runtime.
"""

import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.absolute()))

# Try to import the Flask app
try:
    from app import app
except ImportError:
    # Create a simple error handler app if the main app fails to import
    from flask import Flask, jsonify

    app = Flask(__name__)
    error_message = "Failed to import the main application"

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def error_handler(_):
        return jsonify({"error": "Failed to initialize application", "message": error_message}), 500


# Make the app available as application for WSGI
application = app
