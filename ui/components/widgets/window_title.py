from qframelesswindow import TitleBar
from ui.base.menu_base import MenuBaseWidget

class WindowTitle(TitleBar):
    """Custom title bar for the Application."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("window_title")
        self.menu_bar = MenuBaseWidget(self)
        
        self.raise_()