"""
Shared requests fallback implementation.
This module provides a fallback for the requests module when it's not available.
"""

import sys
# Path is used in type hints and potential path manipulations
from pathlib import Path  # pylint: disable=unused-import

# Try to import requests at module level
try:
    # Imported for its side effects, not directly used
    import requests as _requests  # pylint: disable=unused-import
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

# Initialize module-level variables for vendored requests
VENDORED_REQUESTS_AVAILABLE = False
REQUEST_ERROR = None
VENDORED_DELETE = None
VENDORED_GET = None
VENDORED_POST = None
VENDORED_PUT = None
VENDORED_REQUEST = None

# Try to import vendored requests at module level
if not REQUESTS_AVAILABLE:
    try:
        from requests_vendor import (  # type: ignore
            RequestError as VendorRequestError,
            delete as vendor_delete,
            get as vendor_get,
            post as vendor_post,
            put as vendor_put,
            request as vendor_request,
        )
        VENDORED_REQUESTS_AVAILABLE = True
        REQUEST_ERROR = VendorRequestError
        VENDORED_DELETE = vendor_delete
        VENDORED_GET = vendor_get
        VENDORED_POST = vendor_post
        VENDORED_PUT = vendor_put
        VENDORED_REQUEST = vendor_request
    except ImportError:
        pass


def setup_requests_fallback() -> bool:
    """
    Set up a requests module fallback using vendored implementation.

    Returns:
        bool: True if fallback was set up, False if requests is already available

    Raises:
        ImportError: If neither requests nor vendored version is available
    """
    if REQUESTS_AVAILABLE:
        return False

    if not VENDORED_REQUESTS_AVAILABLE:
        raise ImportError(
            "The 'requests' module is not available. "
            "Please install it with 'pip install requests' or include a vendored version."
        )

    # Create a requests-compatible module
    class RequestsFallback:  # pylint: disable=too-few-public-methods
        """A requests-compatible module using our vendored implementation."""

        request = VENDORED_REQUEST
        get = VENDORED_GET
        post = VENDORED_POST
        put = VENDORED_PUT
        delete = VENDORED_DELETE
        RequestError = REQUEST_ERROR
        codes = type("Codes", (), {"ok": 200, "not_found": 404})

    # Patch sys.modules
    sys.modules["requests"] = RequestsFallback()
    return True
