vinos_jerez = ["Fino Sherry", "Pedro Ximénez", "Sherry Cream", "Moscatel", "Oloroso"]

def analiza_vinos(vinos):
    """
    Función que analiza una lista de nombres de vinos y devuelva cuántos de esos nombres contienen la palabra "Sherry". La función debe aceptar una lista de nombres de vinos y retornar un diccionario donde las claves sean los nombres de los vinos y los valores sean True si contienen la palabra "Sherry", o False si no la contienen.
    :param vinos: Una lista de nombres de vinos que queremos analizar.
    :return:
        - Dict: Un diccionario con los nombres de los vinos (key) y su estado (True si contiene sherry en su nombre, False si no).
        - List: Una lista de nombres de vinos que contienen la palabra sherry en su nombre.
    """
    resultado = {}
    resultado_lista = []
    for vino in vinos:
        contiene_sherry = "sherry" in vino.lower()
        resultado[vino] = contiene_sherry
    for vino, contiene_sherry in resultado.items():
        if contiene_sherry:
            resultado_lista.append(vino)
    print(resultado)
    print(resultado_lista)

analiza_vinos(vinos_jerez)