import json

def generarArchivoDeljson(json):
    with open("resultado_json","w") as arch:
     arch.write(json.toJSON())


def generar_tiempo_video(cant_preguntas):
    resultado = str(cant_preguntas * 10) + ' s'
    return resultado

def encontrar_indice(lista, cadena):
    try:
        indice = lista.index(cadena)
        return indice
    except ValueError:
        # Si no se encuentra la cadena en la lista, se devuelve -1
        return -1
