from PyQt6.QtWidgets import QHBoxLayout, QStackedWidget

from ui.BaseWidgets.custom_button import CustomButton
from ui.BaseWidgets.widget_base import BaseWidget
from ui.components.widgets.agent_panel import AgentPanel
from ui.components.widgets.terminal_panel import TerminalPanel

Panels = {
    "Agent Panel": 0,
    "Terminal Panel": 1,
}

class RightPanel(BaseWidget):
    """Right-hand agent/assistant panel."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("rightPanel")
        self.setMinimumWidth(260)
        self.setMaximumWidth(480)

        self.stack = QStackedWidget()
        self.add(self.stack)

        self.agent_panel = AgentPanel()
        self.stack.addWidget(self.agent_panel)

        self.terminal_panel = TerminalPanel()
        self.stack.addWidget(self.terminal_panel)

        self.btn_area = QHBoxLayout()
        self.add(self.btn_area)

        agent_btn = CustomButton("A")
        agent_btn.clicked.connect(lambda: self.showPanel("Agent Panel"))
        
        terminal_btn = CustomButton("T")
        terminal_btn.clicked.connect(lambda: self.showPanel("Terminal Panel"))

        self.btn_area.addWidget(agent_btn)
        self.btn_area.addWidget(terminal_btn)

    def showPanel(self, panel_name: str):
        index = Panels[panel_name]
        self.stack.setCurrentIndex(index)