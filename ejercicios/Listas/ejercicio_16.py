invitados = ["Messi", "Cristiano", "Mbappe", "Vinicius"]

print(invitados[3], " no podrá asistir")

invitados.remove("Vinicius")
invitados.append("Neymar")

for i in range(len(invitados)):
    print("Bienvenido", invitados[i])