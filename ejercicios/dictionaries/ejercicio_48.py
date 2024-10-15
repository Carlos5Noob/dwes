alumnos = {"Messi": [20, ["Matemáticas", "Biología"]], "Xokas": [33, ["Lengua", "Biología"]], "Antony": [69, ["Matemáticas", "Ciencias"]],}

alumnos["Cristiano"] = [39, ["Deportes, Lengua"]]

alumnos["Messi"] = [20, ["Lengua, Deportes"]]

print(alumnos.get("Xokas"))

alumnos.pop("Xokas")

print("Messi" in alumnos.keys())

print(alumnos.values())

for i in alumnos:
    print(i, ": ", alumnos[i])