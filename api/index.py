import sys
from pathlib import Path

from app_local import app as application

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# For Vercel deployment
if __name__ == "__main__":
    application.run(debug=True)
