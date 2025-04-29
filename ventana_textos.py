import tkinter as tk
from reproducir_audio import reproducir_audio_loop, detener_audio

# Importa aquí tus módulos de niveles (debes crearlos):
from ventana_nivel1 import abrir_nivel1
from ventana_nivel2 import abrir_nivel2
from ventana_nivel3 import abrir_nivel3
from ventana_nivel4 import abrir_nivel4
from ventana_nivel5 import abrir_nivel5

def abrir_menu_textos(parent):
    """
    Abre una ventana con botones para seleccionar los diferentes niveles de lectura.
    Cada botón debe llamar a la función correspondiente de su nivel.
    """
    ventana = tk.Toplevel(parent)
    ventana.title("Menú de Textos")
    ventana.geometry("480x320")  # Resolución ajustada para Raspberry Pi
    ventana.resizable(False, False)
    reproducir_audio_loop("menulectura.mp3")


     # Cargar y aplicar fondo
    fondo_imagen = tk.PhotoImage(file="assets/fondo.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mantener referencia al fondo
    ventana.fondo_imagen = fondo_imagen


    # Título principal
    lbl_titulo = tk.Label(
        ventana,
        text="Selecciona un nivel de lectura",
        font=("Arial", 14, "bold")
    )
    lbl_titulo.pack(pady=10)

    # Botones de niveles (compactos)
    btn_nivel1 = tk.Button(
        ventana,
        text="Nivel 1: palabras con A y E",
        font=("Arial", 9),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        pady=10,
        width=20,
        command=lambda: (abrir_nivel1(ventana),detener_audio())
    )
    btn_nivel1.pack(pady=3)

    btn_nivel2 = tk.Button(
        ventana,
        text="Nivel 2: palabras con I y O",
        font=("Arial", 9),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        pady=10,
        command=lambda: (abrir_nivel2(ventana),detener_audio())
    )
    btn_nivel2.pack(pady=3)

    btn_nivel3 = tk.Button(
        ventana,
        text="Nivel 3: palabras con U y repaso",
        font=("Arial", 9),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        pady=10,
        command=lambda:(abrir_nivel3(ventana),detener_audio())
    )
    btn_nivel3.pack(pady=3)

    btn_nivel4 = tk.Button(
        ventana,
        text="Nivel 4: palabras cotidianas",
        font=("Arial", 9),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        pady=10,
        command=lambda: (abrir_nivel4(ventana),detener_audio())
    )
    btn_nivel4.pack(pady=3)

    btn_nivel5 = tk.Button(
        ventana,
        text="Nivel 5: Frases Cortas",
        font=("Arial",9 ),
        bg="#C68B4E",    # Color marrón claro del botón (lo saqué de la imagen)
        fg="black",    # Color verde oscuro del texto (lo saqué de la imagen)
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        pady=10,
        command=lambda: (abrir_nivel5(ventana),detener_audio())
    )
    btn_nivel5.pack(pady=3)

    # Función para volver al menú principal
    def volver_al_menu():
        import main  # Importación tardía para evitar importación circular
        detener_audio()  # Detener audio de esta ventana
        ventana.destroy()
        parent.deiconify()
        reproducir_audio_loop("bienvenida.mp3")  # Reproducir audio de bienvenida

    # Botón para regresar al menú principal
    btn_cerrar = tk.Button(
        ventana,
        text="Volver al Menú Principal",
        font=("Arial", 11, "bold"),
        width=20,
        command=volver_al_menu,
        bg="#f0ad4e",  # Color de fondo (naranja suave)
        fg="white"    # Texto blanco
    )
    btn_cerrar.pack(pady=10)
