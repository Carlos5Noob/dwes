invitados = ["Sonaldo", "Messi", "Dembele", "Cristiano", "Mbappe", "Neymar", "Vallejo"]

print("Finalmente solo podré invitar a 2 para cenar chicos...")

for i in range(len(invitados)-2):
    print("Lo siento, ", invitados.pop())

for i in range(len(invitados)):
    print(invitados[i], "sigues invitado")

del invitados[0:len(invitados)]

print(invitados)