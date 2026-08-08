from qframelesswindow import StandardTitleBar
from ui.window_menubar import EditorMenuBar


class WindowTitle(StandardTitleBar):
    """Custom title bar for the Application."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("window_title")
        self.setTitle("PyCode")
        self.menu_bar = EditorMenuBar(window=parent)

        self.hBoxLayout.insertWidget(3, self.menu_bar) 
        self.raise_()