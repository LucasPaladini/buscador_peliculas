import json
import os


def obtener_contenido_del_archivo():
    ruta_archivo = os.path.join("recursos", "peliculas.json")

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    except Exception as error:
        print(f"Ocurrió un error: {error}")


class Pelicula:
    def obtener_peliculas(self):
        return obtener_contenido_del_archivo()

    def buscar_por_titulo(self, titulo):
        peliculas = []

        for pelicula in self.obtener_peliculas():
            if titulo in pelicula["titulo"].lower():
                peliculas.append(pelicula)

        return peliculas

    def obtener_por_titulo(self, titulo):
        for pelicula in self.obtener_peliculas():
            if pelicula["titulo"] == titulo:
                return pelicula

    def cargar_ruta(self, poster):
        ruta = os.path.join("recursos", "imagen", poster)
        return ruta

class Actor:
    def obtener_todos(self):
        actores = []
        peliculas = obtener_contenido_del_archivo()

        for pelicula in peliculas:
            for actor in pelicula["actores"]:
                if actor not in actores:
                    actores.append(actor)

        return sorted(actores)

    def buscar_actor_por_nombre(self, nombre_actor):
        actores = []

        for actor_en_lista in self.obtener_todos():
            if nombre_actor.lower() in actor_en_lista.lower():
                actores.append(actor_en_lista)
        return actores

    def buscar_actores_en_pelicula(self, actor_n1, actor_n2):
        peliculas = obtener_contenido_del_archivo()
        peliculas_encontradas = []

        for pelicula in peliculas:
            actores = [actor.lower() for actor in pelicula.get('actores', [])]
            if actor_n1.lower() in actores and actor_n2.lower() in actores:
                peliculas_encontradas.append(pelicula)
        return peliculas_encontradas
