"""
Vendored version of the requests library.
This is a minimal implementation to support basic HTTP requests.
"""

import json
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen


class RequestError(Exception):
    """Custom exception for request errors."""


class Response:  # pylint: disable=too-few-public-methods
    """Minimal response object to match requests.Response interface."""

    def __init__(self, response, content):
        self.status_code = response.code
        self.content = content
        self.text = content.decode("utf-8")
        self.headers = dict(response.headers.items())

    def json(self):
        """Parse response as JSON."""
        return json.loads(self.text)


def request(method, url, **kwargs):
    """Send an HTTP request."""
    headers = kwargs.get("headers", {})
    data = kwargs.get("data")
    json_data = kwargs.get("json")
    params = kwargs.get("params")

    if params:
        url = f"{url}?{urlencode(params)}"

    if json_data:
        data = json.dumps(json_data).encode("utf-8")
        headers.setdefault("Content-Type", "application/json")
    elif data and isinstance(data, dict):
        data = urlencode(data).encode("utf-8")
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")

    req = Request(url, data=data, headers=headers, method=method.upper())

    try:
        with urlopen(req) as response:  # nosec B310
            content = response.read()
            return Response(response, content)
    except HTTPError as e:
        return Response(e, e.read())
    except URLError as e:
        error_msg = f"Request failed: {e}"
        raise RequestError(error_msg) from e


def get(url, **kwargs):
    """Send a GET request."""
    return request("GET", url, **kwargs)


def post(url, **kwargs):
    """Send a POST request."""
    return request("POST", url, **kwargs)


def put(url, **kwargs):
    """Send a PUT request."""
    return request("PUT", url, **kwargs)


def delete(url, **kwargs):
    """Send a DELETE request."""
    return request("DELETE", url, **kwargs)


# Make the module act like the requests module
__all__ = ["RequestError", "delete", "get", "post", "put", "request"]
