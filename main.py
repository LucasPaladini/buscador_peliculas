from PySide6.QtWidgets import QApplication
import sys
from controlador import Controlador

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controlador = Controlador()
    controlador.ejecutar()
    print("Iniciando aplicación de búsqueda de películas")
    sys.exit(app.exec())
