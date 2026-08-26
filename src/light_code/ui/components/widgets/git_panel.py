# ui/components/widgets/git_panel.py

from PyQt6.QtWidgets import QLabel

from ui.base_widgets.base_widget import BaseWidget
from utils.logger import logger

class GitPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing GitPanel")
        self.setObjectName("git_panel")
        self.add(QLabel("GIT PANEL — COMING SOON"))