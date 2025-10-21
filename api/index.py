import sys
from pathlib import Path

from path.app import app as application

# Add the project root to Python path
PROJECT_ROOT = str(Path(__file__).parent.parent)
sys.path.insert(0, PROJECT_ROOT)

# For Vercel deployment
if __name__ == "__main__":
    application.run(debug=True)
