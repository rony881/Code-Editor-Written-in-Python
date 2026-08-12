# Application Window Configuration
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_LOGO = str(PROJECT_ROOT / "resources" / "icons" / "logo.png")

# Style Sheet Dir
STYLE_SHEET_FILE = str(PROJECT_ROOT / "ui" / "themes" / "style.qss")