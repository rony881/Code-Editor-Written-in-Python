from qframelesswindow import StandardTitleBar
from ui.themes.color_theme import APP_TITLE_BAR
from ui.window_menubar import EditorMenuBar


class WindowTitle(StandardTitleBar):
    """Custom title bar for the Application."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("window_title")
        self.setStyleSheet(APP_TITLE_BAR)
        self.setTitle("PyCode")
        self.setIcon("resources/icons/logo.png")
        self.menu_bar = EditorMenuBar(window=parent, parent=self)
        self.hBoxLayout.insertWidget(3,self.menu_bar)
        self.raise_()