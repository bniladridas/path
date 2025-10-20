"""
Shared requests fallback implementation.
This module provides a fallback for the requests module when it's not available.
"""

import sys
from pathlib import Path


def setup_requests_fallback():
    """
    Set up a requests module fallback using vendored implementation.

    Returns:
        bool: True if fallback was set up, False if requests is already available

    Raises:
        ImportError: If neither requests nor vendored version is available
    """
    try:
        # Check if requests is already available
        import requests  # pylint: disable=import-outside-toplevel,unused-import
        return False
    except ImportError:
        try:
            # Add the api directory to the Python path
            api_dir = str(Path(__file__).parent.parent / "api")
            if api_dir not in sys.path:
                sys.path.insert(0, api_dir)

            # Import the vendored requests module
            from requests_vendor import (  # pylint: disable=import-outside-toplevel
                RequestError,
                delete,
                get,
                post,
                put,
                request,
            )

            # Create a requests-compatible module
            class RequestsFallback:  # pylint: disable=too-few-public-methods
                """A requests-compatible module using our vendored implementation."""

                request = request
                get = get
                post = post
                put = put
                delete = delete
                RequestError = RequestError
                codes = type("Codes", (), {"ok": 200, "not_found": 404})

            # Patch sys.modules
            sys.modules["requests"] = RequestsFallback()
            return True

        except ImportError as import_error:
            error_msg = (
                "The 'requests' module is not available. "
                "Please install it with 'pip install requests' or include a vendored version."
            )
            raise ImportError(error_msg) from import_error
