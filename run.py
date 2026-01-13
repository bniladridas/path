#!/usr/bin/env python3
"""
Harper App Runner
Fixed for Python 3.14 compatibility with jinja2 patching.
"""

# Patch jinja2 for Flask 3.0.3 compatibility
import jinja2
from markupsafe import Markup
from markupsafe import escape

jinja2.escape = escape
jinja2.Markup = Markup

from path.app import app  # noqa: E402

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
