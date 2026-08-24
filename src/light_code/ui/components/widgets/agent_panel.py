# ui/components/widgets/agent_panel.py
from PyQt6.QtWidgets import QLabel
from ui.base_widgets.base_widget import BaseWidget


class AgentPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("agent_panel")
        self.add(QLabel("AGENT PANEL — COMING SOON"))