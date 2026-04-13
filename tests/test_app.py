"""
Basic tests for the Flask app.
"""

import os
import sys
from unittest.mock import MagicMock
from unittest.mock import patch

from packages.core.search import app as flask_app

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


def test_app_creation():
    """Test that the Flask app can be created."""
    assert flask_app is not None
    assert flask_app.name == "packages.core.search"


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


# =============================================================================
# VERIFICATION FLOW TESTS
# =============================================================================


def test_verify_get():
    """Test verification page is displayed on GET request."""
    with flask_app.test_client() as client:
        response = client.get("/verify")
        assert response.status_code == 200


def test_verify_post_correct_answer():
    """Test verification succeeds with correct answer."""
    with flask_app.test_client() as client:
        response = client.post("/verify", data={"answer": "box"}, follow_redirects=False)
        assert response.status_code == 302
        assert response.location == "/"


def test_verify_post_incorrect_answer():
    """Test verification fails with incorrect answer."""
    with flask_app.test_client() as client:
        response = client.post("/verify", data={"answer": "wronganswer"}, follow_redirects=False)
        assert response.status_code == 200
        assert b"incorrect" in response.data.lower() or b"try again" in response.data.lower()


def test_verify_post_empty_answer():
    """Test verification fails with empty answer."""
    with flask_app.test_client() as client:
        response = client.post("/verify", data={"answer": ""}, follow_redirects=False)
        assert response.status_code == 200


def test_bypass_verification():
    """Test verification bypass endpoint."""
    with flask_app.test_client() as client:
        response = client.get("/bypass-verification", follow_redirects=True)
        assert response.status_code == 200
        with client.session_transaction() as sess:
            assert sess.get("verified") is True


# =============================================================================
# AUTH/SESSION TESTS
# =============================================================================


def test_index_redirects_unverified_user():
    """Test that unverified users are redirected to verification."""
    with flask_app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 302
        assert "/verify" in response.location


def test_index_allows_verified_user():
    """Test that verified users can access index."""
    with flask_app.test_client() as client:
        with client.session_transaction() as sess:
            sess["verified"] = True
        response = client.get("/")
        assert response.status_code == 200


def test_search_requires_verification():
    """Test that search endpoint requires verification."""
    with flask_app.test_client() as client:
        response = client.post("/search", data={"query": "test"})
        assert response.status_code == 200
        data = response.get_json()
        assert "error" in data or "verification" in data.get("result", "").lower()


def test_search_allows_verified_user():
    """Test that verified users can access search endpoint."""
    with flask_app.test_client() as client:
        with client.session_transaction() as sess:
            sess["verified"] = True
        with patch("packages.core.search.genai") as mock_genai:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.text = '{"candidates": [{"content": {"parts": [{"text": "Test response"}]}}]}'
            mock_client.models.generate_content.return_value = mock_response
            mock_genai.Client.return_value = mock_client
            response = client.post("/search", data={"query": "test book"})
            assert response.status_code == 200
            data = response.get_json()
            assert "result" in data


def test_search_missing_query():
    """Test search endpoint with missing query."""
    with flask_app.test_client() as client:
        with client.session_transaction() as sess:
            sess["verified"] = True
        with patch("packages.core.search.genai") as mock_genai:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.text = '{"candidates": [{"content": {"parts": [{"text": "Empty query response"}]}}]}'
            mock_client.models.generate_content.return_value = mock_response
            mock_genai.Client.return_value = mock_client
            response = client.post("/search", data={"query": ""})
            assert response.status_code == 200
            data = response.get_json()
            assert "result" in data


# =============================================================================
# ERROR HANDLING TESTS
# =============================================================================


def test_status_endpoint():
    """Test the status endpoint returns healthy."""
    with flask_app.test_client() as client:
        response = client.get("/status")
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("status") == "healthy"


def test_image_page_redirects_unverified():
    """Test image page redirects unverified users."""
    with flask_app.test_client() as client:
        response = client.get("/image")
        assert response.status_code == 302
        assert "/verify" in response.location


def test_image_page_allows_verified_user():
    """Test verified users can access image page."""
    with flask_app.test_client() as client:
        with client.session_transaction() as sess:
            sess["verified"] = True
        response = client.get("/image")
        assert response.status_code == 200


def test_menu_page_allowed():
    """Test menu page with allowed page name."""
    with flask_app.test_client() as client:
        response = client.get("/menu/about")
        assert response.status_code == 200


def test_menu_page_blocked():
    """Test menu page blocks disallowed page names."""
    with flask_app.test_client() as client:
        response = client.get("/menu/invalid")
        assert response.status_code == 404


def test_generate_image_requires_verification():
    """Test image generation requires verification."""
    with flask_app.test_client() as client:
        response = client.post("/generate-image", json={"prompt": "test"})
        assert response.status_code == 401
        data = response.get_json()
        assert "verification" in data.get("error", "").lower()
