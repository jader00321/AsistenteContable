<p align="center">
  <img src="icono_organizador.ico" alt="Asistente Contable Logo" width="120">
</p>

<h1 align="center">Asistente Contable Automático (Beta)</h1>

<p align="center">
  <strong>Automatización inteligente para la extracción y registro de comprobantes electrónicos en entornos contables.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-🚧%20En%20Desarrollo%20/%20Beta-orange" alt="Status">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PySide6">
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel">
</p>

---

## 📖 Descripción del Proyecto

El **Asistente Contable** es una herramienta de escritorio diseñada para eliminar la carga manual de datos en procesos contables. Su función principal es navegar automáticamente por portales fiscales (como la SUNAT en Perú), extraer información de facturas y organizarlas sistemáticamente en archivos Excel listos para la declaración de impuestos.

> **Nota de Fase Beta:** Este proyecto se encuentra actualmente en fase de pruebas. Las funciones principales de extracción y clasificación son operativas, mientras que la interfaz de usuario y la lógica de validación avanzada están en proceso de refinamiento.

## ✨ Funcionalidades Actuales

* **🤖 Motor de Automatización:** Uso de `Playwright` para la navegación controlada y extracción de datos desde portales web (Web Scraping).
* **📋 Clasificador Inteligente:** Lógica implementada en `classifier.py` para categorizar comprobantes según tipos de gasto o impuestos.
* **📊 Gestión de Datos:** Manejo de estructuras de datos complejas y exportación optimizada a Excel mediante `data_handler.py`.
* **🖥️ Interfaz de Escritorio:** GUI funcional construida con `PySide6` que permite gestionar los flujos de trabajo de manera visual.
* **🧪 Entorno de Pruebas Seguro:** Incluye un entorno `mock_sunat.html` para realizar pruebas de extracción sin afectar servidores reales.

---

## 🛠️ Arquitectura Técnica

El sistema sigue una arquitectura modular para facilitar el mantenimiento y la escalabilidad de las funciones contables:

<details>
<summary><b>Ver flujo de trabajo (Pipeline)</b></summary>

<br>

1. **Captura:** El `automation_engine.py` inicia la navegación y captura el DOM de la página fiscal.
2. **Procesamiento:** El motor de extracción limpia el ruido visual y extrae campos clave (RUC, Monto, IGV, Fecha).
3. **Clasificación:** El módulo `classifier.py` aplica reglas lógicas para organizar la información.
4. **Persistencia:** `data_handler.py` consolida los datos en el archivo `facturas.xlsx`.

</details>

<details>
<summary><b>Tecnologías Utilizadas</b></summary>

<br>

* **Lenguaje:** Python 3.x
* **Automatización:** Playwright (Chromium/Webkit)
* **GUI:** PySide6 (Qt para Python)
* **Data Ops:** Openpyxl / Pandas
* **Testing:** Entorno local simulado (Mocking)

</details>

---

## 🚀 Instalación y Pruebas Locales

Para probar el asistente en tu entorno local, sigue estos pasos:

### 1. Pre-requisitos
* Tener instalado **Python 3.9+**.
* Instalar los navegadores necesarios para la automatización.

### 2. Configuración del entorno
    ```bash
    # Crear entorno virtual
    python -m venv venv

    # Activar entorno (Windows)
    .\venv\Scripts\activate

    # Instalar dependencias
    pip install -r requirements.txt

    # Instalar navegadores de Playwright
    playwright install chromium


### 3. Ejecución
    ```bash
    python main_app.py
    

### 📈 Próximos Pasos (Roadmap)

[ ] Implementación de OCR para lectura de facturas en formato imagen/PDF.

[ ] Rediseño de la interfaz de usuario con estilos modernos y animaciones.

[ ] Soporte multihilo para procesar múltiples facturas simultáneamente.

[ ] Dashboard estadístico de gastos acumulados.

---

Proyecto desarrollado con el objetivo de optimizar la eficiencia contable mediante tecnología.

