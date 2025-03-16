from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.datos_pelicula import Ui_Dialog
from modelo import Pelicula


class VentanaPelicula(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.setWindowTitle("Detalles de la Película")

    def mostrar_datos(self, pelicula):
        self.__ui.label_titulo_ingresado.setText(pelicula["titulo"])
        self.__ui.label_sinopsis.setText(pelicula["sinopsis"])
        self.__ui.label_puntuacion.setText(str(pelicula["puntuacion"]))
        self.__ui.label_actores.setText(", ".join(pelicula["actores"]))
        self.__modelo_pelicula = Pelicula()
        self.__cargar_ruta = self.__modelo_pelicula.cargar_ruta(pelicula["poster"])
        self.__cargar_poster(self.__cargar_ruta)

    def __cargar_poster(self, ruta):
        pixmap = QPixmap(ruta)
        if pixmap:
            self.__ui.label_poster.setPixmap(pixmap.scaled(300, 450))
        else:
            print("Error al cargar la imagen: poster no encontrado.")
