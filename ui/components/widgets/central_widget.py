from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSplitter, QVBoxLayout, QWidget

from ui.components.panels.central_panel import CentralPanel
from ui.components.panels.left_panel import LeftPanel
from ui.components.panels.right_panel import RightPanel


class CentralWidget(QWidget):
    """
    Owns the main splitter: LeftPanel (explorer) | CentralPanel (editor) | RightPanel (agent).
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(self.splitter, 1)

        self.left_panel = LeftPanel()
        self.central_panel = CentralPanel()
        self.right_panel = RightPanel()

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.central_panel)
        self.splitter.addWidget(self.right_panel)
        self.splitter.setSizes([260, 900, 280])