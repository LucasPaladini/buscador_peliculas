from modelo import Pelicula
from vista import Vista

class Controlador:
    def __init__(self):
        self.__modelo = Pelicula()
        peliculas = self.__modelo.obtener_peliculas()
        self.__vista = Vista(peliculas)

    def ejecutar(self):
        self.__vista.show()
