import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QSplitter, QWidget
from qframelesswindow import FramelessWindow

from app.config import WINDOW_HEIGHT, WINDOW_WIDTH
from ui.base_widgets.menu_manager import Menumanager
from ui.widgets.window_title import WindowTitle


class MainWindow(FramelessWindow):
    """
    Main application window containing TitleBar, Editor,
    Left Panel, Right Panel, Down Panel etc.
    """
    def __init__(self, parent=None):
        """ Initialize the main window """
        super().__init__(parent=parent)
        self.window_title = WindowTitle(self)
        self.setTitleBar(self.window_title)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.menu_bar = Menumanager()
        