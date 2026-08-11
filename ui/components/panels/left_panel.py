from PyQt6.QtWidgets import QHBoxLayout, QStackedWidget

from ui.BaseWidgets.custom_button import CustomButton
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
        
        self.file_explorer = FileExplorer()
        self.stack.addWidget(self.file_explorer)
        
        self.git_panel = GitPanel()
        self.stack.addWidget(self.git_panel)

        self._panels = {
            "File Explorer": 0,
            "Git Panel": 1,
        }

        self.btn_area = QHBoxLayout()
        self.add(self.btn_area)

        explorer_btn = CustomButton("E")
        explorer_btn.clicked.connect(lambda: self.showPanel("File Explorer"))
        
        git_btn = CustomButton("G")
        git_btn.clicked.connect(lambda: self.showPanel("Git Panel"))

        self.btn_area.addWidget(explorer_btn)
        self.btn_area.addWidget(git_btn)
        self.btn_area.addStretch()

    def get_panel_index(self, panel_name: str) -> int:
        return self._panels[panel_name]

    def showPanel(self, panel_name: str):
        index = self.get_panel_index(panel_name)
        self.stack.setCurrentIndex(index)