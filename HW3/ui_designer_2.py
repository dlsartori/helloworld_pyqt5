from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys

# https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html#PyQt5.uic.loadUiType
# https://stackoverflow.com/questions/22663716/working-with-pyqt-and-qt-designer-ui-files

DialogUI, DialogBase = uic.loadUiType("dialog_form.ui")


class MyDialog(DialogBase, DialogUI):
    def __init__(self, parent=None):
        DialogBase.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

