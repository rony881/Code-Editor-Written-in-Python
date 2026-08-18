from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QStatusBar, QWidget

from ui.BaseWidgets.custom_button import CustomButton

BUTTON_STYLE = """
QPushButton {
    background: transparent;
    color: #8b949e;
    border: none;
    border-radius: 3px;
    padding: 0px 6px;
    font-size: 12px;
}
QPushButton:hover {
    background: #30363d;
    color: #e6edf3;
}
QPushButton:pressed {
    background: #21262d;
    color: #e6edf3;
}
"""

LABEL_STYLE = "color: #8b949e; font-size: 12px; padding: 0px 4px;"

SEPARATOR_STYLE = "QFrame { background-color: #30363d; border: none; }"


class StatusBar(QStatusBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setFixedHeight(30)
        self.setSizeGripEnabled(False)

        # Container widget to hold the status bar content
        self.container_widget = QWidget()
        self.h_layout = QHBoxLayout(self.container_widget)
        self.h_layout.setContentsMargins(4, 0, 4, 0)
        self.h_layout.setSpacing(2)

        # Left panel buttons
        self.left_panel_buttons = LeftPanelButtons()
        self.h_layout.addWidget(self.left_panel_buttons)

        self.h_layout.addSpacing(8)

        # Status message label
        self.status_message_label = QLabel("Ready")
        self.status_message_label.setStyleSheet(
            "color: #c9d1d9; font-size: 12px; padding: 0px 4px;"
        )
        self.h_layout.addWidget(self.status_message_label)

        self.h_layout.addStretch()

        # Language label
        self.language_label = QLabel("Plain Text")
        self.language_label.setToolTip("Language Mode")
        self.language_label.setStyleSheet(LABEL_STYLE)
        self.h_layout.addWidget(self.language_label)

        # Indent label
        self.indent_label = QLabel("Spaces: 4")
        self.indent_label.setToolTip("Indentation")
        self.indent_label.setStyleSheet(LABEL_STYLE)
        self.h_layout.addWidget(self.indent_label)

        # Encoding label
        self.encoding_label = QLabel("UTF-8")
        self.encoding_label.setToolTip("Encoding")
        self.encoding_label.setStyleSheet(LABEL_STYLE)
        self.h_layout.addWidget(self.encoding_label)

        # Cursor label
        self.cursor_label = QLabel("Ln 1, Col 1")
        self.cursor_label.setToolTip("Cursor Position")
        self.cursor_label.setStyleSheet(LABEL_STYLE)
        self.h_layout.addWidget(self.cursor_label)

        self.h_layout.addSpacing(8)

        # Right panel buttons
        self.right_panel_buttons = RightPanelButtons()
        self.h_layout.addWidget(self.right_panel_buttons)

        self.addWidget(self.container_widget, 1)

    # Connects the explorer button to a function
    def setExplorerBtnConn(self, func):
        self.left_panel_buttons.explorer_btn.clicked.connect(func)
    
    # Connects the git button to a function
    def setGitBtnConn(self, func):
        self.left_panel_buttons.git_btn.clicked.connect(func)

    # Connects the agent button to a function
    def setAgentBtnConn(self, func):
        self.right_panel_buttons.agent_btn.clicked.connect(func)

    # Connects the terminal button to a function
    def setTerminalBtnConn(self, func):
        self.right_panel_buttons.terminal_btn.clicked.connect(func)

    def set_status_message(self, message: str) -> None:
        self.status_message_label.setText(message)

    def set_cursor_position(self, line: int, column: int) -> None:
        self.cursor_label.setText(f"Ln {line}, Col {column}")

    def set_language(self, language: str) -> None:
        self.language_label.setText(language)

    def set_encoding(self, encoding: str) -> None:
        self.encoding_label.setText(encoding)

    def set_indentation(self, text: str) -> None:
        self.indent_label.setText(text)


class LeftPanelButtons(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)

        self.explorer_btn = CustomButton("E")
        self.explorer_btn.setToolTip("Explorer")
        self.explorer_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.explorer_btn)

        self.git_btn = CustomButton("G")
        self.git_btn.setToolTip("Source Control")
        self.git_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.git_btn)


class RightPanelButtons(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)

        self.agent_btn = CustomButton("A")
        self.agent_btn.setToolTip("AI Agent")
        self.agent_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.agent_btn)

        self.terminal_btn = CustomButton("T")
        self.terminal_btn.setToolTip("Terminal")
        self.terminal_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.terminal_btn)
