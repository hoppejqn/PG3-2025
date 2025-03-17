# -*- coding: utf-8 -*-

class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.padre}, Madre: {self.madre}, Hijos: {hijos_str}"

# Crear un objeto de la clase Familia
familia = Familia("Jos�", "Ana", ["Luis", "Carlos", "Sof�a"])

# Imprimir la representaci�n de la familia
print(familia)
