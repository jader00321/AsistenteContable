# classifier.py

# Definimos nuestras reglas de clasificación.
# La clave es la categoría, el valor es una lista de palabras clave.
CLASSIFICATION_RULES = {
    'Combustible': ['grifo', 'gasolina', 'petro', 'combustible', 'gasohol'],
    'Suministros de Oficina': ['papeleria', 'utiles', 'oficina', 'tinta', 'toner'],
    'Alimentación y Víveres': ['restaurante', 'mercado', 'alimentos', 'vivanda', 'wong', 'tottus'],
    'Transporte y Movilidad': ['peaje', 'pasaje', 'taxi', 'transporte'],
    'Herramientas y Mantenimiento': ['ferreteria', 'maestro', 'sodimac', 'herramientas', 'mantenimiento'],
}

def categorize_description(description):
    """
    Recibe el texto de la descripción y devuelve una categoría basada en reglas.
    """
    # Convertimos la descripción a minúsculas para que la búsqueda no distinga mayúsculas/minúsculas
    lower_description = description.lower()

    for category, keywords in CLASSIFICATION_RULES.items():
        for keyword in keywords:
            if keyword in lower_description:
                return category  # Devolvemos la primera categoría que coincida

    return 'Otros Gastos' # Si no coincide ninguna regla, se clasifica como "Otros"

# --- Bloque de prueba ---
if __name__ == '__main__':
    print("--- Probando el clasificador ---")
    desc1 = 'Compra de GASOLINA 95 en el Grifo Repsol de la Av. Arequipa'
    desc2 = 'Almuerzo ejecutivo en Restaurante El Buen Sabor S.A.C.'
    desc3 = 'Servicio de consultoria de software especializado'

    print(f"'{desc1}' -> Categoría: {categorize_description(desc1)}")
    print(f"'{desc2}' -> Categoría: {categorize_description(desc2)}")
    print(f"'{desc3}' -> Categoría: {categorize_description(desc3)}")