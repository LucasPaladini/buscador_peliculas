from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Signal
from ui.busqueda_actores import Ui_dialog_actor


class VentanaActor(QDialog):
    buscar_actor = Signal(str)
    busqueda_por_actores = Signal(str, str)
    abrir_pelicula = Signal(str)

    def __init__(self):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actores")

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


    def emitir_buscar_actor(self):
        titulo = self.__ui.line_ingreso_actor.text().lower().strip()
        self.buscar_actor.emit(titulo)

    def __obtener_nombres_actores(self):
        actor_1 = self.__ui.actor_n1.text().strip().lower()
        actor_2 = self.__ui.actor_n2.text().strip().lower()
        return actor_1, actor_2

    def emitir_busqueda_por_actores(self):
        actor_1, actor_2 = self.__obtener_nombres_actores()
        self.busqueda_por_actores.emit(actor_1, actor_2)

    def mostrar_error(self, error):
        QMessageBox.warning(self, "Error", error)

    def cargar_actores(self, actores):
        self.__completar_tabla(actores)

    def __completar_tabla(self, actores):
        self.__ui.table_actores.setRowCount(0)

        for actor in actores:
            fila = self.__ui.table_actores.rowCount()
            self.__ui.table_actores.insertRow(fila)
            self.__ui.table_actores.setItem(fila, 0, QTableWidgetItem(actor))

    def cargar_peliculas(self, peliculas):
        self.__mostrar_peliculas_encontradas(peliculas)

    def __mostrar_peliculas_encontradas(self, peliculas):
        self.__ui.table_peliculas_actores.setRowCount(0)
        for pelicula in peliculas:
            fila = self.__ui.table_peliculas_actores.rowCount()
            self.__ui.table_peliculas_actores.insertRow(fila)
            self.__ui.table_peliculas_actores.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))

        self.__ui.table_peliculas_actores.itemDoubleClicked.connect(self.emitir_abrir_pelicula)

    def emitir_abrir_pelicula(self, item):
        self.abrir_pelicula.emit(item.text())
