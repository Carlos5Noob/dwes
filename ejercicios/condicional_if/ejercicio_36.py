nota = int(input("Escriba su nota(0 - 10): "))

if nota >= 0 and nota <= 4:
    print("Suspenso")
elif nota >= 5 and nota <= 6:
    print("Aprobado")
elif nota >= 7 and nota <= 8:
    print("Notable")
else:
    print("Sobresaliente")
