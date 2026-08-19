from PyQt6.QtWidgets import QStackedWidget
from ui.BaseWidgets.widget_base import BaseWidget
from ui.components.widgets.file_explorer import FileExplorer
from ui.components.widgets.git_panel import GitPanel

class LeftPanel(BaseWidget):
    """Sidebar file explorer panel."""
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("leftPanel")
        self.setMinimumWidth(220)
        self.setMaximumWidth(400)

        self.stack = QStackedWidget()
        self.add(self.stack)
        
        self.file_explorer = FileExplorer(parent=self)
        self.stack.addWidget(self.file_explorer)
        
        self.git_panel = GitPanel()
        self.stack.addWidget(self.git_panel)

        self._panels = {
            "explorer": 0,
            "git": 1,
        }

    def browse_folder(self):
        self.file_explorer.browse_folder()

    def explorer_file_selected_conn(self, conn):
        self.file_explorer.file_selected.connect(conn)

    def get_panel_index(self, panel_name: str) -> int:
        return self._panels[panel_name]

    def showPanel(self, panel_name: str):
        index = self.get_panel_index(panel_name)
        self.stack.setCurrentIndex(index)