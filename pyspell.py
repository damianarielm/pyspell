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

def sugerir(palabra):
    print(f"{i}: La palabra '{palabra}' no esta en el diccionario.", end = "")
    sugerencias  = set()
    if argumentos.eliminar_caracteres:
        sugerencias |= eliminar_caracteres(palabra, diccionario)
    if argumentos.insertar_espacios:
        sugerencias |= insertar_espacios(palabra, diccionario)
    if argumentos.reemplazar_caracteres:
        sugerencias |= reemplazar_caracteres(palabra, diccionario)
    if argumentos.insertar_caracteres:
        sugerencias |= insertar_caracteres(palabra, diccionario)
    if argumentos.intercambiar_adyacentes:
        sugerencias |= intercambiar_adyacentes(palabra, diccionario)

    sugerencias = {x for x in sugerencias if x in diccionario}
    if sugerencias:
        print(f" Quizas quizo decir: ")
        for palabra in sugerencias:
            print(f"{palabra}, ", end = "")

with open(argumentos.entrada) as file:
    for i, linea in enumerate(file.read().splitlines(), 1):
        for palabra in linea.split():
            palabra = sub("[^a-zA-ZÀ-ÖØ-öø-ÿ]+", "", palabra.lower())
            if palabra not in diccionario:
                sugerir(palabra)
                print("\n")
