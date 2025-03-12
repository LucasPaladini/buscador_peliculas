from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui.ventana_principal import Ui_Ventana_principal
from vista.ventana_actores import VentanaActor
from vista.ventana_pelicula import VentanaPelicula


class VentanaPrincipal(QMainWindow):
    def __init__(self, peliculas):  # Paso parámetro de peliculas
        super().__init__()  # Se utiliza para poder extender funcionalidades de la clase padre
        self.__ui = Ui_Ventana_principal()  # Crea una instancia de la main
        self.__ui.setupUi(self)     # Configura los botones e interfaz
        self.setWindowTitle("Ventana principal")

        self.__ui.table_peliculas.setRowCount(0)    # Coloca filas al principio
        self.__ui.table_peliculas.setColumnCount(1)  # Cantidad de columnas
        self.__ui.table_peliculas.setHorizontalHeaderLabels(["Películas"])  # Diga el titulo sobre la tabla
        self.__ui.table_peliculas.verticalHeader().setVisible(False)      # Ocultar numeros de las filas
        self.__ui.table_peliculas.horizontalHeader().setStretchLastSection(True)    # Las filas ocupan la totalidad
        self.__ui.table_peliculas.itemDoubleClicked.connect(self.__cargar_peliculas_en_tabla)
        self.__ui.boton_buscar_pelicula.setCheckable(True)
        self.__ui.boton_abrir_ventana_actores.setCheckable(True)

        self.__cargar_peliculas(peliculas)  # Ejecuta ese método enviandole como parámetro las peliculas


    def __cargar_peliculas(self, peliculas):
        self.__peliculas = []
        # print(peliculas)

        for pelicula in peliculas:
            fila = self.__ui.table_peliculas.rowCount()
            self.__ui.table_peliculas.insertRow(fila)
            self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))
            self.__peliculas.append(pelicula)

    def __buscar_peliculas(self):
        texto_busqueda = self.__ui.line_ingreso_nombre.text().lower()
        self.__ui.table_peliculas.setRowCount(0)

        if texto_busqueda == "":
            QMessageBox.warning(self, "Error", "Ingrese una pelicula")

        for pelicula in self.__peliculas:
            if texto_busqueda in pelicula["titulo"].lower():
                fila = self.__ui.table_peliculas.rowCount()
                self.__ui.table_peliculas.insertRow(fila)
                self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula["titulo"]))
        if self.__ui.table_peliculas.rowCount() == 0:
            QMessageBox.warning(self, "Error", "No se encontró la película")


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

    def __abrir_ventana_actores(self):
        print("Ejecutando ventana de búsqueda por actores")
        ventana_actor = VentanaActor(self.__peliculas)
        ventana_actor.exec()
