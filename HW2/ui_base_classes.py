from PyQt5.QtWidgets import QApplication, QWidget
import sys  # se usa para cerrar la aplicación


class HelloWorldWindow(QWidget):
    """
    Clase para la ventana. Se define como una subclase de QWidget.
    También se puede usar cualquier clase que herede de QWidget, como QMainWindow o QDialog .

    Este comentario multilínea es la forma normal de documentar una clase
    """

    def __init__(self, *args, **kwargs):    # *args y **kwargs son opcionales
        """
        Inicialización de la clase
        :param args: (algún comentario soble el parámetro args)
        :param kwargs: (algún comentario soble el parámetro kwargs)
        """

        # Inicializar la clase base (QWidget) para que estén disponibles todos sus elementos
        super(HelloWorldWindow, self).__init__(*args, **kwargs)      # de nuevo, *args y **kwargs son opcionales

        # Inicializar la UI (método definido más abajo)
        self.initializeUI()

    def initializeUI(self):
        """
        Inicialización de la UI
        Acá se se define la apariencia de la ventana y se crean sus elementos
        """
        self.setGeometry(100, 100, 400, 300)    # posición y dimensiones de la ventana
        self.setWindowTitle('Ventana vacía en PyQt')    # título de la ventana

        # Importante: las ventanas están ocultas por defecto
        # self.show()   # esto puede ejecutarse aquí o después de invocar la clase (línea 48), una de dos


if __name__ == '__main__':
    # Se necesita una (y solo una) instancia de QApplication por cada aplicación
    # sys.argv permite pasar argumentos de línea de comandos a la aplicación
    # Si no se van a usar argumentos de línea de comandos se pasa una lista vacía: QApplication([])
    app = QApplication(sys.argv)

    # Crear una instancia de la clase HelloWorldWindow definida más arriba
    window = HelloWorldWindow()

    # Importante: las ventanas están ocultas por defecto
    window.show()   # esto puede ejecutarse aquí o en el método initializeUI() de la clase (línea 35), una de dos

    # Iniciar el loop principal y usar sys.exit() para cerrar la aplicación
    sys.exit(app.exec_())

    # La aplicación no va a llegar hasta aquí hasta que se salga, terminando el loop principal
