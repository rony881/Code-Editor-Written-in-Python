# src/light_code/config.py

from pathlib import Path


# Project Root Folder Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent / "light_code"


# Application Window Configuration
# Window Width and Height
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
# Application Logo
WINDOW_LOGO = str(PROJECT_ROOT / "assets" / "icons" / "app-logo.png")


# ============= Application Icons ========================================
# Used for File Explorer Button in Status Bar
EXPLORER_ICON = str(PROJECT_ROOT / "assets" / "icons" / "file-explorer-logo.svg")

# Used for Git Button in Status Bar
GIT_ICON = str(PROJECT_ROOT / "assets" / "icons" / "git-logo.svg")

# Used for Left Panel Button in Status Bar
LEFT_PANEL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "left-panel-logo.svg")

# Used for AI Agent Button in Status Bar
AI_AGENT_ICON = str(PROJECT_ROOT / "assets" / "icons" / "ai-agent-logo.svg")

# Used for Right Panel Button in Status Bar
RIGHT_PANEL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "right-panel-logo.svg")

# Used for Terminal Button in Status Bar
TERMINAL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "terminal-logo.svg")

# Used for File Plus Button in File Explorer Header
FILE_PLUS_ICON = str(PROJECT_ROOT / "assets" / "icons" / "file-plus-logo.svg")

# Used for Folder Plus Button in File Explorer Header
FOLDER_PLUS_ICON = str(PROJECT_ROOT / "assets" / "icons" / "folder-plus-logo.svg")


# Application Default Style Sheet Dir
STYLE_SHEET_FILE = str(PROJECT_ROOT / "ui" / "themes" / "style.qss")