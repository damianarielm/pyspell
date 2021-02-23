#!/bin/python3

from lib.parse       import parse
from re              import sub
from lib.sugerencias import sugerir

def mostrar_sugerencias(sugerencias, sugeridas):
    if sugerencias:
        for palabra in sugerencias:
            if palabra not in sugeridas:
                print(f"{palabra}, ", end = "")
        print()

argumentos = parse()

diccionario = {}
with open(argumentos.diccionario) as file:
    for palabra in file.read().splitlines():
        diccionario[palabra] = palabra

with open(argumentos.entrada) as file:
    for i, linea in enumerate(file.read().splitlines(), 1):
        for palabra in linea.split():
            palabra = sub("[^a-zA-ZÀ-ÖØ-öø-ÿ]+", "", palabra.lower())
            if palabra not in diccionario:
                print(f"\n{i}: La palabra '{palabra}' no esta en el diccionario.")
                if len(palabra) < argumentos.longitud:
                    posibilidades, sugeridas = sugerir({palabra}, argumentos, diccionario)
                    if sugeridas:
                        print("Quizas quizo decir: ", end = "")
                        mostrar_sugerencias(sugeridas, [])
                    if argumentos.busqueda_profunda:
                        _, sugerencias = sugerir(posibilidades, argumentos, diccionario)
                        if sugerencias:
                            print("Busqueda profunda:")
                            mostrar_sugerencias(sugerencias, sugeridas)
