letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

def insertar_espacios(p):
    return { p[:i] + " " + p[i:] for i in range(len(p)) }

def eliminar_caracteres(p):
    return { p[:i] + p[i + 1:] for i in range(len(p)) }

def reemplazar_caracteres(p):
    return { p[:i] + l + p[i + 1:] for i in range(len(p)) for l in letras }

def insertar_caracteres(p):
    return { p[:i] + l + p[i:] for i in range(len(p)) for l in letras }

def intercambiar_adyacentes(p):
    return { p[:i] + p[i+1] + p[i] + p[i+2:] for i in range(len(p) - 1) }

def generar_posibilidades(palabras, argumentos):
    posibilidades = set()
    for p in palabras:
        if argumentos.eliminar_caracteres:
            posibilidades |= eliminar_caracteres(p)
        if argumentos.insertar_espacios:
            posibilidades |= insertar_espacios(p)
        if argumentos.reemplazar_caracteres:
            posibilidades |= reemplazar_caracteres(p)
        if argumentos.insertar_caracteres:
            posibilidades |= insertar_caracteres(p)
        if argumentos.intercambiar_adyacentes:
            posibilidades |= intercambiar_adyacentes(p)
    return posibilidades

def generar_sugerencias(posibilidades, diccionario, maximo):
    sugerencias = set()
    for p in posibilidades:
        if p in diccionario:
            sugerencias |= { p }
        if len(p.split()) == 2:
            p1, p2 = p.split()
            if p1 in diccionario and p2 in diccionario:
                sugerencias |= { p }
        if len(sugerencias) >= maximo:
            return sugerencias
    return sugerencias
