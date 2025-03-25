import os

class Pelicula:
    def __init__(self, titulo, sinopsis, puntuacion, actores, poster):
        self.__titulo = titulo
        self.__sinopsis = sinopsis
        self.__puntuacion = puntuacion
        self.__poster = poster
        self.__actores = actores

    def obtener_atributos(self):
        actores_nombres = []

        for actor in self.__actores:
            actores_nombres.append(actor.nombre)

        return {
            'Titulo': self.__titulo,
            'Sinopsis': self.__sinopsis,
            'Puntuacion': self.__puntuacion,
            'Actores': actores_nombres,
            'Poster': self.__poster
        }

    def cargar_ruta(self):
        return os.path.join("recursos", "imagen", self.__poster)
