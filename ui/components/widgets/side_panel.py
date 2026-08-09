from ui.BaseWidgets import BaseWidget


class SidePanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setMinimumWidth(220)
        self.setMaximumWidth(400)