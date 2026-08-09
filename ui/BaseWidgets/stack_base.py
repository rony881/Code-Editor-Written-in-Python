import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)

from ui.BaseWidgets.widget_base import BaseWidget


class StackBaseWidget(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        
    