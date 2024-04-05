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
ruta_audio_correcta = Path.cwd() / 'audiosEstaticos' / 'correct.mp3'
duracion_audio_option = audio.obtener_duracion_mp3_en_segundos(Path.cwd() / 'audiosEstaticos' / 'option.mp3')

duracion_speech_final=audio.obtener_duracion_mp3_en_segundos(Path.cwd() / 'audiosEstaticos' /'final_speech.mp3')
duracion_parte_final=audio.sumar_tiempos(duracion_speech_final,"1 s")




def get_duraciones(quiz_data_dict,opcionesCorrectas):
    duracion_video="0 s"
    duracion_presentacion=audio.obtener_duracion_mp3_en_segundos(os.path.abspath(os.path.join(os.getcwd(), 'audio', str(NUMBER_OF_QUESTIONS)+".mp3")))
    duracion_presentacion=audio.sumar_tiempos(duracion_presentacion,"1 s")
    duracion_video=audio.sumar_tiempos(duracion_presentacion,duracion_video)

    duraciones_preguntas=[]

    for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
        duracion_pregunta="0 s"
        duracion_audio_pregunta = audio.obtener_duracion_mp3_en_segundos(os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{index_pregunta}.mp3")))

        duracion_video=audio.sumar_tiempos(duracion_audio_pregunta,duracion_video)
        duracion_pregunta=audio.sumar_tiempos(duracion_audio_pregunta,duracion_pregunta)

        duracion_video=audio.sumar_tiempos("5.1 s",duracion_video)#lo q dura el timer y la espera del sonido de respuesta correcta
        duracion_pregunta=audio.sumar_tiempos("5.1 s",duracion_pregunta)


        duracion_audio_correcto=audio.obtener_duracion_mp3_en_segundos(ruta_audio_correcta)


        #duracion_opcion_audio=audio.obtener_duracion_mp3_en_segundos(Path.cwd() / 'audiosEstaticos' / 'option.mp3') #duracion de lo que tarda en decir decir option     
        duracion_opcion_correcta_char=audio.obtenerDuracionSegundosAudioDeOpcion(opcionesCorrectas[index_pregunta])#duracion de lo que tarda en decir la letra de opcion correcta
       
    
        #duracion_opcion_correcta_total=audio.sumar_tiempos(duracion_opcion_audio,duracion_opcion_correcta_char)#lo que tarda en decir opcion x
        duracion_opcion_correcta_total=audio.sumar_tiempos(duracion_opcion_correcta_char,"0.5 s")#se le agrega un segundo de espera

        
        duracion_contenido_correcto = audio.obtener_duracion_mp3_en_segundos( Path.cwd() / 'audio' / (str(index_pregunta) + "-correct" + ".mp3") ) #Esto es lo que tarda en decir "option x" + una pausa de 0.5s
        duracion_opcion_correcta_total=audio.sumar_tiempos(duracion_opcion_correcta_total,duracion_contenido_correcto)
        
        
        
        duracion_video=audio.sumar_tiempos(audio.comparar_tiempos(duracion_audio_correcto,duracion_opcion_correcta_total),duracion_video)#lo q dura el sonido de pregunta correcta
        duracion_pregunta=audio.sumar_tiempos(audio.comparar_tiempos(duracion_audio_correcto,duracion_opcion_correcta_total),duracion_pregunta)

        if(index_pregunta<NUMBER_OF_QUESTIONS-1):
            duracion_transicion=audio.obtener_duracion_mp3_en_segundos(transition_audio)

            duracion_video=audio.sumar_tiempos("1.2 s",duracion_video)#la espera del sonido de transicion
            duracion_pregunta=audio.sumar_tiempos("1.2 s",duracion_pregunta)#la espera del sonido de transicion

            duracion_video=audio.sumar_tiempos(duracion_transicion,duracion_video)#duracion sonido de transicion
            duracion_pregunta=audio.sumar_tiempos(duracion_transicion,duracion_pregunta)#duracion sonido de transicion

        duraciones_preguntas.append(duracion_pregunta)
        print(f"La duracion de la pregunta{index_pregunta} es ",duracion_pregunta)
    



    print("La duracion total del video es: ",duracion_video)
    duracion_video=audio.sumar_tiempos(duracion_video,duracion_parte_final)
    return duracion_video,duraciones_preguntas,duracion_presentacion,duracion_parte_final



