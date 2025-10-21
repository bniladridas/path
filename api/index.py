"""
Simple Vercel serverless function for testing.
Updated to trigger new deployment.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Vercel! Flask app is working."


@app.route("/test")
def test():
    return "Test route is working."


# For Vercel serverless functions
def handler(request):
    return app(request.environ, lambda status, headers: None)  # noqa: ARG005


# Also export as application for compatibility
application = app
