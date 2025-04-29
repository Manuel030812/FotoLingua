import tkinter as tk
from tkinter import Label, Button
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
from reproducir_audio import reproducir_audio_loop, detener_audio
from ventana_resultado import mostrar_resultado  # Importar desde ventana_resultado

# Cargar el modelo
model = YOLO("yolov5m.pt")

# Traducción de clases (puedes moverla a un archivo aparte si quieres)
class_translation = {
    "person": "persona", "bicycle": "bicicleta", "car": "auto", "motorbike": "motocicleta", 
    "aeroplane": "avión", "bus": "autobús", "train": "tren", "truck": "camión", 
    "boat": "barco", "traffic light": "semáforo", "fire hydrant": "hidrante", 
    "stop sign": "señal de alto", "parking meter": "parquímetro", "bench": "banco", 
    "bird": "pájaro", "cat": "gato", "dog": "perro", "horse": "caballo", "sheep": "oveja", 
    "cow": "vaca", "elephant": "elefante", "bear": "oso", "zebra": "cebra", 
    "giraffe": "jirafa", "backpack": "mochila", "umbrella": "paraguas", "handbag": "bolso", 
    "tie": "corbata", "suitcase": "maleta", "frisbee": "frisbi", "skis": "esquís", 
    "snowboard": "tabla de snowboard", "sports ball": "pelota", "kite": "cometa", 
    "baseball bat": "bate de béisbol", "baseball glove": "guante de béisbol", 
    "skateboard": "patineta", "surfboard": "tabla de surf", "tennis racket": "raqueta de tenis", 
    "bottle": "botella", "wine glass": "copa de vino", "cup": "taza", "fork": "tenedor", 
    "knife": "cuchillo", "spoon": "cuchara", "bowl": "tazón", "banana": "plátano", 
    "apple": "manzana", "sandwich": "sándwich", "orange": "naranja", "broccoli": "brócoli", 
    "carrot": "zanahoria", "hot dog": "hot dog", "pizza": "pizza", "donut": "dona", 
    "cake": "pastel", "chair": "silla", "sofa": "sofá", "potted plant": "maceta", 
    "bed": "cama", "dining table": "mesa de comedor", "toilet": "inodoro", 
    "tvmonitor": "televisión", "laptop": "laptop", "mouse": "ratón", "remote": "control remoto", 
    "keyboard": "teclado", "cell phone": "celular", "microwave": "microondas", 
    "oven": "horno", "toaster": "tostadora", "sink": "fregadero", "refrigerator": "refrigerador", 
    "book": "libro", "clock": "reloj", "vase": "jarrón", "scissors": "tijeras", 
    "teddy bear": "osito de peluche", "hair drier": "secador de pelo", "toothbrush": "cepillo de dientes"
}


# Variable global
objetos_detectados = []

def abrir_ventana_objetos(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Detección de Objetos")
    ventana.geometry("480x320")
    ventana.resizable(False, False)
    reproducir_audio_loop("tomarFoto.mp3")

     # Cargar y aplicar fondo
    fondo_imagen = tk.PhotoImage(file="assets/fondo2.png")
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mantener referencia al fondo
    ventana.fondo_imagen = fondo_imagen

    cap = cv2.VideoCapture(0)

    video_label = Label(ventana)
    video_label.place(x=10, y=10, width=220, height=165)

    btn = Button(ventana, text="Tomar Foto", font=("Arial", 10), bg="green",
                 command=lambda: (tomar_foto_y_mostrar(cap, ventana, parent), detener_audio()))
    btn.place(x=10, y=190)

    def actualizar_video():
        ret, frame = cap.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            img = img.resize((220, 165))
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
        ventana.after(10, actualizar_video)

    actualizar_video()
    ventana.protocol("WM_DELETE_WINDOW", lambda: (cap.release(), ventana.destroy()))

def tomar_foto_y_mostrar(cap, ventana_cam, parent):
    ret, frame = cap.read()
    if not ret:
        return

    ventana_cam.destroy()
    cap.release()

    resultados = model(frame)
    global objetos_detectados
    objetos_detectados = []

    max_area = 0
    objeto_principal = None

    for result in resultados:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            area = (x2 - x1) * (y2 - y1)

            if area > max_area:
                max_area = area
                class_id = int(box.cls)
                class_name = result.names[class_id]
                class_name_es = class_translation.get(class_name, class_name)
                objeto_principal = (class_name_es, x1, y1, x2, y2)

    if objeto_principal:
        class_name_es, x1, y1, x2, y2 = objeto_principal
        objetos_detectados.append(class_name_es)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, class_name_es, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    mostrar_resultado(frame, objetos_detectados, parent)
