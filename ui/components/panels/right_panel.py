from PyQt6.QtWidgets import QLabel

from ui.BaseWidgets.widget_base import BaseWidget


class RightPanel(BaseWidget):
    """Right-hand agent/assistant panel."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("rightPanel")
        self.setMinimumWidth(260)
        self.setMaximumWidth(480)

        title = QLabel("AGENT")
        title.setObjectName("sidebarTitle")
        self.add(title)