suma = 0

for i in range(1, 101, 1):
    if i % 2 != 0:
        continue
    suma += i

print(suma)
