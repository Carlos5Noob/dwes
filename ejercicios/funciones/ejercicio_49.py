vinos_jerez = ["Fino Sherry", "Pedro Ximénez", "Sherry Cream", "Moscatel", "Oloroso"]

def analiza_vinos(vinos):
    """
    Función que analiza una lista de vinos y muestra los vinos que contengan en su nombre la palabra Sherry. Se le pasa por parámetro una lista de vinos.
    """
    resultado = {}
    resultado_lista = [];
    for vino in vinos:
        contiene_sherry = "sherry" in vino.lower()
        resultado[vino] = contiene_sherry
    for vino, contiene_sherry in resultado.items():
        if contiene_sherry:
            resultado_lista.append(vino)
    print(resultado)
    print(resultado_lista)

analiza_vinos(vinos_jerez)

