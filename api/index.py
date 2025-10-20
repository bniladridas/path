"""
Vercel Python Serverless Function Entry Point.

This file is required for Vercel to properly deploy the Python application.
It serves as the entry point for the Vercel Python runtime.
"""

# Try to import the Flask app
try:
    from app import app

    # Check if requests is available
    try:
        import requests  # noqa: F401
    except ImportError:
        # If requests is not available, try to use the vendored version
        try:
            import sys
            from pathlib import Path

            sys.path.append(str(Path(__file__).parent))
            # Import the module but don't assign it to avoid unused import warning
            from requests_vendor import requests as _  # noqa: F401
        except ImportError as vendor_err:
            error_msg = (
                "The 'requests' module is not available. Please ensure all dependencies are included in your deployment."
            )
            raise ImportError(error_msg) from vendor_err
except Exception as error:
    # Create a simple error handler app if the main app fails to import
    from flask import Flask, jsonify

    app = Flask(__name__)
    error_message = str(error)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def error_handler(_):
        return jsonify({"error": "Failed to initialize application", "message": error_message}), 500


# Make the app available as application for WSGI
application = app
