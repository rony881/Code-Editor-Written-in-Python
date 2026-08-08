import sys
from PyQt6.QtWidgets import QApplication
from qfluentwidgets import Theme, setTheme

from ui.views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setTheme(Theme.LIGHT)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())