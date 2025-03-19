from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Signal
from ui.ventana_principal import Ui_Ventana_principal


class VentanaPrincipal(QMainWindow):
    buscar = Signal(str)
    abrir_pelicula = Signal(str)
    abrir_ventana_busqueda_actores = Signal()

    def __init__(self):
        super().__init__()  # Extiende funcionalidades de la clase padre
        self.__ui = Ui_Ventana_principal()
        self.__ui.setupUi(self)  # Configura los botones e interfaz
        self.setWindowTitle("Ventana principal")

        self.__ui.table_peliculas.setRowCount(0)
        self.__ui.table_peliculas.setColumnCount(1)
        self.__ui.table_peliculas.setHorizontalHeaderLabels(["Películas"])
        self.__ui.table_peliculas.verticalHeader().setVisible(False)
        self.__ui.table_peliculas.horizontalHeader().setStretchLastSection(True)
        self.__ui.table_peliculas.itemDoubleClicked.connect(self.emitir_abrir_pelicula)
        self.__ui.boton_buscar_pelicula.setCheckable(True)
        self.__ui.boton_abrir_ventana_actores.setCheckable(True)

    def emitir_buscar(self):
        titulo = self.__ui.line_ingreso_nombre.text().lower()
        self.buscar.emit(titulo)

    def emitir_abrir_pelicula(self, item):
        self.abrir_pelicula.emit(item.text())

    def emitir_abrir_ventana_busqueda_actores(self):
        self.abrir_ventana_busqueda_actores.emit()

    def cargar_peliculas(self, peliculas):
        self.__peliculas = []
        self.__completar_tabla(peliculas)

    def __completar_tabla(self, peliculas):
        self.__ui.table_peliculas.setRowCount(0)

        for pelicula in peliculas:
            fila = self.__ui.table_peliculas.rowCount()
            self.__ui.table_peliculas.insertRow(fila)
            self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula.obtener_atributos()['Titulo']))
            self.__peliculas.append(pelicula)

    def mostrar_error(self, error):
        QMessageBox.warning(self, "Error", error)
