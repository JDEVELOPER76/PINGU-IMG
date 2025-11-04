# 🐧 PINGU  
### Herramienta Profesional de Procesamiento de Imágenes  

![Banner](pingu.PNG)

---

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-cx--Freeze-orange)](#)
[![Status](https://img.shields.io/badge/Estado-Estable-success.svg)](#)

---

## 🧩 Descripción

**Pingu** es una herramienta CLI (Command Line Interface) profesional para **procesamiento de imágenes**, desarrollada en **Python**.  
Ofrece una experiencia visual atractiva con texto en color, menús claros y una arquitectura modular basada en complementos (plugins y tools).

Diseñada para técnicos, fotógrafos o desarrolladores que necesitan automatizar tareas de imágenes de manera eficiente.

---

## ⚙️ Características

✅ Interfaz de consola profesional con **colorama**  
✅ Soporte completo para **Windows 10 / 11**  
✅ Motor gráfico basado en **Pillow (PIL)**  
✅ Modularidad mediante carpetas `PLUGINS` y `TOOLS`  
✅ Comandos integrados para ayuda, limpieza y conexión de carpetas  
✅ Compilación nativa a `.exe` o `.msi` con **cx_Freeze**  

---

## 🖥️ Comandos principales

| Comando | Descripción |
|----------|--------------|
| `/ayuda` | Muestra información sobre los comandos disponibles |
| `/mas` | Muestra información adicional sobre la aplicación |
| `/limpiar` | Limpia la consola |
| `/salir` | Cierra la aplicación |
| `/conectar_carpeta` | Conecta una carpeta de trabajo para procesar imágenes |

---

## 🧠 Requisitos

- **Python 3.10 o superior**
- Librerías necesarias:
  ```bash
  pip install pillow colorama
