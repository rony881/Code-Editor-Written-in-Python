from PyQt6.Qsci import QsciScintilla, QsciLexerPython
from PyQt6.QtGui import QColor, QFont

from config import (
    DEFAULT_FONT_NAME,
    DEFAULT_FONT_SIZE,
)
from themes.color_theme import SYNTAX_COLORS_1

# ============================================================================
# Main Editor Class
# ============================================================================

class Editor(QsciScintilla):
    """The Editor Inharet From QSciScintilla(Code Editor) Class"""

    def __init__(self):
        super().__init__()
        self.setObjectName("Editor")
        lexer = self.syntax_color()
        self.setLexer(lexer)

        self.setMarginWidth(0, "00000")
        self.setMarginsFont(
            QFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)
        )  # line Number Forground Font
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setTabWidth(4)

        # Line Number Forground And Background Color:
        self.setMarginsForegroundColor(
            QColor(SYNTAX_COLORS_1["line_number_fg"])
        )  # line Number Forground Color
        self.setMarginsBackgroundColor(
            QColor(SYNTAX_COLORS_1["line_number_bg"])
        )  # line Number Background Color
        self.setUtf8(True)

        # Caret Line Back and Foreground:
        self.setCaretLineBackgroundColor(QColor(SYNTAX_COLORS_1["caret_line_bg"]))
        self.setCaretForegroundColor(QColor(SYNTAX_COLORS_1["caret_fg"]))
        self.setCaretLineVisible(True)

        # Auto-completion:
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(False)

        # Indentation Guide
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuidesBackgroundColor(QColor("#363636"))  # Indentation line background Color
        self.setIndentationGuidesForegroundColor(QColor("#363636"))  # Indentation line Foregorund Color
        self.setCaretWidth(2)  # Cursor Width

    def syntax_color(self):
        """Seting Python Syntax Highlighting"""

        lexer = QsciLexerPython(self)

        font = QFont(DEFAULT_FONT_NAME)  # Editor's Default Font
        lexer.setDefaultFont(font)

        # Backgorund and Foreground Colors of Editor
        lexer.setDefaultPaper(QColor(SYNTAX_COLORS_1["background"]))  # Background
        lexer.setDefaultColor(QColor(SYNTAX_COLORS_1["default"]))  # Foregorund

        # Configure syntax colors
        color_config = [
            (SYNTAX_COLORS_1["default"], QsciLexerPython.Default),
            (SYNTAX_COLORS_1["keyword"], QsciLexerPython.Keyword),
            (SYNTAX_COLORS_1["number"], QsciLexerPython.Number),
            (SYNTAX_COLORS_1["function"], QsciLexerPython.FunctionMethodName),
            (SYNTAX_COLORS_1["class"], QsciLexerPython.ClassName),
            (SYNTAX_COLORS_1["operator"], QsciLexerPython.Operator),
            (SYNTAX_COLORS_1["identifier"], QsciLexerPython.Identifier),
            (SYNTAX_COLORS_1["decorator"], QsciLexerPython.Decorator),
            (SYNTAX_COLORS_1["comment"], QsciLexerPython.Comment),
            (SYNTAX_COLORS_1["comment"], QsciLexerPython.CommentBlock),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.SingleQuotedString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.SingleQuotedFString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.DoubleQuotedString),
            (SYNTAX_COLORS_1["string"], QsciLexerPython.DoubleQuotedFString),
            ("#8c8b88", QsciLexerPython.TripleSingleQuotedFString),
            ("#8c8b88", QsciLexerPython.TripleDoubleQuotedString),
        ]

        for color, syntax in color_config:
            lexer.setColor(QColor(color), syntax)
            lexer.setFont(font, syntax)

        return lexer