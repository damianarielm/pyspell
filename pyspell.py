#!/bin/python3

from lib.parse       import parse
from re              import sub
from lib.sugerencias import eliminar_caracteres,   \
                            insertar_espacios,     \
                            reemplazar_caracteres, \
                            insertar_caracteres,   \
                            intercambiar_adyacentes

argumentos = parse()

diccionario = {}
with open(argumentos.diccionario) as file:
    for palabra in file.read().splitlines():
        diccionario[palabra] = palabra

def sugerir(palabras):
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

    sugerencias = {p for p in posibilidades if p in diccionario}
    return posibilidades, sugerencias

def mostrar_sugerencias(sugerencias, sugeridas):
    if sugerencias:
        for palabra in sugerencias:
            if palabra not in sugeridas:
                print(f"{palabra}, ", end = "")
        print()

with open(argumentos.entrada) as file:
    for i, linea in enumerate(file.read().splitlines(), 1):
        for palabra in linea.split():
            palabra = sub("[^a-zA-ZÀ-ÖØ-öø-ÿ]+", "", palabra.lower())
            if palabra not in diccionario:
                print(f"\n{i}: La palabra '{palabra}' no esta en el diccionario.")
                if len(palabra) < argumentos.longitud:
                    posibilidades, sugeridas = sugerir({palabra})
                    mostrar_sugerencias(sugeridas, [])
                    if argumentos.busqueda_profunda:
                        _, sugerencias = sugerir(posibilidades)
                        print("Busqueda profunda:")
                        mostrar_sugerencias(sugerencias, sugeridas)
