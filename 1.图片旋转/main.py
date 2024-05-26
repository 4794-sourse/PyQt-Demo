from PyQt5.QtWidgets import *
from windowEx import WindowEx

import sys

if __name__ == '__main__':
    app = QApplication([])
    win = WindowEx()
    win.show()
    sys.exit(app.exec())