from PyQt6.QtGui import QFileSystemModel, QIcon
from PyQt6.QtWidgets import QLabel, QMainWindow, QSplitter, QTabWidget, QTreeView, QVBoxLayout, QWidget
from PyQt6.QtCore import QDir, Qt 

from app.config import WINDOW_HEIGHT, WINDOW_LOGO, WINDOW_WIDTH
from ui.BaseWidgets import BaseWidget
from ui.components.widgets.side_panel import SidePanel
from ui.themes.color_theme import DARK_STYLESHEET
from ui.window_menubar import EditorMenuBar


class MainWindow(QMainWindow):
    """
    Main application window containing MenuBar, Editor,
    Left Panel, Right Panel, Down Panel etc.
    """

    def __init__(self, parent=None):
        """Initialize the main window."""
        super().__init__(parent=parent)

        self.setWindowTitle("PyCode")
        self.setWindowIcon(QIcon(WINDOW_LOGO))
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(DARK_STYLESHEET)

        self.menu_bar = EditorMenuBar(parent=self)
        self.setMenuBar(self.menu_bar)

        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Main splitter: sidebar | editor |
        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(self.main_splitter, 1)

        # ── Sidebar ──
        sidebar = QWidget()
        sidebar.setMinimumWidth(220)
        sidebar.setMaximumWidth(400)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        sidebar_title = QLabel("EXPLORER")
        sidebar_title.setObjectName("sidebarTitle")
        sidebar_layout.addWidget(sidebar_title)

        self.file_model = QFileSystemModel()
        self.file_model.setRootPath("")
        self.file_model.setNameFilters([
            "*.c", "*.cpp", "*.cc", "*.cxx", "*.h", "*.hpp", "*.hxx",
            "*.txt", "*.md", "*.json", "*.xml", "*.py", "*.cmake",
            "*.mk", "*.Makefile", "*"
        ])
        self.file_model.setNameFilterDisables(False)

        self.file_tree = QTreeView()
        self.file_tree.setModel(self.file_model)
        self.file_tree.setHeaderHidden(True)
        self.file_tree.setColumnHidden(1, True)
        self.file_tree.setColumnHidden(2, True)
        self.file_tree.setColumnHidden(3, True)
        self.file_tree.setAnimated(True)
        self.file_tree.setIndentation(16)
        home = QDir.homePath()
        self.file_tree.setRootIndex(self.file_model.index(home))
        sidebar_layout.addWidget(self.file_tree)

        self.main_splitter.addWidget(sidebar)

        # ── Editor area (tabs + terminal) ──
        editor_area = QWidget()
        editor_layout = QVBoxLayout(editor_area)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.setSpacing(0)

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setDocumentMode(True)
        editor_layout.addWidget(self.tab_widget, 3)

        self.main_splitter.addWidget(editor_area)
        self.main_splitter.setSizes([260, 1140])

    # ─────────────────────────────────────────────
    # File
    # ─────────────────────────────────────────────

    def new_file(self):
        """Create a new file."""
        pass

    def open_file(self):
        """Open a file."""
        pass

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