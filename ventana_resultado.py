import tkinter as tk
from tkinter import Label, Button, messagebox
from PIL import Image, ImageTk
import cv2
import threading
import sounddevice as sd
import queue
import json
import sys
from vosk import Model, KaldiRecognizer
from reproducir_audio import reproducir_objeto, reproducir_audio_loop

model_vosk = Model("vosk-model-small-es-0.42")

def activar_microfono_y_comparar(objetos):
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    def reconocimiento():
        with q.mutex:
            q.queue.clear()

        recognizer = KaldiRecognizer(model_vosk, 16000)

        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):
            print("🎤 Escuchando...")
            while True:
                data = q.get()
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    dicho = result.get("text", "")
                    print("🗣️ Dijiste:", dicho)

                    if any(obj.lower() in dicho.lower() for obj in objetos):
                        messagebox.showinfo("Correcto", f"✅ ¡Bien dicho! Objeto reconocido: '{dicho}'")
                    else:
                        messagebox.showerror("Incorrecto", f"❌ Dijiste: '{dicho}'\nNo coincide con los objetos: {', '.join(objetos)}")
                    break

    threading.Thread(target=reconocimiento).start()

def mostrar_resultado(frame, objetos, parent):
    ventana_resultado = tk.Toplevel(parent)
    ventana_resultado.title("Resultado de la Foto")
    ventana_resultado.geometry("480x320")
    ventana_resultado.resizable(False, False)
    # Cargar y aplicar fondo
    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana_resultado, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mantener referencia al fondo
    ventana_resultado.fondo_imagen = fondo_imagen
   

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    img = img.resize((220, 165))
    imgtk = ImageTk.PhotoImage(image=img)

    imagen_resultado = Label(ventana_resultado, image=imgtk)
    imagen_resultado.imgtk = imgtk
    imagen_resultado.place(x=10, y=10, width=220, height=165)

    texto = "Objetos detectados: " + (", ".join(objetos) if objetos else "Ninguno")
    resultado_label = Label(ventana_resultado, text=texto, font=("Arial", 9), wraplength=220, justify="left")
    resultado_label.place(x=10, y=185)

    

    def volverMenu():
        import main
        ventana_resultado.destroy()
        parent.deiconify()
        reproducir_audio_loop("bienvenida.mp3")

    btn_regresar_camara = Button(ventana_resultado, text="Tomar Otra Foto", font=("Arial", 10),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        command=lambda: (ventana_resultado.destroy(), __import__('ventana_objetos').abrir_ventana_objetos(parent)))
    btn_regresar_camara.place(x=260, y=190)

    btn_menu_principal = Button(ventana_resultado, text="Menú Principal", font=("Arial", 10),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        command=lambda: volverMenu())
    btn_menu_principal.place(x=260, y=230)

    btn_escuchar = Button(
        ventana_resultado, text="Escuchar Palabra", font=("Arial", 10), bg="green", fg="black",
        command=lambda: reproducir_objeto(objetos[0] if objetos else "desconocido"))
    btn_escuchar.place(x=260, y=110)

    btn_voz = Button(ventana_resultado, text="Leer Objeto", font=("Arial", 10),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        command=lambda: activar_microfono_y_comparar(objetos))
    btn_voz.place(x=260, y=150)

   
   