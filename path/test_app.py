"""
Simple test Flask app for Vercel debugging.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Vercel! Flask app is working."


@app.route("/test")
def test_route():
    """Test route to verify app functionality."""
    return "Test route is working."


# For Vercel
application = app

if __name__ == "__main__":
    app.run(debug=False)  # nosec B201
