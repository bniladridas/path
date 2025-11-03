"""
Shared verification logic for the PATH application.
"""

# Define keywords that indicate correct understanding of the verification image
# The image shows a human avatar, so we accept various human-related terms
# This list is intentionally broad to accommodate different ways of describing the image
VERIFICATION_KEYWORDS = [
    "human",
    "person",
    "avatar",
    "face",
    "profile",
    "picture",
    "man",
    "woman",
]


def is_verification_answer_valid(answer: str) -> bool:
    """
    Check if the user's verification answer contains valid keywords.

    Args:
        answer: The user's answer, normalized to lowercase

    Returns:
        bool: True if the answer is valid, False otherwise
    """
    # Check if the user's answer contains any of the expected keywords
    # Using 'any()' with generator expression for efficient keyword matching
    return any(keyword in answer for keyword in VERIFICATION_KEYWORDS)
