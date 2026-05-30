import sys
from pathlib import Path

FLASK_DIR = Path(__file__).resolve().parents[1] / "flask"
if str(FLASK_DIR) not in sys.path:
    sys.path.insert(0, str(FLASK_DIR))
