# main_ui.py
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QTableWidget, QTableWidgetItem, 
                               QFileDialog, QLabel, QHeaderView)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # --- Configuración de la ventana principal ---
        self.setWindowTitle("Asistente Contable Automatizado")
        self.setGeometry(100, 100, 800, 600) # (x, y, ancho, alto)

        # --- Widgets (los componentes de la UI) ---
        self.label_status = QLabel("Bienvenido. Cargue un archivo Excel para comenzar.")
        self.btn_load_excel = QPushButton("Cargar Archivo Excel")
        self.btn_start_processing = QPushButton("Iniciar Proceso")
        self.table_invoices = QTableWidget() # Tabla para mostrar los datos del Excel

        # --- Configuración inicial de los widgets ---
        self.btn_start_processing.setEnabled(False) # Deshabilitado hasta que se cargue un archivo
        self.table_invoices.setColumnCount(6) # Columnas iniciales
        self.table_invoices.setHorizontalHeaderLabels(["RUC", "Tipo", "Serie", "Número", "Fecha", "Estado"])
        self.table_invoices.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # --- Layout (el organizador de los widgets) ---
        # El layout vertical apila los widgets uno encima del otro
        layout = QVBoxLayout()
        layout.addWidget(self.label_status)
        layout.addWidget(self.btn_load_excel)
        layout.addWidget(self.btn_start_processing)
        layout.addWidget(self.table_invoices)
        
        # Contenedor central para aplicar el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# --- Bloque de prueba para visualizar la ventana ---
if __name__ == '__main__':
    app = QApplication(sys.argv) # Crea la aplicación
    window = MainWindow() # Crea la ventana que diseñamos
    window.show() # Muestra la ventana
    sys.exit(app.exec()) # Inicia el bucle de eventos de la aplicación