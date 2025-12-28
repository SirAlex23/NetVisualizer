# 🌐 NetVisualizer: Global Network Traffic Monitor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Scapy-0096D6?style=for-the-badge&logo=python&logoColor=white" alt="Scapy" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
</p>

**NetVisualizer** es una herramienta de ciberseguridad diseñada para capturar, geolocalizar y visualizar el tráfico saliente en tiempo real. Transforma datos crudos de red en un dashboard interactivo con un mapa de rutas globales y un registro detallado de IPs capturadas.

---

## 🚀 Características Principales

* **🛰️ Sniffing en Tiempo Real**: Analiza paquetes TCP/IP directamente desde la tarjeta de red.
* **🌍 Inteligencia Geoespacial**: Identifica ciudad y país de destino mediante APIs de geolocalización.
* **📊 Dashboard Profesional**: Visualización unificada con mapa Miller y log lateral.
* **🛡️ Filtrado de Tráfico**: Omite conexiones locales (LAN) para centrarse exclusivamente en tráfico externo.

---

## 🛠️ Instalación y Configuración

Sigue estos pasos exactos para configurar el proyecto en tu máquina local:

### Clonar el repositorio
```bash
git clone [https://github.com/TuUsuario/NetVisualizer.git](https://github.com/TuUsuario/NetVisualizer.git)
cd NetVisualizer


# Crear el entorno virtual
python -m venv venv

# Activar el entorno
.\venv\Scripts\activate

# Instalar dependencias necesarias
pip install scapy plotly requests pandas

# Ejecución con Privilegios 
[!!!IMPORTANTE]
Para capturar tráfico de red, Windows requiere permisos de Administrador. Asegúrate de ejecutar VS Code o la Terminal como Administrador.

python main.py


# Generar el Mapa Final 
Una vez ejecutado, navega por diferentes sitios web (YouTube, Netflix, etc.) para generar tráfico real.
El programa mostrará en consola las IPs detectadas en tiempo real.
Pulsa Ctrl + C para detener la captura de forma segura.
El script generará automáticamente el archivo mapa_mundial.html con el dashboard final.



