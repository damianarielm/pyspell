abecedario = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

def insertar_espacios(palabra, diccionario):
    sugerencias = set()
    for i in range(1, len(palabra)):
        p1, p2 = palabra[:i], palabra[i:]
        if p1 in diccionario and p2 in diccionario:
            sugerencias.add(p1 + " " + p2)
    return sugerencias

def eliminar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        p = palabra[:i] + palabra[i+1:]
        if p in diccionario:
            sugerencias.add(p)
    return sugerencias

def reemplazar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            p = palabra[:i] + letra + palabra[i+1:]
            if p in diccionario:
                sugerencias.add(p)
    return sugerencias

def insertar_caracteres(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            p = palabra[:i] + letra + palabra[i:]
            if p in diccionario:
                sugerencias.add(p)
    return sugerencias

def intercambiar_adyacentes(palabra, diccionario):
    sugerencias = set()
    for i in range(len(palabra) - 1):
        p = palabra[:i] + palabra[i+1] + palabra[i] + palabra[i+2:]
        if p in diccionario:
            sugerencias.add(p)
    return sugerencias
