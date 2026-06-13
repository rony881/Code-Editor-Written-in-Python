from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, QPoint
from ui.menu_manager import Menumanager
# ============================================================================
# Window Title Class
# ============================================================================

class Window_title(QFrame):
    """This Class Creats a Custom Window Title"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)  # Pass parent to Qt so self.parent() works

        self.drag_pos = QPoint()
        self.setObjectName("titlebar")  # Object name
        self.setFixedHeight(35)  # Height of the title Bar

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.setLayout(layout)

        self.topbar = Menumanager(self)
        self.topbar.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        layout.addWidget(self.topbar)
        layout.addStretch()

        # Min Button
        self.min_btn = QPushButton("—")
        self.min_btn.clicked.connect(self.parent().showMinimized)
        layout.addWidget(self.min_btn)
        # Max Button
        self.max_btn = QPushButton("□")
        self.max_btn.clicked.connect(self.toggle_max_restore)
        layout.addWidget(self.max_btn)
        # Close Button
        self.close_btn = QPushButton("✕")
        self.close_btn.clicked.connect(self.parent().close)
        self.close_btn.setObjectName("closebtn")
        layout.addWidget(self.close_btn)

    def toggle_max_restore(self):
        """This Method Handle Window Fullscreen Action"""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()

    # Window Draging Methods :
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = (
                event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.parent().move(event.globalPosition().toPoint() - self.drag_pos)