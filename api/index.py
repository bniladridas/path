"""
Vercel API endpoint that imports the main app from the path directory.
"""

import sys
from pathlib import Path

# Add the path directory to Python path
path_dir = Path(__file__).parent.parent / "path"
sys.path.insert(0, str(path_dir))

# Import the app from the path directory
from app import app  # noqa: E402

# Export for Vercel
application = app
