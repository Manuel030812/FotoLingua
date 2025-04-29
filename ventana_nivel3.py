import tkinter as tk
from niveles_controlador import mostrar_palabra


palabras_nivel = [
    "uva", "unicornio", "uno", "útil", "urraca", "universo", "utensilio",
    "avión", " elefante", "isla", "olla", "uniforme"
]

def abrir_nivel3(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Nivel 3: Palabras con U y repaso")
    ventana.geometry("480x320")
    ventana.resizable(False, False)

     # Cargar y aplicar fondo
    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mantener referencia al fondo
    ventana.fondo_imagen = fondo_imagen

    label_inicio = tk.Label(ventana, text="¡Vamos a practicar palabras con U y Repaso!", font=("Arial", 16))
    label_inicio.pack(pady=30)

    btn_empezar = tk.Button(
        ventana, text="Comenzar", font=("Arial", 14), bg="blue", fg="white",
        command=lambda: mostrar_palabra(ventana, 0,palabras_nivel)
    )
    btn_empezar.pack(pady=10)
