from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class BaseWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("panel")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet(
            """
            QWidget#panel {
                background-color: red;
                border: 1px solid gray;
                border-radius: 60px;
            }
            """
        )

    def add(self, item):
        if isinstance(item, QVBoxLayout):
            self.main_layout.addLayout(item)
        elif isinstance(item, QWidget):
            self.main_layout.addWidget(item)