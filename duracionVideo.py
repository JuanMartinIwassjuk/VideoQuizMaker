import json
import requests
import audio
import time
import functions_videos
import os
from pathlib import Path
import generatorQuiz
from creatomate import Animation, Image, Element, Composition, Source, Video, Audio
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC,BACKGROUND_IMG,AUTORIZACION,TEXTO_INICIAL,FONDO_INCIO,BACKGROUND_MUSIC


countdown_audio = Path.cwd() / 'audiosEstaticos' / 'countdown.mp3'
transition_audio = Path.cwd() / 'audiosEstaticos' / 'transition.mp3'
ruta_audio_correcta =ruta_audios = Path.cwd() / 'audiosEstaticos' / 'correct.mp3'

data = generatorQuiz.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)

quiz_data_dict=json.loads(data)
def get_duraciones(quiz_data_dict):
    duracion_video="0 s"
    duracion_presentacion=str(audio.obtener_duracion_mp3_en_segundos_sin_formato(os.path.abspath(os.path.join(os.getcwd(), 'audio', str(NUMBER_OF_QUESTIONS)+".mp3")))+2.5)+' s'
    duracion_video=audio.sumar_tiempos(duracion_presentacion,duracion_video)

    duraciones_preguntas=[]

    for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
        duracion_pregunta="0 s"
        duracion_audio_pregunta = audio.obtener_duracion_mp3_en_segundos(os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{index_pregunta}.mp3")))

        duracion_video=audio.sumar_tiempos(duracion_audio_pregunta,duracion_video)
        duracion_pregunta=audio.sumar_tiempos(duracion_audio_pregunta,duracion_pregunta)

        tiempo_audio_correct= audio.sumar_tiempos(duracion_audio_pregunta,"5.1 s")#donde empieza a sonar audio correcto
        duracion_video=audio.sumar_tiempos("5.1 s",duracion_video)#lo q dura el timer y la espera del sonido de respuesta correcta
        duracion_pregunta=audio.sumar_tiempos("5.1 s",duracion_pregunta)
        tiempo_max_timer=duracion_pregunta
        duracion_audio_correcto=audio.obtener_duracion_mp3_en_segundos(ruta_audio_correcta)

        tiempo_max_sonido_correcto=audio.sumar_tiempos(tiempo_audio_correct,duracion_audio_correcto)

        duracion_video=audio.sumar_tiempos(duracion_audio_correcto,duracion_video)#lo q dura el sonido de pregunta correcta
        duracion_pregunta=audio.sumar_tiempos(duracion_audio_correcto,duracion_pregunta)

        if(index_pregunta<NUMBER_OF_QUESTIONS-1):
            duracion_transicion=audio.obtener_duracion_mp3_en_segundos(transition_audio)

            duracion_video=audio.sumar_tiempos("1.2 s",duracion_video)#la espera del sonido de transicion
            duracion_pregunta=audio.sumar_tiempos("1.2 s",duracion_pregunta)#la espera del sonido de transicion

            duracion_video=audio.sumar_tiempos(duracion_transicion,duracion_video)#duracion sonido de transicion
            duracion_pregunta=audio.sumar_tiempos(duracion_transicion,duracion_pregunta)#duracion sonido de transicion

        duraciones_preguntas.append(duracion_pregunta)
        print(f"La duracion de la pregunta{index_pregunta} es ",duracion_pregunta)
    



    print("La duracion total del video es: ",duracion_video)

    return duracion_video,duraciones_preguntas,duracion_presentacion



