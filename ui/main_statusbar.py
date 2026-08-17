
from PyQt6.QtWidgets import QPushButton, QStatusBar
from ui.BaseWidgets.custom_button import CustomButton
from ui.BaseWidgets.widget_base import BaseWidget


class StatusBar(QStatusBar):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setFixedHeight(30)

        self.left_panel_buttons = LeftPanelButtons(self)
        self.addWidget(self.left_panel_buttons)

        space = BaseWidget(self)
        space.setFixedWidth(200)
        self.addWidget(space)
        
        self.right_panel_buttons = RightPanelButtons(self)
        self.addWidget(self.right_panel_buttons)


class LeftPanelButtons(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.explorer_btn = CustomButton("E")
        self.add(self.explorer_btn)

        self.git_btn = CustomButton("G")
        self.add(self.git_btn)

    def setExplorerBtnConn(self, func):
        self.explorer_btn.clicked.connect(func)
        
    def setGitBtnConn(self, func):
        self.git_btn.clicked.connect(func)


class RightPanelButtons(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.agent_btn = CustomButton("A")
        self.add(self.agent_btn)

        self.terminal_btn = CustomButton("T")
        self.add(self.terminal_btn)

    def setAgentBtnConn(self, func):
        self.agent_btn.clicked.connect(func)

    def setTerminalBtnConn(self, func):
        self.terminal_btn.clicked.connect(func)
