abecedario = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

def insertar_espacios(palabra, diccionario):
    sugerencias = set()
    for i in range(1, len(palabra)):
        sugerencias.add(palabra[:i] + " " + palabra[i:])
    return sugerencias

def eliminar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        sugerencias.add(palabra[:i] + palabra[i + 1:])
    return sugerencias

def reemplazar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            sugerencias.add(palabra[:i] + letra + palabra[i + 1:])
    return sugerencias

def insertar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            sugerencias.add(palabra[:i] + letra + palabra[i:])
    return sugerencias

def intercambiar_adyacentes(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra) - 1):
        sugerencias.add(palabra[:i] + palabra[i+1] + palabra[i] + palabra[i+2:])
    return sugerencias
