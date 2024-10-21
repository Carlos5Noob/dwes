hotel = {}


def menu():

    while True:
        print("\nIntroduzca una opción: ")
        print("1. Agregar reserva. ")
        print("2. Cancelar reserva. ")
        print("3. Calcular costo total de una reserva. ")
        print("4. Mostrar el resumen de todas las reservas.  ")
        print("5. Salir ")

        try:
            opcion = int(input("Elija una opción: "))

            match opcion:
                case 1:
                    agregar_reserva()
                case 2:
                    cancelar_reserva()
                case 3:
                    calcular_costo_total()
                case 4:
                    mostrar_resumen()
                case 5:
                    print("Has salido del programa. ")
                    return
                case _:
                    print("Opción inválida")
        except ValueError as e:
            print(f"No has elegido una opción válida. {e}")


def agregar_reserva():

    try:
        nombre_cliente = input(
            "Has elegido agregar una nueva reserva. Por favor, introduzca el nombre del cliente: "
        )
        numero_noches = int(input("Introduzca el número de noches: "))
        tipo_habitacion = input("Introduzca el tipo de habitación: ")
    except ValueError as e:
        print(f"No has elegido una nueva reserva. {e}")
    else:
        hotel[nombre_cliente] = {
            "Numero_noches": numero_noches,
            "Tipo_habitacion": tipo_habitacion,
        }
        print("Reserva completada correctamente. ")


def cancelar_reserva():
    nombre_cliente = input(
        "Has elegido la opción de cancelar una reserva. Introduzca el nombre del cliente que desees cancelar. "
    )
    if nombre_cliente in hotel:
        del hotel[nombre_cliente]
        print(f"La reserva de {nombre_cliente} ha sido cancelada. ")
    else:
        print(f"No existe ninguna reserva de {nombre_cliente}")


def calcular_costo_total():
    cliente = input(
        "Has elegido calcular el costo total de una reserva. Introduzca el nombre del cliente que quieras revisar: "
    )
    if cliente in hotel:
        numero_noches = hotel[cliente]["Numero_noches"]
        costo_por_noche = 10 if numero_noches > 5 else 5

        costo_total = costo_por_noche * numero_noches
        print(f"El costo total para el cliente {cliente} es de {costo_total} euros")
    else:
        print(f"No se ha encontrado ninguna reserva para {cliente}")


def mostrar_resumen():
    print(
        "Has elegido la opción de mostrar el resumen de todas las reservas del hotel. "
    )
    print(
        "-----------------------------------------------------------------------------"
    )
    for cliente, datos in hotel.items():
        num_noches = datos["Numero_noches"]
        tipo_hab = datos["Tipo_habitacion"]
        print(f"{cliente}: {num_noches} noches, Tipo de habitación: {tipo_hab}")


menu()
