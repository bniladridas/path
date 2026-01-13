# NOTE: To reduce duplication, consider consolidating into one app with env-based config.

"""
"Path" serves both as the app's name and its guiding metaphor.
The project helps users "find their path" through media exploration
like a guide on a personal journey.

In the codebase, `path/` is the main Python package containing the application logic (e.g., app.py).
The name follows the standard convention where the package name matches the project title.
Note: it's not a filesystem path reference, but a conceptual one—symbolizing user discovery.

A Flask web application that helps people find their way home through
media exploration using Google's Gemini 2.5-flash AI model.

Core Philosophy:
- Authentic discovery: No manipulation, just honest responses
- Human longing: Honoring deeper needs behind every search
- Time is precious: Cutting through noise to find what matters
- Coming home: Helping people reconnect with themselves

Author: Niladri Das (@bniladridas)
Repository: https://github.com/bniladridas/path
"""
# Trigger CI 3

# Standard library imports
import logging
import os
import re
import secrets
import subprocess  # nosec B404
import sys
from pathlib import Path

import requests

# Third-party imports
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_openapi3.models.info import Info
from flask_openapi3.models.tag import Tag
from flask_openapi3.openapi import OpenAPI
from pydantic import BaseModel

# Add the project root to Python path to ensure shared modules can be imported
PROJECT_ROOT = str(Path(__file__).parent.parent)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Local application imports (after path setup)
try:
    from shared.errors import get_ai_unavailable_message
    from shared.errors import get_api_error_message
    from shared.errors import get_internal_error_message
    from shared.errors import get_rate_limit_error_message
    from shared.prompts import SYSTEM_PROMPT
    from shared.requests_fallback import setup_requests_fallback
    from shared.verification import is_verification_answer_valid

    # Set up requests fallback
    setup_requests_fallback()
except ImportError:
    # If shared module is not available, continue without fallback
    pass


# Try to import Google GenAI
try:
    from google import genai

    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    GENAI_AVAILABLE = False

# ============================================================================
# APPLICATION INITIALIZATION
# ============================================================================

# Environment variables are loaded from Vercel environment in production
# For local development, ensure .env file is present
if not os.environ.get("VERCEL"):
    from dotenv import load_dotenv

    load_dotenv()

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("PATH app starting...")


def get_version():
    """
    Get the current version from git tags.
    Falls back to '1.0.0' if git is not available.
    """
    try:
        # Get the latest tag
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"], capture_output=True, text=True, cwd=PROJECT_ROOT, check=False
        )  # nosec B603 B607
        if result.returncode == 0:
            version = result.stdout.strip()
            # Remove 'v' prefix if present
            if version.startswith("v"):
                version = version[1:]
            return version
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    return "1.0.0"


# Initialize OpenAPI application instance
# OpenAPI will serve our web interface and handle HTTP requests with API documentation
info = Info(title="PATH API", version=get_version(), description="AI-powered media exploration API")
app = OpenAPI(
    __name__,
    info=info,
    template_folder=os.path.join(PROJECT_ROOT, "templates"),
    static_folder=os.path.join(PROJECT_ROOT, "static"),
)

# Set a secret key for session management
# This key is used to encrypt session data and maintain user verification state
# Use environment variable if available, otherwise generate a random key for development
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(16)

# Get Gemini API key from environment variable
# The API key authenticates our requests to Google's Gemini AI service
# This must be set in the .env file or environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
logging.info("GEMINI_API_KEY set: %s", bool(GEMINI_API_KEY))

# Initialize Gemini if available
if GENAI_AVAILABLE and GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)  # type: ignore[attr-defined]

# Define the Gemini model to use
# This constant makes it easy to update the model in the future
GEMINI_MODEL = "2.5-flash"


# API Models for OpenAPI documentation
class SearchRequest(BaseModel):
    """Request model for search queries."""

    query: str


class APIResponse(BaseModel):
    """Response model for successful search results."""

    result: str


class ErrorResponse(BaseModel):
    """Response model for error conditions."""

    result: str
    error: str
    error_type: str


# Tags for organizing endpoints
search_tag = Tag(name="Search", description="Media search and AI recommendations")
auth_tag = Tag(name="Authentication", description="User verification and access")
info_tag = Tag(name="Information", description="Static pages and information")
status_tag = Tag(name="Status", description="System status and health checks")


# ============================================================================
# API ENDPOINTS - PROGRAMMATIC ACCESS
# ============================================================================


@app.get(
    "/status",
    summary="Get system status",
    description="Check if the API is running and healthy",
    tags=[status_tag],
    responses={200: {"description": "API is healthy"}},
)
def get_status():
    """
    STATUS ENDPOINT - Health check for the API

    Returns basic system information without requiring verification.
    Useful for monitoring and load balancer health checks.

    Returns:
        JSON: Status information
    """
    return jsonify({"status": "healthy", "version": get_version(), "service": "PATH Media Exploration API"})


# ============================================================================
# ROUTE HANDLERS - WEB INTERFACE ENDPOINTS
# ============================================================================


@app.route("/")
def index():
    """
    HOME PAGE ROUTE - Main interface for path application

    This is the primary entry point for users. It implements a verification-first
    approach to ensure human users while providing a clean, distraction-free
    interface for media exploration.

    Security Flow:
    1. Check if user has completed human verification
    2. If verified: Serve the main application interface
    3. If not verified: Redirect to human verification page

    The main interface includes:
    - Clean search input for media queries
    - Three-dot menu with comprehensive tools
    - Theme customization system
    - Keyboard shortcuts for power users

    Returns:
        Flask Response: Either the main interface (index.html) or redirect to verification
    """
    # Check session for verification status
    # Session data is encrypted and stored client-side for privacy
    if session.get("verified"):
        # User has completed verification - serve main application
        return render_template("index.html")
    # User needs verification - redirect to human verification page
    return redirect(url_for("verify_human"))


@app.route("/verify")
def verify_human():
    """
    HUMAN VERIFICATION PAGE - Display verification challenge

    Serves the human verification interface to distinguish real users from bots.
    This is path's approach to maintaining a human-centered community while
    preventing automated access that could degrade the experience.

    Verification Philosophy:
    - Simple image description task
    - Accessible to humans of all technical levels
    - Respectful of user time and intelligence
    - Gmail users can bypass for streamlined access

    Returns:
        Flask Response: Rendered verification page (verify.html)
    """
    return render_template("verify.html")


@app.route("/verify", methods=["POST"])
def process_verification():
    """
    VERIFICATION PROCESSING - Handle verification form submission

    Processes the user's response to the verification challenge and determines
    if they should be granted access to the main application.

    Verification Logic:
    1. Extract user's answer from form submission
    2. Normalize answer to lowercase for case-insensitive matching
    3. Check against expected keywords for the verification image
    4. Grant access if answer contains relevant keywords
    5. Show error message if verification fails

    Security Considerations:
    - Keywords are broad enough to accept various valid descriptions
    - Case-insensitive matching for user convenience
    - Session-based verification state (encrypted client-side)
    - Graceful error handling with helpful feedback

    Returns:
        Flask Response: Redirect to home page (success) or verification page with error
    """
    # Extract the user's answer from the form submission
    # Default to empty string if no answer provided, convert to lowercase for matching
    answer = request.form.get("answer", "").lower()

    # Check if the user's answer contains valid keywords
    if is_verification_answer_valid(answer):
        # Verification successful - set session flag and redirect to main application
        session["verified"] = True
        return redirect(url_for("index"))
    # Verification failed - show error message and allow retry
    # Error message is intentionally gentle and encouraging
    return render_template("verify.html", error="incorrect answer. please try again.")


@app.route("/bypass-verification")
def bypass_verification():
    """
    DEVELOPMENT BYPASS - Skip verification for testing and development

    Provides a direct route to bypass human verification during development
    and testing phases. This endpoint should be used carefully in production
    environments and could be disabled for enhanced security.

    Use Cases:
    - Local development and testing
    - Automated testing scenarios
    - Quick access during development iterations
    - Gmail users with automatic verification bypass

    Security Note:
    This endpoint grants immediate access without verification. In production,
    consider implementing additional safeguards or disabling this route.

    Returns:
        Flask Response: Redirect to main application (index page)
    """
    # Set verification flag in session to grant access
    # This mimics successful completion of the verification process
    session["verified"] = True

    # Redirect to the main application interface
    return redirect(url_for("index"))


# ============================================================================
# AI PROCESSING ENDPOINT - CORE SEARCH FUNCTIONALITY
# ============================================================================


@app.post(
    "/search",
    summary="Search for media recommendations",
    description="Query the AI for media exploration and recommendations",
    tags=[search_tag],
    responses={
        200: APIResponse,
        400: ErrorResponse,
        403: ErrorResponse,
    },
)
def search():
    """
    SEARCH PROCESSING - Handle media exploration queries with AI

    This is the core endpoint that processes user queries through Google's Gemini
    2.5-flash model. It implements path's unique approach to AI interaction with
    privacy-first design and human-centered responses.

    Processing Pipeline:
    1. Verify user authentication (human verification required)
    2. Extract and validate user query from form submission
    3. Construct specialized prompt with path's personality and constraints
    4. Send request to Google Gemini API with optimized parameters
    5. Process response to remove any unwanted AI reasoning artifacts
    6. Return clean, lowercase response optimized for path's interface

    Privacy Features:
    - No conversation history stored or accessed
    - Fresh context for every interaction
    - Minimal data processing and immediate response
    - Session-based verification only

    Error Handling Philosophy:
    - Maintain curiosity and learning mindset even during errors
    - Provide encouraging, human-friendly error messages
    - Graceful degradation with system resilience
    - Transparent communication about what went wrong

    Returns:
        JSON Response: Contains either successful AI response or error information
    """
    logging.info("Search request received")
    # ========================================================================
    # AUTHENTICATION CHECK
    # ========================================================================

    # Verify that the user has completed human verification
    # This ensures only verified humans can access the AI functionality
    if not session.get("verified"):
        logging.warning("Search request denied: user not verified")
        return jsonify(
            {
                "result": "please verify that you're human before using this service.",
                "error": "not verified",
                "error_type": "verification_required",
            }
        )

    # ========================================================================
    # QUERY EXTRACTION AND VALIDATION
    # ========================================================================

    # Extract the user's query from the form submission
    # Default to empty string if no query provided
    query = request.form.get("query", "")

    # ========================================================================
    # AI PERSONALITY AND PROMPT ENGINEERING
    # ========================================================================

    # Define the system prompt that establishes path's unique AI personality
    # This prompt is carefully crafted to embody path's four core principles
    # and create a consistent, human-centered interaction experience
    system_prompt = SYSTEM_PROMPT

    if not GENAI_AVAILABLE:
        logging.error("Google Generative AI not available")
        return jsonify(
            {
                "result": get_ai_unavailable_message(),
                "error": "ai_unavailable",
                "error_type": "service_unavailable",
            }
        )

    try:
        safe_query_for_log = query[:50].replace("\n", "").replace("\r", "")
        logging.info("Processing search query: %s...", safe_query_for_log)

        # Combine system prompt and user query into a single prompt
        full_prompt = f"{system_prompt}\n\nUser query: {query}"

        # Use the new Google GenAI SDK
        logging.info("Sending request to Gemini API using SDK")

        try:
            # Generate content using the new SDK
            response = client.models.generate_content(
                model=f"gemini-{GEMINI_MODEL}",
                contents=[{"parts": [{"text": full_prompt}]}],
                config={
                    "temperature": 0.7,
                    "max_output_tokens": 1024,
                },
            )

            # Extract the result from the response
            result = response.text

        except (ConnectionError, TimeoutError, ValueError):
            logging.exception("Gemini API connection error")
            # Return a friendly error response instead of continuing without a result
            return jsonify(
                {
                    "result": get_api_error_message(),
                    "error": "connection_error",
                    "error_type": "api_error",
                }
            )
        except Exception as api_error:
            logging.exception("Gemini API unexpected error")

            # Check for rate limit errors more robustly
            # Try to get status code from exception attributes
            status_code = getattr(api_error, "code", None) or getattr(api_error, "status_code", None)
            error_msg = str(api_error).lower()

            # Determine error type and response
            if status_code == 429 or "rate limit" in error_msg or "429" in error_msg:
                error_result = get_rate_limit_error_message()
                error_type = "rate_limit"
                error_code = "rate limit"
            else:
                # For other errors, maintain the curious, learning personality
                error_result = get_api_error_message()
                error_type = "api_error"
                # Do not expose raw exception details to the client
                error_code = "internal_error"

            return jsonify(
                {
                    "result": error_result,
                    "error": error_code,
                    "error_type": error_type,
                }
            )

        # Post-process the result to remove any thinking tags or internal monologue
        # This ensures that the response doesn't include any of the model's internal
        # reasoning process
        # We use a single regular expression to match and remove different formats of thinking tags
        result = re.sub(
            r"(<think>.*?</think>|\[thinking\].*?\[/thinking\]|\(thinking\).*?\(/thinking\))",
            "",
            result,
            flags=re.DOTALL,
        )

        # Convert result to lowercase
        result = result.lower()

        # Return the processed result as JSON
        # This will be sent back to the frontend and displayed to the user
        logging.info("Search completed successfully")
        return jsonify({"result": result})
    except (
        requests.exceptions.RequestException,
        requests.exceptions.JSONDecodeError,
        KeyError,
        IndexError,
    ):
        # If any error occurs during the process, log the actual error server-side only
        # This ensures internal info is not exposed to the user
        # Frontend receives only generic error information
        logging.exception("Error in /search route")
        return jsonify(
            {
                "result": get_internal_error_message(),
                "error": "internal_error",
                "error_type": "system_error",
            }
        )


@app.route("/terms")
def terms():
    """
    Route handler for the Terms of Use page.

    Returns:
        The rendered terms.html template.
    """
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    """
    Route handler for the Privacy Policy page.

    Returns:
        The rendered privacy.html template.
    """
    return render_template("privacy.html")


@app.route("/updates")
def updates():
    """
    Route handler for the Updates page.

    Returns:
        The rendered updates.html template.
    """
    return render_template("updates.html")


@app.route("/menu/about")
def menu_about():
    """
    Route handler for the About menu content.

    Returns:
        The rendered about.html template.
    """
    return render_template("about.html")


@app.route("/menu/help")
def menu_help():
    """
    Route handler for the Help menu content.

    Returns:
        The rendered help.html template.
    """
    return render_template("help.html")


@app.route("/menu/product")
def menu_product():
    """
    Route handler for the Product menu content.

    Returns:
        The rendered product.html template.
    """
    return render_template("product.html")


@app.route("/menu/token")
def menu_token():
    """
    Route handler for the Token menu content.

    Returns:
        The rendered token.html template.
    """
    return render_template("token.html")


@app.route("/menu/protocol")
def menu_protocol():
    """
    Route handler for the Protocol menu content.

    Returns:
        The rendered protocol.html template.
    """
    return render_template("protocol.html")


@app.route("/menu/gmail")
def menu_gmail():
    """
    Route handler for the Gmail menu content.

    Returns:
        The rendered gmail.html template.
    """
    return render_template("gmail.html")


@app.route("/menu/neural-nets")
def menu_neural_nets():
    """
    Route handler for the Neural Nets menu content.

    Returns:
        The rendered neural-nets.html template.
    """
    return render_template("neural-nets.html")


@app.route("/menu/blog")
def menu_blog():
    """
    Route handler for the Blog menu content.

    Returns:
        The rendered blog.html template.
    """
    return render_template("blog.html")


@app.route("/menu/coders")
def menu_coders():
    """
    Route handler for the Coders menu content.

    Returns:
        The rendered coders.html template.
    """
    return render_template("coders.html")


# For local development
# This block only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    # Start the Flask development server
    # debug=True enables debug mode, which shows detailed error messages and enables hot reloading
    # host='0.0.0.0' makes the server accessible from any IP address
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", host="127.0.0.1", port=8000)  # nosec B104


# For Vercel deployment
# This exposes the Flask application as a module-level variable
logging.info("PATH app initialized successfully for Vercel deployment")
