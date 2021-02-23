#!/bin/python3

from lib.parse import parse
from re import sub

argumentos = parse()
abecedario = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

diccionario = {}
with open(argumentos.diccionario) as file:
    for palabra in file.read().splitlines():
        diccionario[palabra] = palabra

def insertar_espacios(palabra):
    sugerencias = set()
    for i in range(1, len(palabra)):
        p1, p2 = palabra[:i], palabra[i:]
        if p1 in diccionario and p2 in diccionario:
            sugerencias.add(p1 + " " + p2)
    return sugerencias

def eliminar_caracteres(palabra):
    sugerencias = set()
    for i in range(len(palabra)):
        p = palabra[:i] + palabra[i+1:]
        if p in diccionario:
            sugerencias.add(p)
    return sugerencias

def reemplazar_caracteres(palabra):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            p = palabra[:i] + letra + palabra[i+1:]
            if p in diccionario:
                sugerencias.add(p)
    return sugerencias

def insertar_caracteres(palabra):
    sugerencias = set()
    for i in range(len(palabra)):
        for letra in abecedario:
            p = palabra[:i] + letra + palabra[i:]
            if p in diccionario:
                sugerencias.add(p)
    return sugerencias

def intercambiar_adyacentes(palabra):
    sugerencias = set()
    for i in range(len(palabra) - 1):
        p = palabra[:i] + palabra[i+1] + palabra[i] + palabra[i+2:]
        if p in diccionario:
            sugerencias.add(p)
    return sugerencias

def sugerir(palabra):
    print(f"{i}: La palabra '{palabra}' no esta en el diccionario.")
    sugerencias = set()
    sugerencias = sugerencias.union(eliminar_caracteres(palabra))
    sugerencias = sugerencias.union(insertar_espacios(palabra))
    sugerencias = sugerencias.union(reemplazar_caracteres(palabra))
    sugerencias = sugerencias.union(insertar_caracteres(palabra))
    sugerencias = sugerencias.union(intercambiar_adyacentes(palabra))

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
