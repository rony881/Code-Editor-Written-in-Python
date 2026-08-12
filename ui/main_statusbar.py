
from PyQt6.QtWidgets import QPushButton, QStatusBar


class StatusBar(QStatusBar):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setFixedHeight(30)

        