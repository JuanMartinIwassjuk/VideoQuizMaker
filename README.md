#Generación del Video

Para crear un video , seguir los siguientes pasos:

1. Ejecutar el siguiente comando para descargar las dependencias de python:

pip install openai requests google-api-python-client google-auth-oauthlib mutagen


2. Debés tener una cuenta de "creatomate.com" y obtener el código de autorización para enviar el request: debe ser algo así:
c623356c25cf47a999df4684c11d6bc8af5g486da8ac9ab718atkc26ada2f5cb37981ab32767cd0561936e91e3e08b01

1. Crear el archivo de configuración
En la carpeta principal del proyecto, crea un archivo llamado "config.py".

3.1. Configuración del archivo
Abre el archivo "config.py" y personalízalo según tus preferencias para diseñar el Quiz y enviar el request. Asegúrate de incluir las siguientes características:

# Key para consultarle a la api de OpenAI
API_KEY = 'api_key'

# Nombre del modelo de OpenAI
MODEL_NAME = 'modelo_de_chatgtp'

# Número de preguntas en el Quiz
NUMBER_OF_QUESTIONS = 2

# Número de opciones por pregunta
NUMBER_OF_OPTIONS = 3

# Nivel de dificultad del Quiz (opciones: 'very_easy','easy','easy-normal', 'normal','normal-hard', 'hard','very_hard')
LEVEL_OF_DIFFICULTY = 'normal'

# Tema del Quiz
TOPIC = 'history'

# Las imágenes de fondo de cada pregunta, deberán venir en formato json
BACKGROUND_IMG='["url_imagen_pregunta_1","url_imagen_pregunta_2"]'

# La autorización para el envío del request mencionado anteriormente
AUTORIZACION='c623356c25cf47a999df4684c11d6bc8af5g486da8ac9ab718atkc26ada2f5cb37981ab32767cd0561936e91e3e08b01'

El archivo para que funcione correctamente deberia quedar algo así:
![Los valores proporcionados para "API_KEY" y "autorizacion" son meramente ejemplos ilustrativos y no tienen la funcionalidad real de acceso.](https://github.com/JuanMartinIwassjuk/generatorQuiz/blob/main/ejemploConfig.png?raw=true)

4. Obtener las credenciales en formato json que se obtienen configurando el proyecto en la Consola de Desarrolladores de Google y pegarlas en el archivo credentials.json

Aclaracion: Los valores proporcionados para "API_KEY" y "AUTORIZACION" y las credenciales de google drive son meramente ejemplos ilustrativos y no tienen la funcionalidad real de acceso.

5. Una vez configurado todo el proyecto, ir a la carpeta fuente del mismo y correr en el bash el siguiente comando: python generatorVideo.py

