"""
Shared requests fallback implementation.
This module provides a fallback for the requests module when it's not available.
"""

from __future__ import annotations

import sys
from typing import Any
from typing import ClassVar

# Try to import requests and vendor at the module level
try:
    import requests  # noqa: F401

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

# Try to import vendored requests
try:
    # type: ignore[import-not-found]
    from requests_vendor import RequestError
    from requests_vendor import delete
    from requests_vendor import get
    from requests_vendor import post
    from requests_vendor import put
    from requests_vendor import request

    VENDORED_AVAILABLE = True
except ImportError:
    VENDORED_AVAILABLE = False


class RequestsFallback:
    """A requests-compatible module using our vendored implementation."""

    def __init__(self) -> None:
        """Initialize the requests fallback with vendored implementations."""
        self.request = self._get_vendored("request")
        self.get = self._get_vendored("get")
        self.post = self._get_vendored("post")
        self.put = self._get_vendored("put")
        self.delete = self._get_vendored("delete")
        self.RequestError = self._get_vendored("RequestError")
        self.codes = type("Codes", (), {"ok": 200, "not_found": 404})

    # Class variable to store vendored implementations
    _vendored: ClassVar[Any] = None

    @classmethod
    def set_vendored_implementation(cls):
        """Set the vendored implementation."""

        class Vendored:
            request = request
            get = get
            post = post
            put = put
            delete = delete
            RequestError = RequestError

        cls._vendored = Vendored()

    @classmethod
    def _get_vendored(cls, name: str) -> Any:
        """Get a vendored implementation by name.

        Raises:
            VendoredNotAvailableError: If vendored requests are not available
        """
        if cls._vendored is None:
            error_msg = "Vendored requests not available"
            raise cls.VendoredNotAvailableError(error_msg)
        return getattr(cls._vendored, name, None)

    class VendoredNotAvailableError(ImportError):
        """Raised when vendored requests are not available."""


def setup_requests_fallback() -> bool:
    """
    Set up a requests module fallback using vendored implementation.

    Returns:
        bool: True if fallback was set up, False if requests is already available

    Raises:
        ImportError: If neither requests nor vendored version is available
    """
    # Check if requests is already available
    if REQUESTS_AVAILABLE:
        return False

    if not VENDORED_AVAILABLE:
        error_msg = (
            "the 'requests' module is not available and could not use vendored version. "
            "please install it with 'pip install requests' or include a complete vendored version."
        )
        raise ImportError(error_msg)

    RequestsFallback.set_vendored_implementation()

    # Patch sys.modules
    sys.modules["requests"] = RequestsFallback()
    return True


# Set up the fallback when the module is imported
setup_requests_fallback()
