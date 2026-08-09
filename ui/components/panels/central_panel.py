from PyQt6.QtWidgets import QTabWidget

from ui.BaseWidgets.widget_base import BaseWidget


class CentralPanel(BaseWidget):
    """Editor area: tabbed code editors (+ terminal later)."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("centralPanel")

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.tabCloseRequested.connect(self._close_tab)
        self.add(self.tab_widget)

    def _close_tab(self, index: int) -> None:
        widget = self.tab_widget.widget(index)
        self.tab_widget.removeTab(index)
        if widget is not None:
            widget.deleteLater()