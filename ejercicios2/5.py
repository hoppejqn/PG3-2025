# -*- coding: utf-8 -*-

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def verificar_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos.")
        else:
            print(f"{self.nombre} no debe pagar impuestos.")

# Crear un objeto de la clase Persona
persona = Persona("Pedro", 30)
persona.imprimir_datos()

# Crear un objeto de la clase Empleado
empleado = Empleado("Laura", 28, 3500)
empleado.imprimir_datos()
empleado.verificar_impuestos()
