# automation_engine.py
import asyncio
from playwright.async_api import async_playwright
import os

async def fetch_invoice_description(invoice_data):
    """
    Navega a la página local simulada, llena el formulario y extrae la descripción.
    invoice_data debe ser un diccionario con claves: 'ruc', 'serie', 'numero'.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) # headless=True para que no se vea el navegador
        page = await browser.new_page()
        
        # Construimos la ruta al archivo HTML local
        file_path = os.path.abspath('mock_sunat.html')
        
        try:
            # Navegamos a nuestro archivo local
            await page.goto(f'file://{file_path}')
            
            # Rellenamos el formulario con los datos de la factura
            await page.fill('#ruc', invoice_data['ruc'])
            await page.fill('#serie', invoice_data['serie'])
            await page.fill('#numero', invoice_data['numero'])
            
            # Hacemos clic en el botón de consulta
            await page.click('button[onclick="showResult()"]')
            
            # Esperamos a que el contenedor del resultado sea visible
            # Esta es la "espera explícita" crucial para la robustez
            await page.wait_for_selector('#result-container', state='visible', timeout=5000)
            
            # Extraemos el texto de la descripción
            description_element = await page.query_selector('#invoice-description')
            description = await description_element.inner_text() if description_element else "Descripción no encontrada"
            
            await browser.close()
            return description.strip()

        except Exception as e:
            await browser.close()
            print(f"Error durante la automatización para la factura {invoice_data}: {e}")
            return "Error al procesar"

# --- Bloque de prueba ---
async def main_test():
    print("--- Probando el motor de automatización ---")
    
    # Factura 1 (debería encontrar "combustible")
    test_invoice_1 = {'ruc': '20100055555', 'serie': 'F001', 'numero': '1234'}
    desc1 = await fetch_invoice_description(test_invoice_1)
    print(f"Factura {test_invoice_1['numero']}: {desc1}")
    
    # Factura 2 (debería encontrar "oficina")
    test_invoice_2 = {'ruc': '20455566666', 'serie': 'F002', 'numero': '567'}
    desc2 = await fetch_invoice_description(test_invoice_2)
    print(f"Factura {test_invoice_2['numero']}: {desc2}")

if __name__ == '__main__':
    asyncio.run(main_test())