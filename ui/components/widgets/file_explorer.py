from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView
from tests.core import DUMMY_FILE_MODEL


class FileExplorer(QTreeView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("file_explorer")
        self.file_model = QFileSystemModel()
        self.clicked.connect(self.on_file_click)

        self._setup_config()

    def _setup_config(self):
        # tree configaretion
        self.setModel(self.file_model)
        self.hideColumn(1)
        self.hideColumn(2)  # Hide Extra Column
        self.hideColumn(3)
        self.setAnimated(True)
        self.setIndentation(10)
        self.setMinimumWidth(170)
        self.setItemsExpandable(True)
        self.setRootIsDecorated(False)
        self.setHeaderHidden(True)  # Hide the File Header
        self.setFolderPath(DUMMY_FILE_MODEL)
        

    def setFolderPath(self, file_path):
        self.file_model.setRootPath(file_path)
        self.setRootIndex(self.file_model.index(file_path))

    def on_file_click(self):
        ...
        