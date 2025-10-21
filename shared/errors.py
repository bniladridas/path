"""
Shared error message helpers for the PATH application.
"""


def get_rate_limit_error_message() -> str:
    """Get the error message for rate limit errors."""
    return (
        "i'm so excited to learn more with you! there's just so much "
        "fascinating stuff about media to discover. let me catch my "
        "breath and we can dive back into exploring together in just a moment."
    )


def get_api_error_message() -> str:
    """Get the error message for general API errors."""
    return (
        "i'm buzzing with curiosity about what you want to explore! "
        "something's just taking a moment to connect, but i'm eager to "
        "learn and discover new things about media with you. let's try again soon!"
    )


def get_internal_error_message() -> str:
    """Get the error message for internal/system errors."""
    return (
        "i'm practically bouncing with excitement to learn about what you're "
        "curious about! something's just taking a moment to sort itself out, "
        "but i can't wait to discover and explore media topics with you. "
        "let's try again in just a bit!"
    )


def get_ai_unavailable_message() -> str:
    """Get the error message when AI is unavailable."""
    return "AI functionality is currently unavailable. Please try again later."
