from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.datos_pelicula import Ui_Dialog


class VentanaPelicula(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.setWindowTitle("Detalles de la Película")

    def mostrar_datos(self, pelicula):
        self.__ui.label_titulo_ingresado.setText(pelicula.obtener_atributos()["Titulo"])
        self.__ui.label_sinopsis.setText(pelicula.obtener_atributos()["Sinopsis"])
        self.__ui.label_puntuacion.setText(str(pelicula.obtener_atributos()["Puntuacion"]))
        self.__ui.label_actores.setText(", ".join(pelicula.obtener_atributos()['Actores']))

        ruta = pelicula.cargar_ruta()
        self.__cargar_poster(ruta)

    def __cargar_poster(self, ruta):
        pixmap = QPixmap(ruta)
        if pixmap:
            self.__ui.label_poster.setPixmap(pixmap.scaled(300, 450))
        else:
            print("Error al cargar la imagen: poster no encontrado.")
