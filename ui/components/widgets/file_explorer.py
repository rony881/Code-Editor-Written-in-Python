from pathlib import Path
from PyQt6.QtCore import pyqtSignal, QModelIndex
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QFileDialog, QTreeView

from ui.BaseWidgets.widget_base import BaseWidget



class FileExplorer(BaseWidget):
    file_selected = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("file_explorer")
        self.file_tree_view = FileTreeView(self)
        self.file_tree_view.file_selected.connect(self.file_selected)
        
        self.add(self.file_tree_view)

    def browse_folder(self):
        self.file_tree_view.browse_folder()


class FileTreeView(QTreeView):
    file_selected = pyqtSignal(str)
    folder_changed = pyqtSignal(str)

    def __init__(self, parent=None, root_path: str | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("file_tree_view")
        self.file_model = QFileSystemModel()
        self.clicked.connect(self.on_file_click)
        self._setup_config(root_path)

    def _setup_config(self, root_path: str | None):
        # tree configuration
        self.setModel(self.file_model)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        self.setAnimated(True)
        self.setIndentation(10)
        self.setMinimumWidth(170)
        self.setItemsExpandable(True)
        self.setRootIsDecorated(False)
        self.setHeaderHidden(True)
        self.setFolderPath(root_path or str(Path.home()))

    def setFolderPath(self, file_path: str) -> None:
        """Point the explorer at a new root folder."""
        self.file_model.setRootPath(file_path)
        self.setRootIndex(self.file_model.index(file_path))
        self.folder_changed.emit(file_path)

    def browse_folder(self) -> None:
        """Open a native dialog and switch root folder if the user picks one."""
        current = self.file_model.rootPath()
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", current)
        if folder:
            self.setFolderPath(folder)

    def on_file_click(self, index: QModelIndex) -> None:
        path = self.file_model.filePath(index)
        if not self.file_model.isDir(index):
            self.file_selected.emit(path)
