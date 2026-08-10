from PyQt6.QtWidgets import QHBoxLayout

from ui.BaseWidgets.custom_button import CustomButton
from ui.BaseWidgets.widget_base import BaseWidget


class StatusBar(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("activity_bar")
        self.setFixedHeight(30)

        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(5,0,0,0)
        self.h_layout.setSpacing(0)
        self.add(self.h_layout)

        explorer_btn = CustomButton("E")
        git_btn = CustomButton("G")
        agent_btn = CustomButton("A")
        terminal_btn = CustomButton("T")

        self.h_layout.addWidget(explorer_btn)
        self.h_layout.addWidget(git_btn)
        self.h_layout.addWidget(agent_btn)
        self.h_layout.addWidget(terminal_btn)
        self.h_layout.addStretch(1)
        