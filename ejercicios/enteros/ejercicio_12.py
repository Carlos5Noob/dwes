# esta función simpplemente hace una operación de suma, resta, multiplicación y división; y las muestra por pantalla
def operaciones() :
    sum = 5 + 3
    rest = 20 - 12
    mult = 4 * 2
    div = 16 / 2

    print(sum, rest, mult, div)


# esta función elimina el sufijo de un archivo que se le pasa por parámetro
def eliminar_sufijo():
    archivo = "holamundo.txt"

    archivo = archivo.removesuffix(".txt")

    print(archivo)



