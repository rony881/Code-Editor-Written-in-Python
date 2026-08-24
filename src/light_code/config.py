# src/light_code/config.py


from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent / "light_code"

# Application Window Configuration
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_LOGO = str(PROJECT_ROOT / "assets" / "icons" / "app-logo.png")

# Icons
EXPLORER_ICON = str(PROJECT_ROOT / "assets" / "icons" / "file-explorer-logo.svg")
GIT_ICON = str(PROJECT_ROOT / "assets" / "icons" / "git-logo.svg")
LEFT_PANEL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "left-panel-logo.svg")
AI_AGENT_ICON = str(PROJECT_ROOT / "assets" / "icons" / "ai-agent-logo.svg")
RIGHT_PANEL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "right-panel-logo.svg")
TERMINAL_ICON = str(PROJECT_ROOT / "assets" / "icons" / "terminal-logo.svg")


# Style Sheet Dir
STYLE_SHEET_FILE = str(PROJECT_ROOT / "ui" / "themes" / "style.qss")