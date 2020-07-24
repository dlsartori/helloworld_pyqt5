from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = uic.loadUi("dialog_form.ui")
    window.show()
    sys.exit(app.exec_())
