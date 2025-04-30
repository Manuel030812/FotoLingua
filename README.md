# 📸 FotoLingua

**FotoLingua** es un proyecto en Python cuyo objetivo es ayudar a las personas a aprender a leer mediante la detección de imágenes y la lectura de frases u oraciones.

---

## 🧩 Requisitos previos

Antes de ejecutar el proyecto, es necesario descargar los siguientes archivos:

1. **Modelo YOLO para detección de objetos:**  
   👉 [Descargar yolov5m.pt](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5m.pt)

2. **Modelo Vosk para reconocimiento de voz (offline):**  
   👉 [Descargar vosk-model-small-es-0.42.zip](https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip)  
   📦 *Recuerda descomprimir este archivo después de descargarlo.*

3. **Carpeta de audios utilizados en el proyecto:**  
   👉 [Descargar carpeta de audios](https://drive.google.com/drive/folders/1wiv2mZklyMAHfgTZ377jDz83LM_xfMa2?usp=sharing)

---

## 🐍 Crear entorno virtual (Linux recomendado)

Para aislar las dependencias del proyecto, se recomienda crear y activar un entorno virtual:

```bash
# Crear el entorno virtual (puedes usar el nombre que desees)
python3 -m venv libproyecto

# Activar el entorno virtual
source libproyecto/bin/activate

#📦 Instalación de dependencias
#Con el entorno virtual activado, instala las siguientes librerías necesarias:
pip install pillow          # Para manejar imágenes en interfaces Tkinter
pip install opencv-python   # Para captura de video y visión por computadora
pip install sounddevice     # Para captura de audio desde el micrófono
pip install vosk            # Para reconocimiento de voz sin conexión
pip install pygame          # Para reproducir audios
pip install ultralytics     # Para utilizar modelos YOLO
#✅ ¡Listo para aprender!
#Una vez cumplidos todos estos pasos, el proyecto estará listo para ejecutarse.

#¡Esperamos que disfrutes aprendiendo con FotoLingua! 📚🖼️🔊

#Solo cópialo tal cual y pégalo en tu terminal de linux.










