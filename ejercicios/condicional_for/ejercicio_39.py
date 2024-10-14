cadena = input("Escribe una cadena: ")

cont = 0

for caracter in cadena:
    if caracter in "aeiouAEIOU":
        cont = cont + 1

print("La cadena '", cadena, "' tiene ", cont, " vocales. ")
