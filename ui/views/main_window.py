from qframelesswindow import FramelessWindow
from app.config import WINDOW_HEIGHT, WINDOW_WIDTH


class MainWindow(FramelessWindow):
    """
    Main application window containing Editor, Left Panel, 
    Right Panel, Down Panel etc.
    """
    def __init__(self, parent=None):
        """ Initialize the main window """
        super().__init__(parent=parent)
        
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        