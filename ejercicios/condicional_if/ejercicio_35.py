def par_o_impar(num):
    if num % 2 == 0:
        return True
    return False


num = int(input("Introduzca un número: "))

if par_o_impar(num):
    print("El número ", num, " es par.")
else:
    print("El número", num, " no es par.")