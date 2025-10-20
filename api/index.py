"""
Vercel Python Serverless Function Entry Point.

This file is required for Vercel to properly deploy the Python application.
It serves as the entry point for the Vercel Python runtime.
"""

# Import the Flask app from the local app.py
from app import app

# Make the app available as application for WSGI
application = app
