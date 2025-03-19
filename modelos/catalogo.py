import json
import os
from modelos.pelicula import Pelicula


class Catalogo:
    def __init__(self):
        self.__peliculas = []
        self.__cargar_datos()

    def __obtener_contenido_del_archivo(self):
        ruta_archivo = os.path.join("recursos", "peliculas.json")
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except Exception as error:
            print(f"Ocurrió un error: {error}")

    def __cargar_datos(self):
        contenido = self.__obtener_contenido_del_archivo()
        self.__peliculas = []

        for pelicula in contenido:
            nueva_pelicula = Pelicula(
                pelicula["titulo"],
                pelicula["sinopsis"],
                pelicula["puntuacion"],
                pelicula["actores"],
                pelicula["poster"]
            )
            self.__peliculas.append(nueva_pelicula)

        self.__actores = self.obtener_actores_unicos()

    def obtener_actores_unicos(self):
        actores = []
        for pelicula in self.__peliculas:
            for actor in pelicula.obtener_atributos()['Actores']:
                actores.append(actor)
        return sorted(set(actores))

    def obtener_peliculas(self):
        return self.__peliculas

    def obtener_actor_por_nombre(self, nombre_actor):
        actores_encontrados = []
        for actor in self.__actores:
            if nombre_actor.lower() in actor.lower():
                actores_encontrados.append(actor)
        return actores_encontrados

    def buscar_peliculas_por_titulo(self, titulo):
        peliculas_encontradas = []
        for pelicula in self.__peliculas:
            if titulo.lower() in pelicula.obtener_atributos()['Titulo'].lower():
                peliculas_encontradas.append(pelicula)
        return peliculas_encontradas

    def buscar_peliculas_por_actores(self, actor_n1, actor_n2):
        peliculas_encontradas = []
        for pelicula in self.__peliculas:
            actores_minuscula = [actor.lower() for actor in pelicula.obtener_atributos()['Actores']]
            if actor_n1.lower() in actores_minuscula and actor_n2.lower() in actores_minuscula:
                peliculas_encontradas.append(pelicula)
        return peliculas_encontradas
