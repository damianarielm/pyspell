from argparse import ArgumentParser

def parse():
    parser = ArgumentParser()

    parser.add_argument("entrada", type = str,
                        help = "Archivo de entrada.")
    parser.add_argument("diccionario", type = str,
                         help = "Archivo de diccionario.")
    parser.add_argument("-longitud", type = int, default = 15,
                        help = "Longitud maxima de palabras.")
    parser.add_argument("-maximo", type = int, default = 5,
                        help = "Cantidad maxima de sugerencias")
    parser.add_argument("-minimo", type = int, default = 0,
                        help = "Cantidad minima de sugerencias")
    parser.add_argument("-intercambiar_adyacentes", action = "store_false",
                        help = "Deshabilita intercambiar adyacentes.")
    parser.add_argument("-insertar_espacios", action = "store_false",
                        help = "Deshabilita insertar espacios.")
    parser.add_argument("-eliminar_caracteres", action = "store_false",
                        help = "Deshabilita eliminar caracteres.")
    parser.add_argument("-reemplazar_caracteres", action = "store_false",
                        help = "Deshabilita reemplazar caracteres.")
    parser.add_argument("-insertar_caracteres", action = "store_false",
                        help = "Deshabilita insertar caracteres.")

    return parser.parse_args()
