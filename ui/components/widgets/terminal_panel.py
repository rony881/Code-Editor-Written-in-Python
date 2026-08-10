# ui/components/widgets/git_panel.py
from PyQt6.QtWidgets import QLabel
from ui.BaseWidgets.widget_base import BaseWidget


class TerminalPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("terminal_panel")
        self.add(QLabel("TERMINAL PANEL — COMING SOON"))