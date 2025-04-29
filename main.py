import tkinter as tk
from ventana_objetos import abrir_ventana_objetos
from ventana_textos import abrir_menu_textos
from reproducir_audio import reproducir_audio_loop, detener_audio

def mostrar_menu_principal():
    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("480x320")
    root.resizable(False, False)

  

     # --- Fondo ---
    fondo_imagen = tk.PhotoImage(file="assets/fondo.png")
    fondo_label = tk.Label(root, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


    # Título
    titulo = tk.Label(root, text="Bienvenido al Sistema", font=("Arial", 16), bg="#000000",fg="white" )
    titulo.pack(pady=20)

    # Botón para detectar objetos
    btn_objetos = tk.Button(
        root,
        text="Detecta Objetos",
        font=("Arial", 14),
        bg="green",
        fg="white",
        relief="flat",
        activebackground="#d9a06b",  # Color al presionar
        activeforeground="#495239",  # Texto permanece igual al presionar
        bd=0,    # Sin bordes
        padx=20,
        command=lambda: [
            detener_audio(),
            root.iconify(),
            abrir_ventana_objetos(root)
        ]
    )
    btn_objetos.pack(pady=10)

    # Botón para textos
    btn_textos = tk.Button(
        root,
        text="Textos",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=lambda: [
            detener_audio(),
            root.iconify(),
            abrir_menu_textos(root)
        ]
    )
    btn_textos.pack(pady=10)

      # Reproducir audio de bienvenida en loop
    reproducir_audio_loop("bienvenida.mp3")

     # Mantener referencia al fondo
    root.fondo_imagen = fondo_imagen

    root.mainloop()

if __name__ == "__main__":
    mostrar_menu_principal()
