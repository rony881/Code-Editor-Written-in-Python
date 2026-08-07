from qframelesswindow import TitleBar


class WindowTitle(TitleBar):
    """Custom title bar for the Application."""

    def __init__(self, parent):
        super().__init__(parent)
        
        self.raise_()