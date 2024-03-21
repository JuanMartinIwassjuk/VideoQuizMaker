import json
import audio
import os
from config import NUMBER_OF_QUESTIONS

def generarArchivoDeljson(json):
    with open("resultado_json","w") as arch:
     arch.write(json.toJSON())


def generar_tiempo_video(cant_preguntas):
    resultado = str((cant_preguntas * 10)+1.5+audio.obtener_duracion_mp3_en_segundos_sin_formato(os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{str(NUMBER_OF_QUESTIONS)}.mp3")))) + ' s'
    return resultado

def encontrar_indice(lista, cadena):
    try:
        indice = lista.index(cadena)
        return indice
    except ValueError:
        # Si no se encuentra la cadena en la lista, se devuelve -1
        return -1
