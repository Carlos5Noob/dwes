temperaturas_celsius = [0, 10, 20, 30, 40]

temperaturas_fahrenheit = list(map(lambda x: ((9/5) * x)+32, temperaturas_celsius))

print(temperaturas_fahrenheit)

