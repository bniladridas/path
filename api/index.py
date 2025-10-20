from app import app

# This file is required for Vercel to properly deploy the Python application
# It serves as the entry point for the Vercel Python runtime
application = app  # Make the app available as application for WSGI

# The application will be served at the root URL (/) as defined in vercel.json
