from PyQt6.Qsci import QsciScintilla,QsciLexerPython
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
    QTreeView,
    QFileDialog
    )
from PyQt6.QtGui import (
    QAction,
    QFileSystemModel,
    QColor,
    QFont
)
from PyQt6.QtCore import Qt, QPoint
import sys,os

DEFAULT_FONT_NAME = "Consolas"
DEFAULT_FONT_SIZE = 11
STYLESHEET = "style.qss"



# Syntax highlighting colors

SYNTAX_COLORS_1 = {
    "default": "#bb6afe",  # Text
    "background": "#1e1e1e",  # Base
    "keyword": "#ff8f40",  # Pink
    "number": "#d2a6ff",  # Peach
    "function": "#ffb454",  # Blue
    "class": "#67f6d7",  # Mauve
    "operator": "#f29668",  # Yellowz
    "identifier": "#dadada",  # Lavender
    "decorator": "#e69d95",  # Rosewater
    "comment": "#5a6673",  # Subtext 0
    "string": "#b7ef47",  # Green
    "line_number_fg": "#363636",  # Overlay 0
    "line_number_bg": "#1e1e1e",  # Base
    "caret_line_bg": "#454444",  # Surface 0
    "caret_fg": "#fe8f40",  # Sky
}


# ============================================================================
# Window Title Class
# ============================================================================

class Window_title(QFrame):
    """This Class Creats a Custom Window Title"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)  # Pass parent to Qt so self.parent() works

        self.drag_pos = QPoint()
        self.setObjectName("titlebar")  # Object name
        self.setFixedHeight(30)  # Height of the title Bar

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
    """Main application window."""

    def __init__(self):
        super().__init__()

        # Window configuration
        self.setObjectName("container")
        self.resize(800, 600)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.title = Window_title(self) # <- Title Bar

        # File TreeView
        self.tree = QTreeView()
        self.tree.setObjectName("treeview")
        self.tree.clicked.connect(self.on_file_click)

        # This Will Use For File Operations
        self.file_ops = FileOps(self)

        # My Working Directory
        self.current_working_dir = r"C:\Users\Lenovo\OneDrive\文件\Projects\Text Editor"

        # This Will Keep tarck of Opened Tabs and Files
        self.open_files = {}
        self.open_tabs = {}

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

        self._setup_tabs()
        self._setup_splitter()
        self._setup_layout()
        self._setup_menubar()
        self.mk_tree(self.current_working_dir)
        self.setStylesheet(STYLESHEET)

    def setStylesheet(self, styleSheet):
        """Set The SyleSheeet To The Application"""

        style_sheet = self.file_ops.read_file(STYLESHEET)

        if style_sheet:
            self.setStyleSheet(style_sheet)
    
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
                ("Zen Mode", None, None),
                ("Open Terminal", None, "Ctrl+'"),
                "separator",
                ("Toggle Sidebar", None, None),
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
    
    def mk_tree(self, file_path):
        self.model = QFileSystemModel()

        self.model.setRootPath(file_path)
        self.model.setIconProvider(None)  # Remove Folder and File Icons

        # tree configaretion
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(file_path))
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)  # Hide Extra Column
        self.tree.hideColumn(3)
        self.tree.setAnimated(True)
        self.tree.setIndentation(10)
        self.tree.setMinimumWidth(170)
        self.tree.setItemsExpandable(True)
        self.tree.setRootIsDecorated(False)
        self.tree.setHeaderHidden(False)  # Hide the File Header

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

        self.open_files[file_path] = tab_index
        self.open_tabs[file_path] = new_tab
        self.tabs.setCurrentIndex(tab_index)
    
    def get_text(self):
        widget = self.tabs.currentWidget()

        return widget.text() if widget else ""
    
    def get_path(self):
        widget = self.tabs.currentWidget()

        return widget.file_path if widget else None
    

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
        self.setMarginsFont(
            QFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)
        )  # line Number Forground Font
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setTabWidth(4)

        # Line Number Forground And Background Color:
        self.setMarginsForegroundColor(
            QColor(SYNTAX_COLORS_1["line_number_fg"])
        )  # line Number Forground Color
        self.setMarginsBackgroundColor(
            QColor(SYNTAX_COLORS_1["line_number_bg"])
        )  # line Number Background Color
        self.setUtf8(True)

        # Caret Line Back and Foreground:
        self.setCaretLineBackgroundColor(QColor(SYNTAX_COLORS_1["caret_line_bg"]))
        self.setCaretForegroundColor(QColor(SYNTAX_COLORS_1["caret_fg"]))
        self.setCaretLineVisible(True)

        # Auto-completion:
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(False)

        # Indentation Guide
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuidesBackgroundColor(QColor("#363636"))  # Indentation line background Color
        self.setIndentationGuidesForegroundColor(QColor("#363636"))  # Indentation line Foregorund Color
        self.setCaretWidth(2)  # Cursor Width

    def syntax_color(self):
        """Seting Python Syntax Highlighting"""

        lexer = QsciLexerPython(self)

        font = QFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)  # Editor's Default Font
        lexer.setDefaultFont(font)

        # Backgorund and Foreground Colors of Editor
        lexer.setDefaultPaper(QColor(SYNTAX_COLORS_1["background"]))  # Background
        lexer.setDefaultColor(QColor(SYNTAX_COLORS_1["default"]))  # Foregorund

        # Configure syntax colors
        color_config = [
            (SYNTAX_COLORS_1["default"], QsciLexerPython.Default),
            (SYNTAX_COLORS_1["keyword"], QsciLexerPython.Keyword),
            (SYNTAX_COLORS_1["number"], QsciLexerPython.Number),
            (SYNTAX_COLORS_1["function"], QsciLexerPython.FunctionMethodName),
            (SYNTAX_COLORS_1["class"], QsciLexerPython.ClassName),
            (SYNTAX_COLORS_1["operator"], QsciLexerPython.Operator),
            (SYNTAX_COLORS_1["identifier"], QsciLexerPython.Identifier),
            (SYNTAX_COLORS_1["decorator"], QsciLexerPython.Decorator),
            (SYNTAX_COLORS_1["comment"], QsciLexerPython.Comment),
            (SYNTAX_COLORS_1["comment"], QsciLexerPython.CommentBlock),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.SingleQuotedString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.SingleQuotedFString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.DoubleQuotedString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.DoubleQuotedFString),
            ("#8c8b88", QsciLexerPython.TripleSingleQuotedFString),
            ("#8c8b88", QsciLexerPython.TripleDoubleQuotedString),
        ]

        for color, syntax in color_config:
            lexer.setColor(QColor(color), syntax)
            lexer.setFont(font, syntax)

        return lexer

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

# ============================================================================
# File Operation Class
# ============================================================================
class FileOps:
    """ This Class Handle File Operations """
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent

    def read_file(self,file_path):
        """ This Method Reads a File And Returns Its Content """
        try:
            with open(file_path,"r",encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            return content
        
    def write_file(self,file_path,content):
        """ This Method Writes a File """
        try:
            with open(file_path,"w",encoding="utf-8",newline="") as f:
                f.write(content)
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            return True

    def open_file(self):
        """This Method Open File"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent,
            self.parent.file_filter,
        )
        file_name = os.path.basename(file_path)

        if not file_path:
            return
        
        self.parent.path = file_path

        text = self.read_file(file_path)
        if text:
            self.parent.mk_tab(file_name, file_path, text)
            print(f"{file_name} was opened")

    def open_folder(self):
        """This Method Open Folder"""

        file_path = QFileDialog.getExistingDirectory(self.parent, "Open Folder")
        if not file_path:
            return

        self.parent.mk_tree(file_path)

    def new_file(self):
        name = "Untitled.py"
        text = ""

        path = os.path.join(self.parent.current_working_dir, name)

        counter = 1
        while path in self.parent.open_tabs:
            path = os.path.join(self.parent.current_working_dir, f"Untitled_{counter}.py")
            counter += 1

        self.parent.mk_tab(os.path.basename(path), path, text)

    def save_file(self,file_path=None,content=None):
        """This Method Saves the File"""

        content = self.parent.get_text()
        file_path = self.parent.get_path()

        if not content:
            return

        save = self.write_file(file_path,content)

        if save :
            print("File Saved ✅")

    def save_as(self, index):

        content = self.parent.get_text()

        file_path, _ = QFileDialog.getSaveFileName(self.parent, "", "Untitled.py")

        if not file_path:
            return
        
        self.save_file(file_path,content)
        

# =============================================================================
# Run App
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())