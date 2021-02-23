from argparse import ArgumentParser

def parse():
    parser = ArgumentParser()

    parser.add_argument("entrada", type = str,
                        help = "Archivo de entrada.")
    parser.add_argument("diccionario", type = str,
                         help = "Archivo de diccionario.")

    return parser.parse_args()
