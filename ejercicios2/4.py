# -*- coding: utf-8 -*-

class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        print(f"La suma es: {self.num1 + self.num2}")

    def restar(self):
        print(f"La resta es: {self.num1 - self.num2}")

    def multiplicar(self):
        print(f"La multiplicaci�n es: {self.num1 * self.num2}")

    def dividir(self):
        if self.num2 != 0:
            print(f"La divisi�n es: {self.num1 / self.num2}")
        else:
            print("No se puede dividir por cero.")

# Crear un objeto de la clase Operaciones
operacion = Operaciones(10, 5)
