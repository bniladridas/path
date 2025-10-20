"""
Docker entry point for the path application.
Imports the Flask app from app_local.py for Gunicorn compatibility.
"""

from app_local import app

if __name__ == "__main__":
    app.run()
