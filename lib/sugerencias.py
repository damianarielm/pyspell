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

def sugerir(palabras, argumentos, diccionario):
    posibilidades = set()
    for palabra in palabras:
        if argumentos.eliminar_caracteres:
            posibilidades |= eliminar_caracteres(palabra, diccionario)
        if argumentos.insertar_espacios:
            posibilidades |= insertar_espacios(palabra, diccionario)
        if argumentos.reemplazar_caracteres:
            posibilidades |= reemplazar_caracteres(palabra, diccionario)
        if argumentos.insertar_caracteres:
            posibilidades |= insertar_caracteres(palabra, diccionario)
        if argumentos.intercambiar_adyacentes:
            posibilidades |= intercambiar_adyacentes(palabra, diccionario)

    sugerencias = set()
    for p in posibilidades:
        if p in diccionario:
            sugerencias |= {p}
        if len(p.split()) == 2:
            p1, p2 = p.split()
            if p1 in diccionario and p2 in diccionario:
                sugerencias |= {p}
    return posibilidades, sugerencias
