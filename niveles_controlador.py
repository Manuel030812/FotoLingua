import tkinter as tk
import threading
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from tkinter import messagebox
from reproducir_audio import reproducir_audio_una_vez

fondo_imagen = None
# Modelo Vosk
model = Model("vosk-model-small-es-0.42")
q = queue.Queue()

def escuchar_y_validar(palabra, mostrar_boton_siguiente):
    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    def reconocer():
        with q.mutex:
            q.queue.clear()
        rec = KaldiRecognizer(model, 16000)
        
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                                channels=1, callback=callback):
            print("🎤 Escuchando...")
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    dicho = result.get("text", "")
                    print("🗣️ Dijiste:", dicho)
                    if palabra.lower() == dicho.lower():
                        messagebox.showinfo("Correcto", f"✅ ¡Bien dicho! Palabra reconocida: '{palabra}'")
                        mostrar_boton_siguiente()
                    else:
                        messagebox.showwarning("Intenta otra vez", f"❌ Dijiste: '{dicho}'\nIntenta decir: '{palabra}'")
                    break

    threading.Thread(target=reconocer).start()

def mostrar_palabra(ventana, indice, palabras_nivel):
    global fondo_imagen  # Evitar que se borre la imagen del fondo


    for widget in ventana.winfo_children():
        widget.destroy()


     # ========== FONDO ==========
    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo_imagen = fondo_imagen
    # ============================

    if indice >= len(palabras_nivel):
        messagebox.showinfo("¡Felicidades!", "🎉 Has completado todas las palabras del Nivel.")
        ventana.destroy()
        return

    palabra = palabras_nivel[indice]

    label = tk.Label(ventana, text=palabra, font=("Arial", 35), fg="blue")
    label.pack(pady=20)

    btn_escuchar = tk.Button(
        ventana, text="Escuchar Palabra", font=("Arial", 9), width=20,
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        command=lambda: reproducir_audio_una_vez(palabra))
    btn_escuchar.pack(pady=5)

    btn_microfono = tk.Button(
        ventana, text="🎤 Decir Palabra", font=("Arial", 9), width=20, bg="green", fg="white",
        command=lambda: escuchar_y_validar(palabra, mostrar_siguiente)
    )
    btn_microfono.pack(pady=5)

    btn_siguiente = tk.Button(
        ventana, text="Siguiente", font=("Arial", 9), width=22, state="disabled",
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        command=lambda: mostrar_palabra(ventana, indice + 1, palabras_nivel)
    )
    btn_siguiente.pack(pady=5)

    def mostrar_siguiente():
        btn_siguiente.config(state="normal")
