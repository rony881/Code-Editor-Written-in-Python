from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
print("Opening Applicaton Please Wait...")

# =============================================================================
# Run App
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print("Running ✅")
    sys.exit(app.exec())