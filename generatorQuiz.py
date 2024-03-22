from openai import OpenAI
import json
import os
from config import API_KEY, MODEL_NAME
from pathlib import Path
client = OpenAI(api_key=API_KEY)
def get_openai_response_in_json_format(number_of_questions, number_of_options, difficulty_level, topic):
    if ((comparar_parametros_con_json(number_of_questions, number_of_options, difficulty_level, topic)==False)): # Si Son iguales los parámetros actuales con la consulta anterior
        prompt = f"generate {number_of_questions} specific questions with a difficulty level of {difficulty_level} about the topic {topic}"
        # Utilizar el cliente para crear completaciones de chat
        response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": f'You need to provide {number_of_questions} specific questions about the topic {topic} with a difficulty level of {difficulty_level}. Each question should have {number_of_options} options, including the correct answer. Do not use single quotes, and your response should be in JSON format like this: openkey "questions": [ openkey "question": "Sample question?", "options": ["A) Option A",B) "Option B", "C) Option C"], "correct_answer": "A) Option A" closedkey ] closedkey'},
            {"role": "user", "content": prompt}
        ]
            )


        
        # Obtener la respuesta en formato JSON
        json_response = response.choices[0].message.content
        print(json_response)

        guardar_datos_en_json(number_of_questions, number_of_options, difficulty_level, topic)
        with open(os.getcwd()+'/response'+'/'+"data.txt", "w") as file:
                file.write(json_response)
        return json_response
    else: return obtener_contenido_txt()
          
def guardar_datos_en_json(number_of_questions, number_of_options, difficulty_level, topic):
    # Crear un diccionario con los datos
    data = {
        "number_of_questions": number_of_questions,
        "number_of_options": number_of_options,
        "difficulty_level": difficulty_level,
        "topic": topic
    }
    with open(os.getcwd()+'/response'+'/'+"lastParameters.txt", "w") as file:
        # Escribir los datos en formato JSON
        json.dump(data,file)
def comparar_parametros_con_json(number_of_questions, number_of_options, difficulty_level, topic):
    if (os.path.getsize(os.getcwd()+'/response'+'/'+"lastParameters.txt") != 0):#No Esta vacio
        # Cargar los datos del archivo JSON
        with open(os.getcwd()+'/response'+'/'+"lastParameters.txt", "r") as file:
            datos = json.load(file)
        # Comparar los valores con los parámetros
        if (datos["number_of_questions"] == number_of_questions and
            datos["number_of_options"] == number_of_options and
            datos["difficulty_level"] == difficulty_level and
            datos["topic"] == topic):
            return True
        else:
            return False
    else: return False
def obtener_contenido_txt():
    ruta_archivo = os.path.join(os.getcwd(), 'response', 'data.txt')
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido



def verificar_archivo_vacio():
    if os.path.getsize(os.getcwd()+'/response'+'/'+"lastParameters.txt") == 0:
        return True
    else:
        return False

def es_la_misma_que_anterior(number_of_questions, number_of_options, difficulty_level, topic):
    if not verificar_archivo_vacio():
        # Cargar los datos del archivo JSON
        with open(os.getcwd()+'/response'+'/'+"lastParameters.txt", "r") as file:
            datos = json.load(file)
        # Comparar los valores con los parámetros
        if (datos["number_of_questions"] == number_of_questions and
            datos["number_of_options"] == number_of_options and
            datos["difficulty_level"] == difficulty_level and
            datos["topic"] == topic):
            return True
    return False
