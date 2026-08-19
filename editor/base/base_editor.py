
from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QFont


class BaseEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("base_editor")

    def _config(self):
        self.setCaretWidth(2)  # Cursor Width
        self.setUtf8(True)
        self.setTabWidth(4)
        self.setMarginWidth(0, "00000")
        self.setMarginsFont(QFont("Consolas", 12))
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)

        # Auto-completion
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)

        # Indentation Guide
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        