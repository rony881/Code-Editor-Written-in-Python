"""File explorer side panel for browsing and opening project files."""

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import CaptionLabel, TreeView


class SidePanel(QWidget):
    """Dockable side panel showing a file-system tree of the open folder.

    Emits `fileDoubleClicked` with the absolute file path whenever the
    user double-clicks a file (not a folder) in the tree.
    """

    fileDoubleClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.model = QFileSystemModel(self)

        self.tree = TreeView(self)
        self.tree.setModel(self.model)
        self.tree.setHeaderHidden(True)
        # Only the "name" column is useful in a narrow side panel;
        # size/type/date-modified columns just get squeezed and truncated.
        for column in range(1, self.model.columnCount()):
            self.tree.hideColumn(column)

        self.titleLabel = CaptionLabel("EXPLORER", self)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(8, 8, 0, 0)
        self.vBoxLayout.setSpacing(4)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.tree)

        self.tree.doubleClicked.connect(self._onDoubleClicked)

    def setRootPath(self, path: str):
        """Point the explorer at a project folder."""
        self.model.setRootPath(path)
        self.tree.setRootIndex(self.model.index(path))

    def _onDoubleClicked(self, index):
        """Emit fileDoubleClicked when a file (not a directory) is opened."""
        if not self.model.isDir(index):
            self.fileDoubleClicked.emit(self.model.filePath(index))
