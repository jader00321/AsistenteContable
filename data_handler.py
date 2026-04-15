# data_handler.py
import pandas as pd

def load_invoices_from_excel(filepath):
    """
    Carga un archivo Excel y devuelve un DataFrame de Pandas y los nombres de las columnas.
    Maneja errores si el archivo no se encuentra o no es un Excel válido.
    """
    try:
        df = pd.read_excel(filepath)
        # Limpiamos los nombres de las columnas por si acaso (quitar espacios extra)
        df.columns = df.columns.str.strip()
        print("Excel cargado exitosamente.")
        print("Columnas detectadas:", df.columns.tolist())
        return df, df.columns.tolist()
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta: {filepath}")
        return None, []
    except Exception as e:
        print(f"Error inesperado al leer el archivo Excel: {e}")
        return None, []

def save_processed_excel(df, output_path):
    """
    Guarda el DataFrame procesado en un nuevo archivo Excel.
    """
    try:
        df.to_excel(output_path, index=False)
        print(f"Archivo procesado guardado exitosamente en: {output_path}")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")
        return False

# --- Bloque de prueba ---
# Este código solo se ejecutará cuando corras este archivo directamente
if __name__ == '__main__':
    test_filepath = 'facturas.xlsx'
    invoice_df, columns = load_invoices_from_excel(test_filepath)
    
    if invoice_df is not None:
        print("\n--- Primeras 5 filas del Excel ---")
        print(invoice_df.head())
        
        # Simulamos que añadimos una columna de resultados
        invoice_df['Categoria'] = 'No Procesado'
        
        # Probamos guardar el archivo
        save_processed_excel(invoice_df, 'facturas_PROCESADO.xlsx')