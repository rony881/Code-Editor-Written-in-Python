import os
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
    QSplitter,
    QTreeView,
    QMessageBox,
)
from PyQt6.QtGui import QShortcut, QKeySequence, QFileSystemModel
from PyQt6.QtCore import Qt, QSize

from config import(
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    STYLESHEET
)
from ui.window_title import Window_title
from core.fileops import FileOps
from core.run_ops import run_code
from editor.editor import Editor
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

        # Custome Title Bar Object
        self.title = Window_title(self) # <- Title Bar
        # This Will Use For File Operations
        self.file_ops = FileOps(self)
        # This Will Keep tarck of Opened Tabs and Files
        self.open_tabs = {}
        self.open_files = {}
        # File TreeView
        self.tree = QTreeView()
        self.tree.setObjectName("treeview")
        self.tree.clicked.connect(self.on_file_click)
        # en Mode Shortcuts
        self.fullscreen_shortcut = QShortcut(QKeySequence("F11"), self)
        self.fullscreen_shortcut.activated.connect(self.zen_mode)
        # My Working Directory
        self.current_working_dir = r"C:\Users\Lenovo\OneDrive\文件\Projects\Text Editor"
        # File dialog filters
        self.file_filter = (
            "All Files (*.*);"
            "Python Files (*.py);"
            "C++ Files (*.cpp);"
            "C Files (*.c);"
            "QSS Files (*.qss);"
            "Java Files (*.java);"
            "Javascript (*.js);"
            "HTML (*.html);"
            "Readme File (*.md)"
        )
        
        # ======== Window Setup =========
        self._setup_menubar()
        self._setup_tabs()
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

    def _setup_tabs(self):
        """This Method Setup Tabs"""

        self.tabs = QTabWidget()
        self.tabs.setObjectName("tabwidget")

        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
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
        self.model = QFileSystemModel()
        self.model.setRootPath(file_path)

        # tree configaretion
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(file_path))
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

    def zen_mode(self):
        if self.isFullScreen():
            self.showNormal()
            self.title.show()
            self.tree.show()
        else:
            self.showFullScreen()
            self.tree.hide()
            self.title.hide()


    def close_tab(self, index):
        """Close a tab and save its content"""
        widget = self.tabs.widget(index)

        file_path = widget.file_path
        content = widget.text()

        reply = QMessageBox.question(self, "Save File", "Save File Befor Closing Tab? ")

        if file_path in self.open_tabs:
            del self.open_tabs[file_path]

        if file_path in self.open_files:
            del self.open_files[file_path]

        if reply == QMessageBox.StandardButton.No:
            self.tabs.removeTab(index)
            return

        save = self.file_ops.write_file(file_path,content)

        if save:
            self.tabs.removeTab(index)

    def mk_tab(self, name, file_path, text):

        if file_path in self.open_tabs:
            tab = self.open_tabs[file_path]  # -> tab
            indx = self.tabs.indexOf(tab)
            self.tabs.setCurrentIndex(indx)
            return

        new_tab = Editor()
        new_tab.setText(text)
        new_tab.file_path = file_path

        tab_index = self.tabs.addTab(
            new_tab, name
        )  # Creat New Tab and return Tab Index

        self.open_tabs[file_path] = new_tab
        self.open_files[file_path] = tab_index
        self.tabs.setCurrentIndex(tab_index)

        return tab_index

    def on_file_click(self, index):
        """Handle File Tree Click"""
        file_info = self.model.fileInfo(index)

        if file_info.isDir():  # If file is Folder then Do nothing
            return

        file_path = file_info.filePath()
        file_name = file_info.fileName()

        text = self.file_ops.read_file(file_path)
        
        if text:
            self.mk_tab(file_name, file_path, text)
    
    
    def get_text(self):
        widget = self.tabs.currentWidget()

        return widget.text() if widget else ""
    
    def get_path(self):
        widget = self.tabs.currentWidget()

        return widget.file_path if widget else None