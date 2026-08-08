from qframelesswindow import TitleBar
from ui.window_menubar import EditorMenuBar
class WindowTitle(TitleBar):
    """Custom title bar for the Application."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("window_title")
        self.menu_bar = EditorMenuBar(window=parent, parent=self)
        
        self.raise_()

