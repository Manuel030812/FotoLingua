import tkinter as tk
from niveles_controlador import mostrar_palabra

palabras_nivel = [
    "agua", "ave", "alto", "amigo", "araña", "abuelo", "anillo",
    "espejo", "elefante", "estrella", "escuela", "enano", "estufa", "espera"
]

def abrir_nivel1(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Nivel 1: Palabras con A y E")
    ventana.geometry("480x320")
    ventana.resizable(False, False)

    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo_imagen = fondo_imagen

    label_inicio = tk.Label(ventana, text="¡Vamos a practicar palabras con A y E!", font=("Arial", 16))
    label_inicio.pack(pady=25)

    btn_empezar = tk.Button(
        ventana, text="Comenzar", font=("Arial", 14), bg="blue", fg="white",
        command=lambda: mostrar_palabra(ventana, 0, palabras_nivel)
    )
    btn_empezar.pack(pady=10)
