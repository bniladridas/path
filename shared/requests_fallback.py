"""
Shared requests fallback implementation.
This module provides a fallback for the requests module when it's not available.
"""

def setup_requests_fallback():
    """
    Set up a requests module fallback using vendored implementation.
    
    Returns:
        bool: True if fallback was set up, False if requests is already available
    """
    try:
        import requests
        return False  # requests is available, no fallback needed
    except ImportError:
        try:
            # Try to use the vendored version in the api directory
            import sys
            from pathlib import Path

            # Add the api directory to the Python path
            API_DIR = str(Path(__file__).parent.parent / "api")
            if API_DIR not in sys.path:
                sys.path.insert(0, API_DIR)
                
            # Import the vendored requests module
            from requests_vendor import (
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

                # Add other necessary attributes
                codes = type("Codes", (), {"ok": 200, "not_found": 404})

            # Patch sys.modules
            import sys as _sys
            _sys.modules["requests"] = RequestsFallback()
            return True
            
        except ImportError as e:
            # If vendored version is not available, raise a helpful error
            error_msg = "The 'requests' module is not available. "
            error_msg += "Please install it with 'pip install requests' or include a vendored version."
            raise ImportError(error_msg) from e
