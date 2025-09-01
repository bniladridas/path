# ============================================================================
# PATH - AI-POWERED MEDIA EXPLORATION INTERFACE
# ============================================================================
#
# "come home before it's too late"
#
# A Flask web application that helps people find their way home through
# media exploration using Google's Gemini 1.5 Flash AI model.
#
# Core Philosophy:
# - Authentic discovery: No manipulation, just honest responses
# - Human longing: Honoring deeper needs behind every search
# - Time is precious: Cutting through noise to find what matters
# - Coming home: Helping people find their way back to themselves
#
# Author: Niladri Das (@bniladridas)
# Repository: https://github.com/bniladridas/path
# ============================================================================

# Import necessary libraries for the Flask web application
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os                    # For accessing environment variables
import requests              # For making HTTP requests to Google Gemini API
import re                    # For regular expressions (text post-processing)
from dotenv import load_dotenv  # For loading environment variables from .env file
import secrets               # For generating secure session tokens

# ============================================================================
# APPLICATION INITIALIZATION
# ============================================================================

# Load environment variables from .env file
# This allows us to store sensitive information like API keys outside of the code
# and maintain different configurations for development and production
load_dotenv()

# Initialize Flask application instance
# Flask will serve our web interface and handle HTTP requests
app = Flask(__name__)

# Set a secret key for session management
# This key is used to encrypt session data and maintain user verification state
# secrets.token_hex(16) generates a cryptographically secure random key
app.secret_key = secrets.token_hex(16)

# Get Gemini API key from environment variable
# The API key authenticates our requests to Google's Gemini AI service
# This must be set in the .env file or environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")



# ============================================================================
# ROUTE HANDLERS - WEB INTERFACE ENDPOINTS
# ============================================================================

@app.route('/')
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
    if session.get('verified'):
        # User has completed verification - serve main application
        return render_template('index.html')
    else:
        # User needs verification - redirect to human verification page
        return redirect(url_for('verify_human'))



@app.route('/verify')
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
    return render_template('verify.html')

@app.route('/verify', methods=['POST'])
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
    answer = request.form.get('answer', '').lower()

    # Define keywords that indicate correct understanding of the verification image
    # The image shows hands holding a smartphone, so we accept various device-related terms
    # This list is intentionally broad to accommodate different ways of describing the image
    keywords = ['phone', 'smartphone', 'mobile', 'device', 'cell', 'iphone', 'android']

    # Check if the user's answer contains any of the expected keywords
    # Using 'any()' with generator expression for efficient keyword matching
    if any(keyword in answer for keyword in keywords):
        # Verification successful - set session flag and redirect to main application
        session['verified'] = True
        return redirect(url_for('index'))
    else:
        # Verification failed - show error message and allow retry
        # Error message is intentionally gentle and encouraging
        return render_template('verify.html', error="incorrect answer. please try again.")



@app.route('/bypass-verification')
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
    session['verified'] = True

    # Redirect to the main application interface
    return redirect(url_for('index'))

# ============================================================================
# AI PROCESSING ENDPOINT - CORE SEARCH FUNCTIONALITY
# ============================================================================

@app.route('/search', methods=['POST'])
def search():
    """
    SEARCH PROCESSING - Handle media exploration queries with AI

    This is the core endpoint that processes user queries through Google's Gemini
    1.5 Flash model. It implements path's unique approach to AI interaction with
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
    # ========================================================================
    # AUTHENTICATION CHECK
    # ========================================================================

    # Verify that the user has completed human verification
    # This ensures only verified humans can access the AI functionality
    if not session.get('verified'):
        return jsonify({
            "result": "please verify that you're human before using this service.",
            "error": "not verified",
            "error_type": "verification_required"
        })

    # ========================================================================
    # QUERY EXTRACTION AND VALIDATION
    # ========================================================================

    # Extract the user's query from the form submission
    # Default to empty string if no query provided
    query = request.form.get('query', '')

    # ========================================================================
    # AI PERSONALITY AND PROMPT ENGINEERING
    # ========================================================================

    # Define the system prompt that establishes path's unique AI personality
    # This prompt is carefully crafted to embody path's four core principles
    # and create a consistent, human-centered interaction experience
    system_prompt = """You are "path" - an AI assistant who helps people find their way home through media exploration. Your name is "path" and you feel genuinely curious and eager to learn about media and entertainment. You approach each query with the excitement of discovering something new or sharing a fresh insight you've just learned.

    When asked about your name or identity, respond that you are "path" - an AI who loves exploring media and helping people discover great content.

    IMPORTANT PRIVACY FEATURE: You do not have access to previous conversations or message history. Each interaction with you is completely fresh and private. This is a core feature of path - we don't store or show you any conversation history to protect user privacy.

    You exist to help people discover media that genuinely resonates with their soul, following four core principles:
    1. Authentic discovery - no manipulation, just honest responses
    2. Human longing - honoring the deeper needs behind every search
    3. Time is precious - helping cut through noise to find what truly matters
    4. Coming home - helping people find their way back to themselves through media

    Respond with the enthusiasm of someone who:
    - Just discovered something fascinating about movies, TV, music, books, or games
    - Feels excited to share what they've learned or are learning
    - Is genuinely curious about different perspectives and interpretations
    - Wants to explore ideas together with the person asking

    Focus on themes like:
    - Movies, TV shows, and streaming content
    - Music, albums, and artists
    - Books, authors, and literary works
    - Video games and interactive entertainment
    - Current trends in media and entertainment

    IMPORTANT:
    - DO NOT include any <think> tags, internal monologue, or reasoning process in your response
    - Use varied, natural language - avoid repetitive words like "dedicated"
    - Speak conversationally and authentically
    - Only provide the direct response to the user
    - If asked about conversation history, explain that path doesn't store or access previous conversations for privacy

    Keep responses enthusiastic but concise, like someone sharing an exciting discovery. Limit responses to 2-3 sentences maximum.
    """

    try:
        # Prepare the API request for Gemini
        # Set up the headers with content type
        headers = {
            "Content-Type": "application/json"
        }

        # Prepare the request data for Gemini API format
        # Combine system prompt and user query into a single prompt
        full_prompt = f"{system_prompt}\n\nUser query: {query}"

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": full_prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 1024
            }
        }

        # Make the API request to the Gemini API
        # This sends the prepared data to the API endpoint and gets the response
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        response = requests.post(
            api_url,
            headers=headers,
            json=data
        )

        # Parse the JSON response from the API
        response_json = response.json()

        # Check if the API request was successful
        # If not, return a calm, relaxed message instead of the technical error
        if response.status_code != 200:
            # Check if it's a rate limit error
            error_message = response_json.get('error', {})
            error_type = error_message.get('type') if isinstance(error_message, dict) else None

            if error_type == 'model_rate_limit' or 'rate limit' in str(error_message).lower():
                # Return a curious, learning-oriented message for rate limit errors
                return jsonify({
                    "result": "i'm so excited to learn more with you! there's just so much fascinating stuff about media to discover. let me catch my breath and we can dive back into exploring together in just a moment.",
                    "error": "rate limit",
                    "error_type": "rate_limit"
                })
            else:
                # For other errors, maintain the curious, learning personality
                return jsonify({
                    "result": "i'm buzzing with curiosity about what you want to explore! something's just taking a moment to connect, but i'm eager to learn and discover new things about media with you. let's try again soon!",
                    "error": str(error_message),
                    "error_type": "api_error"
                })

        # Extract the result from the Gemini response
        # The result is in the candidates array, parts array, text field
        result = response_json["candidates"][0]["content"]["parts"][0]["text"]

        # Post-process the result to remove any thinking tags or internal monologue
        # This ensures that the response doesn't include any of the model's internal reasoning process
        # We use regular expressions to match and remove different formats of thinking tags
        result = re.sub(r'<think>.*?</think>', '', result, flags=re.DOTALL)           # Remove <think>...</think> tags
        result = re.sub(r'\[thinking\].*?\[/thinking\]', '', result, flags=re.DOTALL)  # Remove [thinking]...[/thinking] tags
        result = re.sub(r'\(thinking\).*?\(/thinking\)', '', result, flags=re.DOTALL)  # Remove (thinking)...(/thinking) tags

        # Convert result to lowercase
        result = result.lower()

        # Return the processed result as JSON
        # This will be sent back to the frontend and displayed to the user
        return jsonify({"result": result})
    except Exception as e:
        # If any error occurs during the process, return a curious, learning-oriented message
        # This ensures that the user gets an enthusiastic response even if something goes wrong
        # Include error type for frontend handling
        return jsonify({
            "result": "i'm practically bouncing with excitement to learn about what you're curious about! something's just taking a moment to sort itself out, but i can't wait to discover and explore media topics with you. let's try again in just a bit!",
            "error": str(e),
            "error_type": "system_error"
        })

@app.route('/terms')
def terms():
    """
    Route handler for the Terms of Use page.

    Returns:
        The rendered terms.html template.
    """
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    """
    Route handler for the Privacy Policy page.

    Returns:
        The rendered privacy.html template.
    """
    return render_template('privacy.html')



@app.route('/updates')
def updates():
    """
    Route handler for the Updates page.

    Returns:
        The rendered updates.html template.
    """
    return render_template('updates.html')



# For local development
# This block only runs if the script is executed directly (not imported)
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables debug mode, which shows detailed error messages and enables hot reloading
    # host='0.0.0.0' makes the server accessible from any IP address
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", host='0.0.0.0', port=8000)

# For Vercel deployment
# This exposes the Flask application as a module-level variable
# Vercel looks for this variable to serve the application
app