class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self.__nombre = valor
        else: 
            raise ValueError("El nombre debe de ser una cadena de caracteres.")
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        if isinstance(valor, int):
            self.__salario = valor
        else: 
            raise ValueError("El salario debe de ser un número entero.")
        

    def detalles(self):
        return f"Nombre empleado: {self.__nombre}. Salario: {self.__salario}$"

    def __del__(self):
        print(f"Empleado {self.nombre} destruido.")

    @classmethod
    def descuento_sueldo(cls, salario):
        descuento_aplicado = ((salario*10)/100) 
        return salario - descuento_aplicado
    
    @staticmethod
    def impuesto(salario):
        return ((salario*21)/100)


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.__departamento = departamento

    def detalles(self):
        return f"Nombre empleado: {self.nombre}. Salario: {self.salario}$. Departamento: {self.__departamento}"



def main():
    gerente1 = Gerente("Lucio", 1200, 12)
    gerente2 = Gerente("Messi", 1450, 8)

    gerente2.salario = 2000

    print(gerente1.detalles())
    print(gerente2.detalles())
    print(Empleado.descuento_sueldo(100))
    print(Empleado.impuesto(75))

if __name__ == "__main__":
    main()
    