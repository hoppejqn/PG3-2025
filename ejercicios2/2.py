# -*- coding: utf-8 -*-

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")

    def estado(self):
        if self.nota >= 6:
            print(f"{self.nombre} est� aprobado.")
        else:
            print(f"{self.nombre} est� regular.")

# Crear dos objetos de la clase Alumno
alumno1 = Alumno("Carlos", 8)
alumno2 = Alumno("Mar�a", 4)

# Imprimir los detalles de los alumnos
alumno1.imprimir()
alumno1.estado()
alumno2.imprimir()
alumno2.estado()
