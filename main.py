import sys
from PyQt6.QtWidgets import QApplication
from gui import FordFulkersonGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FordFulkersonGUI()
    window.show()
    sys.exit(app.exec())
