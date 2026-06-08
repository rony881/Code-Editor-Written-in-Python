from PyQt6.Qsci import QsciScintilla
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QSizePolicy,
    QTabWidget,
    QSplitter,
    QMenuBar,
    QTreeView
    )
from PyQt6.QtGui import (
    QAction,
    QFileSystemModel
)
from PyQt6.QtCore import Qt, QPoint
import sys


# ============================================================================
# Window Title Class
# ============================================================================


class Window_title(QFrame):
    """This Class Creates a Custom Window Title"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.drag_pos = QPoint()
        self.setObjectName("titlebar")
        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.setLayout(layout)

        self.topbar = Menumanager(self)
        self.topbar.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        layout.addWidget(self.topbar)
        layout.addStretch()

        # Min Button
        self.min_btn = QPushButton("—")
        self.min_btn.clicked.connect(self.parent().showMinimized)
        layout.addWidget(self.min_btn)

        # Max Button
        self.max_btn = QPushButton("□")
        self.max_btn.clicked.connect(self.toggle_max_restore)
        self.max_btn.setObjectName("maxbtn")
        layout.addWidget(self.max_btn)
        
        # Close Button
        self.close_btn = QPushButton("✕")
        self.close_btn.clicked.connect(self.parent().close)
        self.close_btn.setObjectName("closebtn")
        layout.addWidget(self.close_btn)

        # Setup MenuBar
        self._setup_menubar()

    def _setup_menubar(self):
        """This method setup MenuBar"""

        menubar = self.topbar
        menus = {
            "File": [
                ("New File",None, "Ctrl+N"),
                ("Open File",None, "Ctrl+O"),
                ("Open Folder", None, "Ctrl+K"),
                "separator",
                ("Save", None, "Ctrl+S"),
                ("Save As",None, "Ctrl+Shift+S"),
                "separator",
                ("Settings", None, None),
                ("Exit", None, None),
            ],
            "Edit": [
                ("Undo", None, "Ctrl+Z"),
                ("Redo", None, "Ctrl+Shift+Z"),
                "separator",
                ("Cut", None, "Ctrl+X"),
                ("Copy", None, "Ctrl+C"),
                ("Paste", None, "Ctrl+V"),
                "separator",
                ("Find", None, None),
                ("Replace", None, None),
                ("Select All", None, "Ctrl+A"),
                ("Go to Line", None, None),
            ],
            "View": [
                ("Terminal", None, "Ctrl+'"),
                "separator",
                ("Toggle Sidebar", None, None),
                "separator",
                ("Zoom In", None, "Ctrl++"),
                ("Zoom Out", None, "Ctrl+-"),
            ],
            "Run": [
                ("Run Code", None, "Ctrl+R"),
                ("Debug Code", None, None),
            ],
        }

        for menu_name, actions in menus.items():
            menu = menubar.add_menu(menu_name)

            for item in actions:

                if item == "separator":
                    menu.addSeparator()
                else:
                    name, func, shortcut = item
                    menubar.add_action(menu, name, func, shortcut)

    def toggle_max_restore(self):
        """This Method Handles Window Fullscreen Action"""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()
    # Window Dragging Methods:
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = (
                event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.parent().move(event.globalPosition().toPoint() - self.drag_pos)

# ============================================================================
# Mainwindow Class
# ============================================================================

class MainWindow(QWidget):
    """Main application window."""

    def __init__(self):
        super().__init__()

        # Window configuration
        self.setObjectName("container")
        self.resize(800, 600)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.title = Window_title(self) # <- Title Bar

        # My Working Directory
        self.current_working_dir = r"C:\Users\Lenovo\OneDrive\文件\Projects\Tree_View"

        self._setup_tree(self.current_working_dir)
        self._setup_tabs()
        self._setup_splitter()
        self._setup_layout()
    
    def _setup_tree(self, file_path):
        self.model = QFileSystemModel()
        self.tree = QTreeView()

        self.model.setRootPath(file_path)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(file_path))

        # File TreeView Configarations
        self.model.setIconProvider(None)  # Remove Folder and File Icons
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)  # Hide The Columns Of File TreeView
        self.tree.hideColumn(3)
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setMinimumWidth(180)
        self.tree.setItemsExpandable(True)
        self.tree.setRootIsDecorated(True)
        self.tree.setHeaderHidden(True)  # Hide the File Header

    def _setup_tabs(self):
        """This Method Setup Tabs"""

        self.tabs = QTabWidget()
        self.tabs.setObjectName("tabwidget")

        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

    def _setup_splitter(self):
        """This Method Setup Splitter"""

        self.splitter = QSplitter()
        self.splitter.setObjectName("splitter")
        self.splitter.setHandleWidth(0)

        self.splitter.setContentsMargins(0, 0, 0, 0)

        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.tabs)

        self.splitter.setSizes([200, 900])

    def _setup_layout(self):
        """This Method Setup Layout"""

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add The TitleBar and The Splitter
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.splitter)
    
    def close_tab(self,index):
        self.tabs.removeTab(index)

# ============================================================================
# Main Editor Class
# ============================================================================

class Editor(QsciScintilla):
    """The Editor Inharet From QSciScintilla(Code Editor) Class"""

    def __init__(self):
        super().__init__()
        self.setObjectName("Editor")
        lexer = self.syntax_color()
        self.setLexer(lexer)

        self.setMarginWidth(0, "00000")
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setTabWidth(4)

        # Auto-completion:
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(False)

        # Indentation Guide
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setCaretWidth(2)  # Cursor Width

# ============================================================================
# Menu Manager Class
# ============================================================================
class Menumanager(QMenuBar):
    """Manages menu bar creation and action handling."""

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setObjectName("menubar")

    def add_menu(self, name: str):
        
        return self.addMenu(name)

    def add_action(self, menu, name: str, func=None, shortcut: str = None) -> QAction:
        action = QAction(name, self.parent()) 

        if shortcut:
            action.setShortcut(shortcut)

        if func:
            action.triggered.connect(func)

        menu.addAction(action)
        return action


# =============================================================================
# Run App
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())