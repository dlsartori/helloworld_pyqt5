from PyQt5.QtWidgets import QApplication, QWidget
import sys

class HelloWorldWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(HelloWorldWindow, self).__init__(*args, **kwargs)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Ventana vacía en PyQt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())
