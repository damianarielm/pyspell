#!/bin/python3

from re              import sub
from lib.parse       import parse
from lib.sugerencias import generar_posibilidades, generar_sugerencias

def generar_diccionario(archivo):
    with open(archivo) as file:
        return { palabra for palabra in file.read().splitlines() }

def palabra_no_encontrada(palabra, argumentos, diccionario):
    ps = generar_posibilidades({palabra}, argumentos)
    ss = generar_sugerencias(ps, diccionario, argumentos.maximo)
    while len(ss) < argumentos.minimo:
        ps = generar_posibilidades(ps, argumentos)
        ss |= generar_sugerencias(ps, diccionario, argumentos.maximo - len(ss))
    mostrar_sugerencias(list(ss)[:argumentos.maximo])

def mostrar_sugerencias(sugerencias):
    if sugerencias:
        print("Quizas quizo decir: ", end = "")
        for i, palabra in enumerate(sugerencias):
            print(f"{palabra}, ", end = "")
        print("\n")
    else:
        print("No se encontraron sugerencias.\n")

def main():
    argumentos  = parse()
    diccionario = generar_diccionario(argumentos.diccionario)

    with open(argumentos.entrada) as file:
        for i, linea in enumerate(file.read().splitlines(), 1):
            for palabra in linea.split():
                p = sub("[^a-zá-úü]+", "", palabra.lower())
                if p not in diccionario:
                    print(f"{i}: La palabra '{palabra}'"
                           " no está en el diccionario.")
                    if len(p) < argumentos.longitud:
                        palabra_no_encontrada(p, argumentos, diccionario)
                    else:
                        print(f"Palabra demasiado larga.\n")

if __name__ == "__main__":
    main()
