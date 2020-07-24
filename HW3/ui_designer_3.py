from PyQt5.QtWidgets import QApplication, QDialog
import sys
# https://stackoverflow.com/questions/35950050/how-to-import-python-file-located-in-same-subdirectory-in-a-pycharm-project
from dialog_form import Ui_Dialog


class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
