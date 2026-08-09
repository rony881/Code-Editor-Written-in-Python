from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)
from ui.BaseWidgets import BaseWidget


class DummySidePanel(BaseWidget):
    """Dummy file explorer panel for testing."""

    fileDoubleClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = CaptionLabel("EXPLORER", self)
        self.fileList = QListWidget(self)

        self._add_files()

        self.add(self.titleLabel)
        self.add(self.fileList)

        self.fileList.itemDoubleClicked.connect(self._onDoubleClicked)

    def _add_files(self):
        files = [
            "📁 src",
            "    📄 main.py",
            "    📄 editor.py",
            "    📄 window.py",
            "📁 ui",
            "    📄 sidebar.py",
            "    📄 titlebar.py",
            "📄 README.md",
            "📄 config.py",
        ]

        for file in files:
            self.fileList.addItem(file)

    def _onDoubleClicked(self, item: QListWidgetItem):
        if "📁" in item.text():
            return

        filename = item.text().strip()
        filename = filename.replace("📄", "").strip()

        self.fileDoubleClicked.emit(
            f"C:/DummyProject/{filename}"
        )


class DummyEditor(QWidget):
    """Dummy code editor for testing."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = CaptionLabel("EDITOR", self)

        self.editor = QPlainTextEdit(self)
        self.editor.setPlainText(
            '''def main():
    print("Hello, world!")


if __name__ == "__main__":
    main()
'''
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.editor)


class DummyAgentPanel(QWidget):
    """Dummy AI agent panel for testing."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = CaptionLabel("AGENT", self)

        self.chat = QPlainTextEdit(self)
        self.chat.setReadOnly(True)
        self.chat.setPlainText(
            "Agent: Hello! How can I help you?\n\n"
            "Agent: This is a dummy agent panel."
        )

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Ask the agent...")

        self.sendButton = PrimaryPushButton("Send", self)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.chat)
        layout.addWidget(self.input)
        layout.addWidget(self.sendButton)

        self.sendButton.clicked.connect(self._send_message)
        self.input.returnPressed.connect(self._send_message)

    def _send_message(self):
        message = self.input.text().strip()

        if not message:
            return

        self.chat.appendPlainText(
            f"\nYou: {message}\n"
            "Agent: This is a dummy response."
        )

        self.input.clear()