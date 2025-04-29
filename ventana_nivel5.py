import tkinter as tk
from niveles_controlador import mostrar_palabra


palabras_nivel = [
    "El sol brilla", "La uva es dulce", "Yo veo un oso", "El niño come", "Ella canta", "El perro corre", "Yo tomo mezcal", "La luna brilla",
    "El gato juega", "La casa es grande", "El pez nada", "La flor es roja", "El río fluye", "La nube es blanca", "El árbol crece"
]
def abrir_nivel5(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Nivel 5: fraces cortas")
    ventana.geometry("480x320")
    ventana.resizable(False, False)

     # Cargar y aplicar fondo
    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mantener referencia al fondo
    ventana.fondo_imagen = fondo_imagen

    label_inicio = tk.Label(ventana, text="¡Vamos a practicar faces cortas", font=("Arial", 16))
    label_inicio.pack(pady=30)

    btn_empezar = tk.Button(
        ventana, text="Comenzar", font=("Arial", 14), bg="blue", fg="white",
        command=lambda: mostrar_palabra(ventana, 0,palabras_nivel)
    )
    btn_empezar.pack(pady=10)
