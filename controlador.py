from modelos.catalogo import Catalogo
from vista.ventana_principal import VentanaPrincipal
from vista.ventana_pelicula import VentanaPelicula
from vista.ventana_actores import VentanaActor

class Controlador:
    def __init__(self):
        # Instancia de catálogo
        self.__catalogo = Catalogo()

        # Instancias Ventana Principal
        peliculas = self.__catalogo.obtener_peliculas()
        self.__ventana_principal = VentanaPrincipal()
        self.__ventana_principal.cargar_peliculas(peliculas)
        self.__ventana_principal.buscar.connect(self.__buscar_peliculas)
        self.__ventana_principal.abrir_pelicula.connect(self.__mostrar_pelicula)
        self.__ventana_principal.abrir_ventana_busqueda_actores.connect(self.__abrir_ventana_busqueda_actores)

        # Instancias Ventana Película
        self.__ventana_pelicula = VentanaPelicula()

        # Instancias Ventana Actores
        self.__ventana_actores = VentanaActor()
        self.__ventana_actores.buscar_actor.connect(self.__buscar_actor)
        self.__ventana_actores.busqueda_por_actores.connect(self.__buscar_por_actores)
        self.__ventana_actores.abrir_pelicula.connect(self.__mostrar_pelicula)

    def __buscar_peliculas(self, titulo):
        peliculas = self.__catalogo.buscar_peliculas_por_titulo(titulo)
        if len(peliculas) == 0:
            self.__ventana_principal.mostrar_error("No se encontró la película")
            peliculas = self.__catalogo.obtener_peliculas()

        self.__ventana_principal.cargar_peliculas(peliculas)

    def __mostrar_pelicula(self, titulo):
        peliculas = self.__catalogo.buscar_peliculas_por_titulo(titulo)

        if peliculas:
            pelicula = peliculas[0]
            self.__ventana_pelicula.mostrar_datos(pelicula)
            self.__ventana_pelicula.exec()
        else:
            self.__ventana_principal.mostrar_error("No se encontró la película.")

    def __abrir_ventana_busqueda_actores(self):
        actores = self.__catalogo.obtener_actores_unicos()
        self.__ventana_actores.cargar_actores(actores)
        self.__ventana_actores.exec()

    def __buscar_actor(self, nombre):
        actores = self.__catalogo.obtener_actor_por_nombre(nombre)
        if len(actores) == 0:
            self.__ventana_actores.mostrar_error("No se encontró el actor")
        else:
            self.__ventana_actores.cargar_actores(actores)

    def __buscar_por_actores(self, actor_n1, actor_n2):
        if actor_n1 and actor_n2:
            if actor_n1 != actor_n2:
                peliculas_encontradas = self.__catalogo.buscar_peliculas_por_actores(actor_n1, actor_n2)

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
