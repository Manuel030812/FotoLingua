# reproducir_audio.py
import pygame
import os
import time


pygame.mixer.init()

def reproducir_audio_loop(nombre_archivo):
    ruta_audio = os.path.join("audios", nombre_archivo)
    if os.path.exists(ruta_audio):
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play(loops=0)  # Reproducir en bucle infinito
    else:
        print("Archivo no encontrado:", ruta_audio)
    

        
def reproducir_audio_una_vez(nombre_archivo):
    ruta_audio = os.path.join("audios/niveles", nombre_archivo+".mp3")
    if os.path.exists(ruta_audio):
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play(loops=0)  # Reproducir una sola vez
    else:
        print("Archivo no encontrado:", ruta_audio)

def reproducir_objeto(nombre_archivo):
    ruta_audio = os.path.join("audios/objetos", nombre_archivo+".mp3")
    if os.path.exists(ruta_audio):
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play(loops=0)  # Reproducir una sola vez
    else:
        print("Archivo no encontrado:", ruta_audio)

def detener_audio():
    pygame.mixer.music.stop()
