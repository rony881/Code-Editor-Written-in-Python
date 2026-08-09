# ui/components/widgets/git_panel.py
from PyQt6.QtWidgets import QLabel
from ui.BaseWidgets.widget_base import BaseWidget


class GitPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("git_panel")
        self.add(QLabel("Git panel — coming soon"))