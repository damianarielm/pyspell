#!/bin/python3

from lib.parse import parse
from re import sub
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
    print(f"{i}: La palabra '{palabra}' no esta en el diccionario.")
    sugerencias = set()
    sugerencias = sugerencias.union(eliminar_caracteres(palabra, diccionario))
    sugerencias = sugerencias.union(insertar_espacios(palabra, diccionario))
    sugerencias = sugerencias.union(reemplazar_caracteres(palabra, diccionario))
    sugerencias = sugerencias.union(insertar_caracteres(palabra, diccionario))
    sugerencias = sugerencias.union(intercambiar_adyacentes(palabra, diccionario))

    if sugerencias:
        print(f"Quizas quizo decir: ", end = "")
        for palabra in sugerencias:
            print(f"{palabra}, ", end = "")
        print("")

with open(argumentos.entrada) as file:
    for i, linea in enumerate(file.read().splitlines(), 1):
        for palabra in linea.split():
            palabra = sub("[^a-zA-ZÀ-ÖØ-öø-ÿ]+", "", palabra.lower())
            if palabra not in diccionario:
                sugerir(palabra)
                print("")
