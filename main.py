from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QMenuBar)
from PyQt6.QtGui import (
    QAction
)
from PyQt6.QtCore import Qt, QPoint
import sys


# ============================================================================
# Window Title Class
# ============================================================================


class Window_title(QFrame):
    """This Class Creates a Custom Window Title"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.drag_pos = QPoint()
        self.setObjectName("titlebar")
        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.setLayout(layout)

        layout.addStretch()

        # Min Button
        self.min_btn = QPushButton("—")
        self.min_btn.clicked.connect(self.parent().showMinimized)
        layout.addWidget(self.min_btn)

        # Max Button
        self.max_btn = QPushButton("□")
        self.max_btn.clicked.connect(self.toggle_max_restore)
        self.max_btn.setObjectName("maxbtn")
        layout.addWidget(self.max_btn)
        
        # Close Button
        self.close_btn = QPushButton("✕")
        self.close_btn.clicked.connect(self.parent().close)
        self.close_btn.setObjectName("closebtn")
        layout.addWidget(self.close_btn)

    def toggle_max_restore(self):
        """This Method Handles Window Fullscreen Action"""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()

    # Window Dragging Methods:
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = (
                event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.parent().move(event.globalPosition().toPoint() - self.drag_pos)


# ============================================================================
# Mainwindow Class
# ============================================================================


class MainWindow(QWidget):
    """Main application window."""

    def __init__(self):
        super().__init__()

        # Window configuration
        self.setObjectName("container")
        self.resize(800, 600)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.title = Window_title(self)

        # Layout configuration
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_layout.addWidget(self.title)
        self.main_layout.addStretch()

# ============================================================================
# Menu Manager Class
# ============================================================================
class Menumanager(QMenuBar):
    """Manages menu bar creation and action handling."""

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



# =============================================================================
# Run App
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())