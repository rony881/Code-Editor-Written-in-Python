# src/light_code/ui/views/editor_area.py

from editor.editor import BaseEditor
from ui.base_widgets.tab_base import TabBase
from PyQt6.QtWidgets import QMessageBox
from services.file_service import write_file
from utils.logger import logger


class EditorArea(TabBase):
    """Editor area: tabbed code editors (+ terminal later)."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("editor_panel")
        logger.info("Initializing EditorArea")
        

    def add_tab(self, tab_name: str, file_path: str, content: str) -> int | None:
        """ this method used for open a tab """
        
        # check if the file is already open
        if file_path in self.OPEN_TABS:
            tab = self.OPEN_TABS[file_path]  # -> tab
            index = self.indexOf(tab)
            self.setCurrentIndex(index)
            return

        # create a new tab
        tab = BaseEditor(file_path = file_path)
        tab.setText(content)

        # Creat New Tab and return Tab Index
        tab_index = self.addTab(tab, tab_name)

        # saving the file and tab open to the list
        self.OPEN_TABS[file_path] = tab
        self.setCurrentIndex(tab_index)

        return tab_index

    def current_file_path(self) -> str:
        """Returns file path of current selected tab"""
        widget = self.currentWidget()
        file_path = getattr(widget, "file_path", None)

        if not widget:
            return None

        return file_path

    def current_content(self) -> str:
        """Returns content of current selected tab"""
        widget = self.currentWidget()

        if not widget:
            return ""   
        content = widget.text()

        return content

    def on_close_tab(self, index: int) -> None:
        """Close the tab at the given index, ask to save changes first."""
        widget = self.widget(index)
        file_path = getattr(widget, "file_path", None)
        content = widget.text()
    
        if widget is not None and widget.isModified():
            choice = QMessageBox.question(
                self,
                "Unsaved Changes",
                f'Save changes to "{self.tabText(index)}" before closing?',
                QMessageBox.StandardButton.Save
                | QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Save,
            )
    
            if choice == QMessageBox.StandardButton.Cancel:
                return
            if choice == QMessageBox.StandardButton.Save:
                write_file(file_path, content)
    
        if widget is not None:
            if file_path in self.OPEN_TABS:
                del self.OPEN_TABS[file_path]
    
        self.removeTab(index)
    
        if widget is not None:
            widget.deleteLater()
