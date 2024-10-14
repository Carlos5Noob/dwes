numeros = [2, 3, 5, 1, 2, 3, 4, 9, 8, 6, 12, 43, 4]

print(sorted(numeros))
print(sorted(numeros, reverse=True))
numeros.reverse()
print(numeros)

print(numeros.pop())
numeros.insert(5, 2)
numeros.remove(3)
numeros.append(80)

print(numeros)