from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QTreeView,
    QSizePolicy,
    QPushButton,
)
from PyQt6.QtGui import QShortcut, QKeySequence, QFileSystemModel
from PyQt6.QtCore import Qt, QSize, QPoint
from core.fileops import FileOps
from core.code_runner import run_code
from ui.tab_manager import Tab
from ui.menu_manager import Menumanager

# Window Size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

STYLESHEET = "themes/style.qss"

# ============================================================================
# Window Title Class
# ============================================================================

class Window_title(QFrame):
    """This Class Creats a Custom Window Title"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)  # Pass parent to Qt so self.parent() works

        self.drag_pos = QPoint()
        self.setObjectName("titlebar")  # Object name
        self.setFixedHeight(35)  # Height of the title Bar

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
        layout.addWidget(self.max_btn)
        # Close Button
        self.close_btn = QPushButton("✕")
        self.close_btn.clicked.connect(self.parent().close)
        self.close_btn.setObjectName("closebtn")
        layout.addWidget(self.close_btn)

    def toggle_max_restore(self):
        """This Method Handle Window Fullscreen Action"""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()

    # Window Draging Methods :
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
    """Main application window for the text editor."""

    def __init__(self):
        """Initialize The Main Window"""
        super().__init__()

        # Window configuration
        self.setObjectName("container")
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # window_title class object
        self.title = Window_title(self)

        # FileOps() class object
        self.file_ops = FileOps(self)

        # Tabs() class object
        self.tabs = Tab(self)

        # File TreeView
        self.tree = QTreeView()
        self.model = QFileSystemModel()
        self.tree.setObjectName("treeview")
        self.tree.clicked.connect(self.on_file_click)

        # tree configaretion
        self.tree.setModel(self.model)
        self.tree.setIconSize(QSize(0,0))  # Remove Folder and File Icons
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)  # Hide Extra Column
        self.tree.hideColumn(3)
        self.tree.setAnimated(True)
        self.tree.setIndentation(10)
        self.tree.setMinimumWidth(170)
        self.tree.setItemsExpandable(True)
        self.tree.setRootIsDecorated(False)
        self.tree.setHeaderHidden(True)  # Hide the File Header

        # Zen Mode Shortcuts
        self.fullscreen_shortcut = QShortcut(QKeySequence("F11"), self)
        self.fullscreen_shortcut.activated.connect(self.zen_mode)
        # My Working Directory
        self.current_working_dir = r"C:\Users\Lenovo\OneDrive\文件\Projects\Text Editor"

        # ======== Window Setup =========
        self._setup_menubar()
        self._setup_splitter()
        self._setup_layout()
        self.mk_tree(self.current_working_dir)
        self.setStylesheet(STYLESHEET)

    def setStylesheet(self, styleSheet):
        """Set The SyleSheeet To The Application"""

        style_sheet = self.file_ops.read_file(STYLESHEET)

        if style_sheet:
            self.setStyleSheet(style_sheet)

    def _setup_layout(self):
        """This Method Setup Layout"""

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add The TitleBar and The Splitter
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.splitter)

    def _setup_splitter(self):
        """This Method Setup Splitter"""

        self.splitter = QSplitter()
        self.splitter.setObjectName("splitter")
        self.splitter.setHandleWidth(1)

        self.splitter.setContentsMargins(0, 0, 0, 0)

        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.tabs)

        self.splitter.setSizes([190, 910])

    def on_file_click(self, index):
        """Handle File Tree Click"""
        file_info = self.model.fileInfo(index)

        if file_info.isDir():  # If file is Folder then Do nothing
            return

        file_path = file_info.filePath()
        file_name = file_info.fileName()

        content = self.file_ops.read_file(file_path)
        
        if content:
            self.tabs.open_tab(file_name, file_path, content)

    def _setup_menubar(self):
        """This method setup MenuBar"""

        menubar = self.title.topbar
        menus = {
            "File": [
                ("New File", self.file_ops.new_file, "Ctrl+N"),
                ("Open File", self.file_ops.open_file, "Ctrl+O"),
                ("Open Folder", self.file_ops.open_folder, "Ctrl+K"),
                "separator",
                ("Save", self.file_ops.save_file, "Ctrl+S"),
                ("Save As", self.file_ops.save_as, "Ctrl+Shift+S"),
                "separator",
                ("Settings", None, None),
                ("Exit", self.close, None),
            ],
            "Edit": [
                ("Find", None, None),
                ("Replace", None, None),
                ("Select All", None, "Ctrl+A"),
                ("Go to Line", None, None),
                ("Zoom In", None, "Ctrl++"),
                ("Zoom Out", None, "Ctrl+-"),
            ],
            "View": [
                ("Zen Mode", self.zen_mode, None),
                ("Open Terminal", None, "Ctrl+'"),
                "separator",
                ("Toggle Sidebar", None, None),
            ],
            "Run": [
                ("Run Code",run_code, "Ctrl+R"),
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

    def mk_tree(self, file_path):
        self.model.setRootPath(file_path)
        self.tree.setRootIndex(self.model.index(file_path))

    def zen_mode(self):
        if self.isFullScreen():
            self.showNormal()
            self.title.show()
            self.tree.show()
        else:
            self.showFullScreen()
            self.tree.hide()
            self.title.hide()

    