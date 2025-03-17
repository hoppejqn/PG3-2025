# -*- coding: utf-8 -*-

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"Lado mayor: {mayor}")

    def verificar_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El tri�ngulo es equil�tero.")
        else:
            print("El tri�ngulo no es equil�tero.")

# Crear un objeto de la clase Triangulo
triangulo = Triangulo(5, 5, 8)

# Imprimir el lado mayor y verificar si es equil�tero
triangulo.imprimir_lado_mayor()
triangulo.verificar_equilatero()
