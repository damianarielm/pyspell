#!/bin/python3

from lib.parse       import parse
from re              import sub
from lib.sugerencias import generar_posibilidades, generar_sugerencias

def mostrar_sugerencias(sugerencias, sugeridas):
    if sugerencias:
        for palabra in {p for p in sugerencias if p not in sugeridas}:
            print(f"{palabra}, ", end = "")
        print("")

def palabra_no_encontrada(palabra):
    posibilidades = generar_posibilidades({palabra}, argumentos)
    sugeridas = generar_sugerencias(posibilidades, diccionario, argumentos)
    mostrar_sugerencias(sugeridas, {})
    if argumentos.busqueda_profunda:
        posibilidades = generar_posibilidades(posibilidades, argumentos)
        sugerencias = generar_sugerencias(posibilidades, diccionario, argumentos)
        mostrar_sugerencias(sugerencias, sugeridas)

def generar_diccionario(archivo):
    with open(archivo) as file:
        return {palabra for palabra in file.read().splitlines()}

argumentos  = parse()
diccionario = generar_diccionario(argumentos.diccionario)
with open(argumentos.entrada) as file:
    for i, linea in enumerate(file.read().splitlines(), 1):
        for palabra in linea.split():
            palabra = sub("[^a-zá-úü]+", "", palabra.lower())
            if palabra not in diccionario:
                print(f"{i}: La palabra '{palabra}'"
                       " no esta en el diccionario.")
                if len(palabra) < argumentos.longitud:
                    palabra_no_encontrada(palabra)
                else:
                    print(f"Palabra demasiado larga.")
