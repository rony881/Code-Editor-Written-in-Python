from pathlib import Path

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QSplitter, QVBoxLayout
from PyQt6.QtCore import Qt

from app.config import STYLE_SHEET_FILE, WINDOW_HEIGHT, WINDOW_LOGO, WINDOW_WIDTH
from core.file_ops import read_file
from ui.BaseWidgets.widget_base import BaseWidget
from ui.components.panels.central_panel import CentralPanel
from ui.components.panels.left_panel import LeftPanel
from ui.components.panels.right_panel import RightPanel
from ui.main_statusbar import StatusBar
from ui.window_menubar import EditorMenuBar


class MainWindow(QMainWindow):
    """
    Main application window containing MenuBar, Editor,
    Left Panel, Right Panel, Down Panel etc.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("PyCode")
        self.setWindowIcon(QIcon(WINDOW_LOGO))
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(self.read_style_sheet())

        #============= Menu Bar ===============
        self.menu_bar = EditorMenuBar(parent=self)
        self.setMenuBar(self.menu_bar)

        #============= Central Widget ============
        self.central_widget = BaseWidget()
        self.setCentralWidget(self.central_widget)

        #============== Main Window Splitter ===========================
        # This splitter container widget would contain 3 panels-
        # left,right and the contral panel. 
        self.splitter_container = QSplitter(Qt.Orientation.Horizontal)
        self.splitter_container.setSizes([260, 900, 280])
        self.central_widget.add(self.splitter_container)

        self.left_panel = LeftPanel()
        self.splitter_container.addWidget(self.left_panel)
        self.left_panel.explorer_file_selected_conn(self.open_file_from_explorer)
        
        self.central_panel = CentralPanel()
        self.splitter_container.addWidget(self.central_panel)
        
        self.right_panel = RightPanel()
        self.splitter_container.addWidget(self.right_panel)

        #============= Status Bar ============
        self.status_bar = StatusBar(self)
        self.setStatusBar(self.status_bar)

        self.status_bar.setGitBtnConn(self.open_git_panel)
        self.status_bar.setExplorerBtnConn(self.open_explorer_panel)
        self.status_bar.setAgentBtnConn(self.open_agent_panel)
        self.status_bar.setTerminalBtnConn(self.open_terminal_panel)

    def open_file_from_explorer(self, file_path: str):
        content, name = read_file(file_path)
        self.central_panel.add_tab(name, file_path, content)

    def open_git_panel(self):
        self.left_panel.showPanel("git")

    def open_explorer_panel(self):
        self.left_panel.showPanel("explorer")

    def open_agent_panel(self):
        self.right_panel.showPanel("agent")

    def open_terminal_panel(self):
        self.right_panel.showPanel("terminal")

    def read_style_sheet(self, styleSheetFile: str=STYLE_SHEET_FILE) -> str:
        with open(styleSheetFile, "r", encoding="utf-8") as file:
            style_sheet = file.read()
        return style_sheet

    # File / Edit / View / Settings / About / Help methods unchanged below...

    # ─────────────────────────────────────────────
    # File
    # ─────────────────────────────────────────────

    def new_file(self):
        """Create a new file."""
        pass

    def open_file(self):
        """Open a file."""
        pass

    def browse_folder(self):
        """Open a folder."""
        self.left_panel.browse_folder()

    def save_file(self):
        """Save the current file."""
        pass

    def save_file_as(self):
        """Save the current file with a new name."""
        pass

    def close_tab(self):
        """Close the current editor tab."""
        pass

    # ─────────────────────────────────────────────
    # Edit
    # ─────────────────────────────────────────────

    def undo(self):
        """Undo the last editing operation."""
        pass

    def redo(self):
        """Redo the last editing operation."""
        pass

    def cut(self):
        """Cut the selected text."""
        pass

    def copy(self):
        """Copy the selected text."""
        pass

    def paste(self):
        """Paste text from the clipboard."""
        pass

    def find_(self):
        """Open the find interface."""
        pass

    def replace(self):
        """Open the replace interface."""
        pass

    def go_to_line(self):
        """Go to a specific line."""
        pass

    # ─────────────────────────────────────────────
    # View
    # ─────────────────────────────────────────────

    def toggle_sidebar(self):
        """Show or hide the sidebar."""
        pass

    def toggle_terminal(self):
        """Show or hide the terminal."""
        pass

    def toggle_minimap(self):
        """Show or hide the minimap."""
        pass

    def zoom_in(self):
        """Increase editor zoom."""
        pass

    def zoom_out(self):
        """Decrease editor zoom."""
        pass

    def reset_zoom(self):
        """Reset editor zoom to the default level."""
        pass

    # ─────────────────────────────────────────────
    # Settings
    # ─────────────────────────────────────────────

    def open_preferences(self):
        """Open editor preferences."""
        pass

    def open_shortcuts_editor(self):
        """Open keyboard shortcut settings."""
        pass

    def open_theme_settings(self):
        """Open theme settings."""
        pass

    # ─────────────────────────────────────────────
    # About
    # ─────────────────────────────────────────────

    def show_about_dialog(self):
        """Show the About dialog."""
        pass

    def check_for_updates(self):
        """Check for application updates."""
        pass

    # ─────────────────────────────────────────────
    # Help
    # ─────────────────────────────────────────────

    def open_docs(self):
        """Open the editor documentation."""
        pass

    def report_issue(self):
        """Open the issue reporting page."""
        pass