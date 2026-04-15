# main_app.py
import sys
import asyncio
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QThread, Signal, Slot

# Importamos las clases y funciones de nuestros otros archivos
from main_ui import MainWindow
from data_handler import load_invoices_from_excel, save_processed_excel
from automation_engine import fetch_invoice_description
from classifier import categorize_description

# --- Hilo de Trabajo para el Procesamiento ---
# Esto es CRUCIAL para evitar que la interfaz se congele mientras el robot trabaja.
class WorkerThread(QThread):
    # Señales para comunicar el progreso y los resultados a la UI
    progress_updated = Signal(int, str) # (fila, mensaje_de_estado)
    processing_finished = Signal()

    def __init__(self, df, column_map):
        super().__init__()
        self.df = df
        self.column_map = column_map

    def run(self):
        # El bucle principal que procesa cada factura
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        for index, row in self.df.iterrows():
            try:
                # 1. Preparamos los datos de la factura usando el mapeo
                invoice_data = {
                    'ruc': str(row[self.column_map['ruc']]),
                    'serie': str(row[self.column_map['serie']]),
                    'numero': str(row[self.column_map['numero']])
                }
                
                # 2. Obtenemos la descripción
                self.progress_updated.emit(index, f"Procesando factura {invoice_data['numero']}...")
                description = loop.run_until_complete(fetch_invoice_description(invoice_data))

                if "Error" not in description:
                    # 3. Clasificamos la descripción
                    category = categorize_description(description)
                    # 4. Actualizamos el DataFrame
                    self.df.at[index, 'Categoria'] = category
                    self.progress_updated.emit(index, f"Clasificada como: {category}")
                else:
                    self.df.at[index, 'Categoria'] = "Error"
                    self.progress_updated.emit(index, "Error al obtener descripción")

            except Exception as e:
                self.df.at[index, 'Categoria'] = "Error en Datos"
                self.progress_updated.emit(index, f"Error: {e}")

        loop.close()
        self.processing_finished.emit()

# --- Controlador Principal de la Aplicación ---
class AppController:
    def __init__(self, window):
        self.window = window
        self.df = None
        self.worker = None
        
        # Conectamos los botones (señales) a nuestras funciones (slots)
        self.window.btn_load_excel.clicked.connect(self.load_excel)
        self.window.btn_start_processing.clicked.connect(self.start_processing)

    def load_excel(self):
        # Abre el diálogo para seleccionar un archivo
        filepath, _ = QFileDialog.getOpenFileName(self.window, "Seleccionar Excel", "", "Excel Files (*.xlsx)")
        if filepath:
            self.df, columns = load_invoices_from_excel(filepath)
            if self.df is not None:
                # Aquí iría la lógica de mapeo de columnas en una versión más avanzada
                # Por ahora, asumimos que las columnas se llaman como en nuestro Excel de prueba
                self.window.label_status.setText(f"Archivo cargado: {filepath}")
                self.populate_table()
                self.window.btn_start_processing.setEnabled(True)

    def populate_table(self):
        # Muestra los datos del Excel en la tabla de la UI
        self.window.table_invoices.setRowCount(self.df.shape[0])
        self.window.table_invoices.setColumnCount(self.df.shape[1] + 1) # Añadimos una columna para el estado
        
        headers = self.df.columns.tolist() + ["Estado del Proceso"]
        self.window.table_invoices.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in self.df.iterrows():
            for col_idx, cell_data in enumerate(row_data):
                self.window.table_invoices.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

    def start_processing(self):
        self.window.label_status.setText("Procesando facturas, por favor espere...")
        self.window.btn_start_processing.setEnabled(False)
        self.window.btn_load_excel.setEnabled(False)

        # Añadimos la columna de resultados si no existe
        if 'Categoria' not in self.df.columns:
            self.df['Categoria'] = 'No Procesado'

        # Asumimos un mapeo simple para nuestro ejemplo
        column_map = {
            'ruc': 'RUC del Proveedor',
            'serie': 'Serie',
            'numero': 'Correlativo'
        }
        
        # Creamos y ejecutamos el hilo de trabajo
        self.worker = WorkerThread(self.df, column_map)
        self.worker.progress_updated.connect(self.update_status_table)
        self.worker.processing_finished.connect(self.on_processing_finished)
        self.worker.start()

    @Slot(int, str)
    def update_status_table(self, row_index, message):
        # Actualiza la tabla en tiempo real con el estado del proceso
        status_col_index = self.window.table_invoices.columnCount() - 1
        self.window.table_invoices.setItem(row_index, status_col_index, QTableWidgetItem(message))

    def on_processing_finished(self):
        self.window.label_status.setText("¡Proceso completado! Guardando resultados...")
        output_path, _ = QFileDialog.getSaveFileName(self.window, "Guardar Archivo Procesado", "", "Excel Files (*.xlsx)")
        
        if output_path:
            save_processed_excel(self.df, output_path)
            self.window.label_status.setText(f"¡Resultados guardados en {output_path}!")
        else:
            self.window.label_status.setText("Guardado cancelado. Proceso finalizado.")

        self.window.btn_load_excel.setEnabled(True)

# --- Punto de Entrada Principal ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    controller = AppController(main_window) # El controlador conecta la UI con la lógica
    main_window.show()
    sys.exit(app.exec())