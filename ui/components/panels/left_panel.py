from ui.BaseWidgets.widget_base import BaseWidget
from ui.components.widgets.file_explorer import FileExplorer


class LeftPanel(BaseWidget):
    """Sidebar file explorer panel."""
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("leftPanel")
        self.setMinimumWidth(220)
        self.setMaximumWidth(400)
        self.file_explorer = FileExplorer(self)
        self.add(self.file_explorer)