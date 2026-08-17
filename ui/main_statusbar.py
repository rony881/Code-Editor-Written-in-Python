from PyQt6.QtWidgets import QHBoxLayout, QStatusBar, QWidget

from ui.BaseWidgets.custom_button import CustomButton


class StatusBar(QStatusBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setFixedHeight(30)

        self.container_widget = QWidget()
        self.h_layout = QHBoxLayout(self.container_widget)
        self.h_layout.setContentsMargins(4, 0, 4, 0)
        self.h_layout.setSpacing(2)

        self.left_panel_buttons = LeftPanelButtons()
        self.h_layout.addWidget(self.left_panel_buttons)

        self.h_layout.addStretch()

        self.right_panel_buttons = RightPanelButtons()
        self.h_layout.addWidget(self.right_panel_buttons)

        self.addWidget(self.container_widget)


class LeftPanelButtons(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)

        self.explorer_btn = CustomButton("E")
        self.h_layout.addWidget(self.explorer_btn)

        self.git_btn = CustomButton("G")
        self.h_layout.addWidget(self.git_btn)

    def setExplorerBtnConn(self, func):
        self.explorer_btn.clicked.connect(func)

    def setGitBtnConn(self, func):
        self.git_btn.clicked.connect(func)


class RightPanelButtons(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)

        self.agent_btn = CustomButton("A")
        self.h_layout.addWidget(self.agent_btn)

        self.terminal_btn = CustomButton("T")
        self.h_layout.addWidget(self.terminal_btn)

    def setAgentBtnConn(self, func):
        self.agent_btn.clicked.connect(func)

    def setTerminalBtnConn(self, func):
        self.terminal_btn.clicked.connect(func)