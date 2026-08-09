from PyQt6.QtWidgets import QStackedWidget

from ui.BaseWidgets.widget_base import BaseWidget
from ui.components.widgets.agent_panel import AgentPanel
from ui.components.widgets.file_explorer import FileExplorer
from ui.components.widgets.git_panel import GitPanel
from ui.components.widgets.terminal_panel import TerminalPanel

Panels = {
    "File Explorer": 0,
    "Git Panel": 1,
    "Agent Panel": 2,
    "Terminal Panel": 3,
}

class LeftPanel(BaseWidget):
    """Sidebar file explorer panel."""
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("leftPanel")
        self.setMinimumWidth(220)
        self.setMaximumWidth(400)

        self.file_explorer = FileExplorer()
        self.git_panel = GitPanel()
        self.agent_panel = AgentPanel()
        self.terminal_panel = TerminalPanel()

        self.stack = QStackedWidget()

        self.stack.addWidget(self.file_explorer)
        self.stack.addWidget(self.git_panel)
        self.stack.addWidget(self.agent_panel)
        self.stack.addWidget(self.terminal_panel)

        self.add(self.stack)

    def showPanel(self, panel_name: str):
        index = Panels[panel_name]
        self.stack.setCurrentIndex(index)