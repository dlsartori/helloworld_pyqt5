from PyQt5.QtWidgets import QApplication, QMainWindow
import sys  # solo es necesario si hay argumentos de línea de comandos

def main():
    # Se necesita una (y solo una) instancia de QApplication por cada aplicación
    # sys.argv permite pasar argumentos de línea de comandos a la aplicación
    # Si no se van a usar argumentos de línea de comandos se pasa una lista vacía: QApplication([])
    app = QApplication(sys.argv)

    # Se necesita por lo menos una instancia de QMainWindow o algún otro widget que cree una ventana
    window = QMainWindow()

    # Importante: las ventanas están ocultas por defecto
    window.show()

    # Iniciar el loop principal de la aplicación
    app.exec_()

    # La aplicación no va a llegar hasta aquí hasta que se salga, terminando el loop principal

if __name__ == '__main__': main()
