APP_MENUBAR_STYLE = """
    color: gray;
"""

APP_TITLE_BAR = """
    color: #cdcdcd;
"""

"""Carbon Editor — Theme & Stylesheet Module"""

DARK_STYLESHEET = """
QMainWindow {
    background-color: #0d1117;
    color: #c9d1d9;
}
QWidget#activity_bar {
    background-color: #161b22;
    border-top: 1px solid #21262d;

}
QMenuBar {
    background-color: #161b22;
    color: #c9d1d9;
    border-bottom: 1px solid #21262d;
    padding: 2px 0;
    font-size: 13px;
}
QMenuBar::item {
    padding: 6px 12px;
    border-radius: 6px;
    margin: 2px 1px;
}
QMenuBar::item:selected {
    background-color: #1f6feb33;
    color: #58a6ff;
}
QMenu {
    background-color: #1c2128;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 4px;
}
QMenu::item {
    padding: 8px 32px 8px 16px;
    border-radius: 4px;
    margin: 1px 4px;
}
QMenu::item:selected {
    background-color: #1f6feb44;
    color: #58a6ff;
}
QMenu::separator {
    height: 1px;
    background: #21262d;
    margin: 4px 12px;
}
QTabWidget::pane {
    border: none;
    background: #0d1117;
}
QTabBar {
    background: #161b22;
    border-bottom: 1px solid #21262d;
}
QTabBar::tab {
    background: #161b22;
    color: #8b949e;
    padding: 10px 20px;
    border: none;
    border-bottom: 2px solid transparent;
    min-width: 120px;
    font-size: 13px;
}
QTabBar::tab:selected {
    color: #f0f6fc;
    border-bottom: 2px solid #1f6feb;
    background: #0d1117;
}
QTabBar::tab:hover:!selected {
    color: #c9d1d9;
    background: #1c2128;
}
QTabBar::close-button {
    image: none;
    subcontrol-position: right;
}
QToolBar {
    background: #161b22;
    border-bottom: 1px solid #21262d;
    padding: 4px 8px;
    spacing: 4px;
}
QToolButton {
    background: transparent;
    color: #8b949e;
    border: none;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
}
QToolButton:hover {
    background: #1f6feb33;
    color: #58a6ff;
}
QToolButton:pressed {
    background: #1f6feb55;
}
QStatusBar {
    background: #161b22;
    color: #8b949e;
    border-top: 1px solid #21262d;
    font-size: 12px;
    padding: 2px 8px;
}
QStatusBar::item { border: none; }
QStatusBar QLabel {
    color: #8b949e;
    padding: 2px 10px;
    font-size: 12px;
}
QTreeView {
    background: #0d1117;
    color: #c9d1d9;
    border: none;
    font-size: 13px;
    outline: none;
}
QTreeView::item {
    padding: 5px 4px;
    border-radius: 4px;
    margin: 1px 4px;
}
QTreeView::item:selected {
    background: #1f6feb33;
    color: #58a6ff;
}
QTreeView::item:hover:!selected {
    background: #1c2128;
}
QTreeView::branch { border-image: none; image: none; }
QHeaderView::section {
    background: #161b22;
    color: #8b949e;
    border: none;
    padding: 6px 8px;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
QSplitter::handle {
    background: #21262d;
    width: 1px;
    height: 1px;
}
QLineEdit {
    background: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
    selection-background-color: #1f6feb55;
}
QLineEdit:focus {
    border-color: #1f6feb;
}
QPushButton {
    background: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 16px;
    font-size: 13px;
}
QPushButton:hover {
    background: #30363d;
    border-color: #8b949e;
}
QPushButton:pressed {
    background: #1f6feb44;
}
QPushButton#accentBtn {
    background: #1f6feb;
    color: #ffffff;
    border: none;
    font-weight: 600;
}
QPushButton#accentBtn:hover {
    background: #388bfd;
}
QPlainTextEdit {
    background: #0d1117;
    color: #a1f0a1;
    border: none;
    font-family: 'Cascadia Code', 'Consolas', monospace;
    font-size: 13px;
    selection-background-color: #1f6feb44;
}
QScrollBar:vertical {
    background: #0d1117;
    width: 10px;
    border: none;
}
QScrollBar::handle:vertical {
    background: #30363d;
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover { background: #484f58; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QScrollBar:horizontal {
    background: #0d1117;
    height: 10px;
    border: none;
}
QScrollBar::handle:horizontal {
    background: #30363d;
    border-radius: 5px;
    min-width: 30px;
}
QScrollBar::handle:horizontal:hover { background: #484f58; }
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; }
QLabel {
    color: #8b949e;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 12px 16px 8px 16px;
}
QFrame#findBar {
    background: #1c2128;
    border: 1px solid #30363d;
    border-radius: 8px;
}
QFrame#welcomeFrame {
    background: #0d1117;
}
QLabel#welcomeTitle {
    color: #f0f6fc;
    font-size: 32px;
    font-weight: 700;
}
QLabel#welcomeSubtitle {
    color: #8b949e;
    font-size: 15px;
}
QPushButton#welcomeBtn {
    background: #161b22;
    color: #c9d1d9;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 14px 24px;
    font-size: 14px;
    text-align: left;
    min-width: 260px;
}
QPushButton#welcomeBtn:hover {
    background: #1c2128;
    border-color: #1f6feb;
    color: #58a6ff;
}
"""

# Scintilla editor colors
EDITOR_COLORS = {
    "paper": "#0d1117",
    "default_text": "#c9d1d9",
    "margin_bg": "#161b22",
    "margin_fg": "#484f58",
    "caret": "#58a6ff",
    "caret_line_bg": "#161b2299",
    "selection_bg": "#1f6feb44",
    "fold_margin_bg": "#0d1117",
    "matched_brace_fg": "#79c0ff",
    "matched_brace_bg": "#1f6feb33",
    "unmatched_brace_fg": "#f85149",
    "edge_color": "#21262d",
    "indent_guide": "#21262d",
}

# C/C++ Lexer colors
CPP_LEXER_COLORS = {
    "Comment":        "#8b949e",
    "CommentLine":    "#8b949e",
    "CommentDoc":     "#8b949e",
    "Number":         "#79c0ff",
    "Keyword":        "#ff7b72",
    "DoubleQuotedString": "#a5d6ff",
    "SingleQuotedString": "#a5d6ff",
    "UUID":           "#d2a8ff",
    "PreProcessor":   "#d2a8ff",
    "Operator":       "#79c0ff",
    "Identifier":     "#c9d1d9",
    "UnclosedString": "#f85149",
    "GlobalClass":    "#ffa657",
    "InactiveDefault":"#484f58",
    "KeywordSet2":    "#ffa657",
    "CommentDocKeyword": "#7ee787",
}

EDITOR_FONT_FAMILY = "Cascadia Code, Fira Code, Consolas, Courier New, monospace"
EDITOR_FONT_SIZE = 12
