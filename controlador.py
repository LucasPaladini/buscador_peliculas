from modelo import Pelicula, Actor
from vista.ventana_principal import VentanaPrincipal
from vista.ventana_pelicula import VentanaPelicula
from vista.ventana_actores import VentanaActor


class Controlador:
    def __init__(self):
        self.__modelo_pelicula = Pelicula()
        peliculas = self.__modelo_pelicula.obtener_peliculas()
        self.__ventana_principal = VentanaPrincipal()
        self.__ventana_principal.cargar_peliculas(peliculas)
        self.__ventana_principal.buscar.connect(self.__buscar_peliculas)
        self.__ventana_principal.abrir_pelicula.connect(self.__mostrar_pelicula)
        self.__ventana_principal.abrir_ventana_busqueda_actores.connect(self.__abrir_ventana_busqueda_actores)

        self.__ventana_pelicula = VentanaPelicula()

        self.__modelo_actor = Actor()
        self.__ventana_actores = VentanaActor()
        self.__ventana_actores.buscar_actor.connect(self.__buscar_actor)
        self.__ventana_actores.busqueda_por_actores.connect(self.__buscar_por_actores)
        self.__ventana_actores.abrir_pelicula.connect(self.__mostrar_pelicula)


    def __buscar_peliculas(self, titulo):
        peliculas = self.__modelo_pelicula.buscar_por_titulo(titulo)

        if len(peliculas) == 0:
            self.__ventana_principal.mostrar_error("No se encontró la película")
            peliculas = self.__modelo_pelicula.obtener_peliculas()

        self.__ventana_principal.cargar_peliculas(peliculas)

    def __mostrar_pelicula(self, titulo):
        pelicula = self.__modelo_pelicula.obtener_por_titulo(titulo)
        self.__ventana_pelicula.mostrar_datos(pelicula)
        self.__ventana_pelicula.exec()

    def __abrir_ventana_busqueda_actores(self):
        self.__ventana_actores.cargar_actores(self.__modelo_actor.obtener_todos())
        self.__ventana_actores.exec()

    def __buscar_actor(self, nombre):
        actor = self.__modelo_actor.buscar_actor_por_nombre(nombre)

        if len(actor) == 0:
            self.__ventana_actores.mostrar_error("No se encontró el actor")
            self.__ventana_actores.cargar_actores(self.__modelo_actor.obtener_todos())

        else:
            self.__ventana_actores.cargar_actores(actor)

    def __buscar_por_actores(self, actor_n1, actor_n2):
        if actor_n1 and actor_n2:
            if actor_n1 != actor_n2:
                peliculas_encontradas = self.__modelo_actor.buscar_actores_en_pelicula(actor_n1, actor_n2)

                if len(peliculas_encontradas) == 0:
                    self.__ventana_actores.mostrar_error("No se encontraron películas con esos actores.")
                else:
                    self.__ventana_actores.cargar_peliculas(peliculas_encontradas)
            else:
                self.__ventana_actores.mostrar_error("Los actores no pueden ser los mismos.")
        else:
            self.__ventana_actores.mostrar_error("Ingrese ambos nombres de actores.")

    def ejecutar(self):
        self.__ventana_principal.show()


