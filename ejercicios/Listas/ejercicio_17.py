invitados = ["Messi", "Cristiano", "Mbappe", "Neymar"]

print("He encontrado una mesa de comedor más grande, así que habrá más invitados.")

invitados.insert(0, "Sonaldo")
invitados.insert(2, "Dembele")
invitados.append("Vallejo")

for i in range(len(invitados)):
    print("Hola", invitados[i])