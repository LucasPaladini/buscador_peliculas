from modelo import Pelicula
from vista.ventana_principal import VentanaPrincipal

class Controlador:
    def __init__(self):
        self.__modelo = Pelicula()
        peliculas = self.__modelo.obtener_peliculas()
        self.__ventana_principal = VentanaPrincipal(peliculas)

    def ejecutar(self):
        self.__ventana_principal.show()
