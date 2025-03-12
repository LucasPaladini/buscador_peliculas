import os
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.datos_pelicula import Ui_Dialog


class VentanaPelicula(QDialog):
    def __init__(self, pelicula):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.setWindowTitle("Detalles de la Película")

        self.__ui.label_titulo_ingresado.setText(pelicula["titulo"])
        self.__ui.label_sinopsis.setText(pelicula["sinopsis"])
        self.__ui.label_puntuacion.setText(str(pelicula["puntuacion"]))
        self.__ui.label_actores.setText(", ".join(pelicula["actores"]))
        self.__cargar_poster(pelicula['poster'])

    def __cargar_poster(self, archivo):
        ruta = os.path.join("peliculas", "imagen", archivo)
        # print(ruta)
        pixmap = QPixmap(ruta)

        if pixmap:
            self.__ui.label_poster.setPixmap(pixmap.scaled(300, 450))
        else:
            print("Error al cargar la imagen: archivo no encontrado.")