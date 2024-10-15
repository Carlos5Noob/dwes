inventario = {
    "Laptop": {
        "precio": 1200,
        "cantidad": 10,
        "reseñas": [5, 4, 4, 5]
    },
    "Smartphone": {
        "precio": 800,
        "cantidad": 25,
        "reseñas": [4, 5, 3, 4]
    },
    "Auriculares": {
        "precio": 150,
        "cantidad": 50,
        "reseñas": [4, 5, 5, 4]
    }
}

# 1. Agregar un nuevo producto al inventario
nuevo_producto = {
    "precio": 600,
    "cantidad": 15,
    "reseñas": [5, 4, 5]
}
inventario["Tablet"] = nuevo_producto  # Agregamos un producto nuevo

# 2. Actualizar el precio y la cantidad de un producto
inventario["Smartphone"]["precio"] = 750  # Actualizamos el precio del Smartphone
inventario["Smartphone"]["cantidad"] = 30  # Actualizamos la cantidad del Smartphone

# 3. Consultar la información de un producto específico
producto = "Laptop"
if producto in inventario:
    print(f"Información del {producto}: {inventario[producto]}")

# 4. Eliminar un producto del inventario
producto_a_eliminar = "Auriculares"
if producto_a_eliminar in inventario:
    del inventario[producto_a_eliminar]
    print(f"Producto '{producto_a_eliminar}' eliminado.")

# 5. Comprobar si un producto está en el inventario
producto_a_buscar = "Tablet"
if producto_a_buscar in inventario:
    print(f"El producto '{producto_a_buscar}' está en el inventario.")
else:
    print(f"El producto '{producto_a_buscar}' no está en el inventario.")

# 6. Obtener todas las claves (nombres de los productos)
nombres_productos = inventario.keys()
print("Productos en el inventario:", list(nombres_productos))

# 7. Obtener todos los valores (información de los productos)
valores_productos = inventario.values()
print("Información de los productos:", list(valores_productos))

# 8. Recorrer el inventario y mostrar la información de cada producto
print("\nInventario completo:")
for producto, info in inventario.items():
    print(f"Producto: {producto}")
    print(f"  Precio: ${info['precio']}")
    print(f"  Cantidad: {info['cantidad']} unidades")
    print(f"  Reseñas: {info['reseñas']}\n")
