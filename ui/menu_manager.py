from PyQt6.QtWidgets import QWidget,QMenuBar
from PyQt6.QtGui import QAction

# ============================================================================
# Menu Manager Class
# ============================================================================
class Menumanager(QMenuBar):
    """This Class Manages menu bar creation and action handling."""

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
