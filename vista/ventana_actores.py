from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from ui.busqueda_actores import Ui_dialog_actor
from vista.ventana_pelicula import VentanaPelicula


class VentanaActor(QDialog):
    def __init__(self, peliculas):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actores")
        self.__peliculas = peliculas

        # self.resize(500, 600)

        self.__ui.table_peliculas_actores.setRowCount(0)
        self.__ui.table_peliculas_actores.setColumnCount(1)
        self.__ui.table_peliculas_actores.setHorizontalHeaderLabels([""])
        self.__ui.table_peliculas_actores.verticalHeader().setVisible(False)
        self.__ui.table_peliculas_actores.horizontalHeader().setStretchLastSection(True)

        self.__ui.table_actores.setRowCount(0)
        self.__ui.table_actores.setColumnCount(1)
        self.__ui.table_actores.setHorizontalHeaderLabels([""])
        self.__ui.table_actores.verticalHeader().setVisible(False)
        self.__ui.table_actores.horizontalHeader().setStretchLastSection(True)

        self.cargar_actores()

    def __buscar_actor(self):
        texto_busqueda = self.__ui.line_ingreso_actor.text().strip().lower()
        self.__ui.table_actores.setRowCount(0)

        for pelicula in self.__peliculas:
            for actor in pelicula["actores"]:
                if texto_busqueda in actor.lower():
                    fila = self.__ui.table_actores.rowCount()
                    self.__ui.table_actores.insertRow(fila)
                    self.__ui.table_actores.setItem(fila, 0, QTableWidgetItem(actor))

        if self.__ui.table_actores.rowCount() == 0:
            QMessageBox.warning(self, "Error", "No se encontró actor con ese nombre.")

    def cargar_actores(self):
        actores = []

        for pelicula in self.__peliculas:
            for actor in pelicula["actores"]:
                if actor not in actores:
                    actores.append(actor)

        for actor in sorted(actores):
            fila = self.__ui.table_actores.rowCount()
            self.__ui.table_actores.insertRow(fila)
            self.__ui.table_actores.setItem(fila, 0, QTableWidgetItem(actor))

    def __obtener_nombres_actores(self):
        actor_1 = self.__ui.actor_n1.text().strip()
        actor_2 = self.__ui.actor_n2.text().strip()
        return actor_1, actor_2

    def __buscar_pelicula_por_actores(self):
        actor_1, actor_2 = self.__obtener_nombres_actores()

        if actor_1 and actor_2:
            if actor_1 != actor_2:
                peliculas_encontradas = []
                for pelicula in self.__peliculas:
                    actores = [actor.lower() for actor in pelicula['actores']]
                    if actor_1.lower() in actores and actor_2.lower() in actores:
                        peliculas_encontradas.append(pelicula)

                if peliculas_encontradas:
                    self.__mostrar_peliculas_encontradas(peliculas_encontradas)
                else:
                    QMessageBox.warning(self, "Error", "No se encontraron películas con esos actores.")
            else:
                QMessageBox.warning(self, "Error", "Los actores no pueden ser los mismos.")
        else:
            QMessageBox.warning(self, "Error", "Ingrese ambos nombres de actores.")

    def __mostrar_peliculas_encontradas(self, peliculas):
        self.__ui.table_peliculas_actores.setRowCount(0)
        for pelicula in peliculas:
            fila = self.__ui.table_peliculas_actores.rowCount()
            self.__ui.table_peliculas_actores.insertRow(fila)
            self.__ui.table_peliculas_actores.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))

        self.__ui.table_peliculas_actores.itemDoubleClicked.connect(self.__cargar_detalles_pelicula)

    def __cargar_detalles_pelicula(self, item):
        titulo = item.text()
        pelicula = self.__buscar_pelicula_por_titulo(titulo)
        if pelicula:
            ventana_pelicula = VentanaPelicula(pelicula)
            ventana_pelicula.exec()

    def __buscar_pelicula_por_titulo(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula["titulo"] == titulo:
                return pelicula
        return None
