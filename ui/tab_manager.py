import os

from PyQt6.QtWidgets import QTabWidget, QMessageBox

from editor.code_editor import Editor
class Tab(QTabWidget):
    """ This Class Handles Open Tab, Current Tab Logic  """

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        self.setObjectName("tabwidget")
        # This makes the tabs closable
        self.setTabsClosable(True)

        # This make the tabs movable
        self.setMovable(True)

        # This Will Keep tarck of Opened Tabs and Files
        self.open_tabs = {}

        # when user request for closing the tab this code 
        # connects to close tab method
        self.tabCloseRequested.connect(self.close_tab)

    def open_tab(self, tab_title, file_path, content):
        """ this method used for open a tab """

        # check if the file is already open
        if file_path in self.open_tabs:
            tab = self.open_tabs[file_path]  # -> tab
            index = self.indexOf(tab)
            self.setCurrentIndex(index)
            return

        new_tab = Editor()
        new_tab.setText(content)
        # setting the file path with that tab 
        new_tab.file_path = file_path
        # Creat New Tab and return Tab Index
        tab_index = self.addTab(new_tab, tab_title)
        # saving the file and tab open to the list
        self.open_tabs[file_path] = new_tab
        self.setCurrentIndex(tab_index)

        return tab_index

    def close_tab(self,index):
        """ this used for closing the tab"""

        widget = self.widget(index)

        # Gets the file path and content of file
        file_path = widget.file_path
        content = widget.text()

        # ask the user to save or Discard before closing the tab
        reply = QMessageBox.question(self, "Save File", "Do You Want to Save the File Befor Closing? ")
        # if the user answer is no, then close
        # tab without saving
        if reply == QMessageBox.StandardButton.No:
            self.removeTab(index)
            if file_path in self.open_tabs:
                del self.open_tabs[file_path]
            return

        if not self.parent.file_ops.save_file(file_path, content):
            return

        file_path = widget.file_path
        self.removeTab(index)
        if file_path in self.open_tabs:
            del self.open_tabs[file_path]

    def get_text(self):
        widget = self.currentWidget()

        return widget.text() if widget else ""
    
    def get_path(self):
        widget = self.currentWidget()     

        return widget.file_path if widget else None
