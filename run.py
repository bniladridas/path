#!/usr/bin/env python3
"""
Harper App Runner
Fixed for Python 3.14 compatibility with jinja2 patching.
"""

import jinja2
from markupsafe import Markup
from markupsafe import escape

# Patch jinja2 for Flask 3.0.3 compatibility
jinja2.escape = escape
jinja2.Markup = Markup

from path.app import app

if __name__ == "__main__":
    print("🎉 Harper - AI Media Exploration Interface")
    print("📡 Starting server at: http://127.0.0.1:8000")
    print("🧭 Test refactored menu functionality!")
    print("🔑 Features: Jinja templates, Flask routes, AJAX loading")
    print()
    app.run(debug=True, host="127.0.0.1", port=8000)
