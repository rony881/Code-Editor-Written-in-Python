from PyQt6.QtWidgets import QHBoxLayout, QStackedWidget

from ui.BaseWidgets.custom_button import CustomButton
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

        self.stack = QStackedWidget()
        self.add(self.stack)
        
        self.file_explorer = FileExplorer()
        self.stack.addWidget(self.file_explorer)
        
        self.git_panel = GitPanel()
        self.stack.addWidget(self.git_panel)

        self.agent_panel = AgentPanel()
        self.stack.addWidget(self.agent_panel)

        self.terminal_panel = TerminalPanel()
        self.stack.addWidget(self.terminal_panel)

        self.btn_area = QHBoxLayout()
        self.add(self.btn_area)

        explorer_btn = CustomButton("E")
        explorer_btn.clicked.connect(lambda: self.showPanel("File Explorer"))
        
        git_btn = CustomButton("G")
        git_btn.clicked.connect(lambda: self.showPanel("Git Panel"))
        
        agent_btn = CustomButton("A")
        agent_btn.clicked.connect(lambda: self.showPanel("Agent Panel"))
        
        terminal_btn = CustomButton("T")
        terminal_btn.clicked.connect(lambda: self.showPanel("Terminal Panel"))

        self.btn_area.addWidget(explorer_btn)
        self.btn_area.addWidget(git_btn)
        self.btn_area.addWidget(agent_btn)
        self.btn_area.addWidget(terminal_btn)
        
    def showPanel(self, panel_name: str):
        index = Panels[panel_name]
        self.stack.setCurrentIndex(index)