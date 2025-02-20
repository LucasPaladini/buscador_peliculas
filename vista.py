import os
from PySide6.QtWidgets import QMainWindow, QDialog, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QPixmap
from ui.ventana_principal import Ui_Ventana_principal
from ui.busqueda_actores import Ui_dialog_actor
from ui.datos_pelicula import Ui_Dialog

class Vista(QMainWindow):
    def __init__(self, peliculas):
        super().__init__()
        self.__ui = Ui_Ventana_principal()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana principal")

        self.__ui.table_peliculas.setRowCount(0)
        self.__ui.table_peliculas.setColumnCount(1)
        self.__ui.table_peliculas.setHorizontalHeaderLabels(["Películas"])
        self.__ui.table_peliculas.verticalHeader().setVisible(False)
        self.__ui.table_peliculas.horizontalHeader().setStretchLastSection(True)
        self.__ui.table_peliculas.itemDoubleClicked.connect(self.__cargar_peliculas_en_tabla)

        self.__cargar_peliculas(peliculas)

    def __cargar_peliculas(self, peliculas):
        self.__peliculas = []

        for pelicula in peliculas:
            fila = self.__ui.table_peliculas.rowCount()
            self.__ui.table_peliculas.insertRow(fila)
            self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))
            self.__peliculas.append(pelicula)

    def __buscar_peliculas(self):
        texto_busqueda = self.__ui.line_ingreso_nombre.text().lower()
        self.__ui.table_peliculas.setRowCount(0)

        for pelicula in self.__peliculas:
            if texto_busqueda in pelicula["titulo"].lower():
                fila = self.__ui.table_peliculas.rowCount()
                self.__ui.table_peliculas.insertRow(fila)
                self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))

    def __abrir_ventana_actores(self):
        print("Abriendo ventana películas por actores")
        ventana_actor = VentanaActor(self.__peliculas)
        ventana_actor.exec()

    def __cargar_peliculas_en_tabla(self, item):
        titulo = item.text()
        pelicula = self.__buscar_pelicula_por_titulo(titulo)
        if pelicula:
            ventana_pelicula = VentanaPelicula(pelicula)
            ventana_pelicula.exec()

    def __buscar_pelicula_por_titulo(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula["titulo"] == titulo:
                return pelicula

    # Aquí emitimos la señal para abrir la ventana de actores
    def emitir_signal_abrir_ventana_actores(self):
        self.__abrir_ventana_actores()


class VentanaActor(QDialog):
    def __init__(self, peliculas):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actor")
        self.__peliculas = peliculas

        self.__ui.table_peliculas_actores.setRowCount(0)
        self.__ui.table_peliculas_actores.setColumnCount(1)
        self.__ui.table_peliculas_actores.setHorizontalHeaderLabels(["Películas"])
        self.__ui.table_peliculas_actores.verticalHeader().setVisible(False)
        self.__ui.table_peliculas_actores.horizontalHeader().setStretchLastSection(True)

        self.__ui.table_actores.setRowCount(0)
        self.__ui.table_actores.setColumnCount(1)
        self.__ui.table_actores.setHorizontalHeaderLabels(["Actores"])
        self.__ui.table_actores.verticalHeader().setVisible(False)
        self.__ui.table_actores.horizontalHeader().setStretchLastSection(True)

        self.cargar_actores()

    def __buscar_actor_1(self):
        texto_busqueda = self.__ui.line_ingreso_actor_1.text().strip().lower()
        self.__ui.table_actores.setRowCount(0)

        for pelicula in self.__peliculas:
            for actor in pelicula["actores"]:
                if texto_busqueda in actor.lower():
                    fila = self.__ui.table_actores.rowCount()
                    self.__ui.table_actores.insertRow(fila)
                    self.__ui.table_actores.setItem(fila, 0, QTableWidgetItem(actor))

        if self.__ui.table_actores.rowCount() == 0:
            QMessageBox.warning(self, "Error", "No se encontró actor con ese nombre.")

    def __buscar_actor_2(self):
        texto_busqueda = self.__ui.line_ingreso_actor_2.text().strip().lower()
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
        actor_1 = self.__ui.line_ingreso_actor_1.text().strip()
        actor_2 = self.__ui.line_ingreso_actor_2.text().strip()
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


class VentanaPelicula(QDialog):
    def __init__(self, pelicula):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.setWindowTitle("Detalles de la Película")

        self.__ui.label_titulo_ingresado.setText(pelicula["titulo"])
        self.__ui.label_sinopsis.setText(pelicula["sinopsis"])
        self.__ui.label_puntuacion.setText(str(pelicula["puntuacion"]))
        self.__ui.label_actores.setText(", ".join(pelicula["actores"]))
        self.__cargar_poster(pelicula['poster'])

    def __cargar_poster(self, archivo):
        ruta = os.path.join("peliculas", "imagen", archivo)
        pixmap = QPixmap(ruta)

        if pixmap:
            self.__ui.label_poster.setPixmap(pixmap.scaled(300, 450))
        else:
            print("Error al cargar la imagen: archivo no encontrado.")
