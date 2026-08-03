from qfluentwidgets import FluentWindow

from app.config import WINDOW_HEIGHT, WINDOW_WIDTH


class MainWindow(FluentWindow):
    """
    Main application window containing Editor, Left Panel, 
    Right Panel, Down Panel etc.
    """

    def __init__(self):
        """ Initialize the main window """
        super().__init__()
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        