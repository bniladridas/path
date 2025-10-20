"""
Basic tests for the Flask app.
"""

import os
import sys

from api.app import app as flask_app

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


def test_app_creation():
    """Test that the Flask app can be created."""
    assert flask_app is not None
    assert flask_app.name == "api.app"


def test_index_route():
    """Test the index route."""
    with flask_app.test_client() as client:
        response = client.get("/")
        assert response.status_code in [200, 302]  # 302 for redirect to verify


def test_terms_route():
    """Test the terms route."""
    with flask_app.test_client() as client:
        response = client.get("/terms")
        assert response.status_code == 200


def test_privacy_route():
    """Test the privacy route."""
    with flask_app.test_client() as client:
        response = client.get("/privacy")
        assert response.status_code == 200


def test_updates_route():
    """Test the updates route."""
    with flask_app.test_client() as client:
        response = client.get("/updates")
        assert response.status_code == 200
