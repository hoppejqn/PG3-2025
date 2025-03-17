class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")

# Crear dos objetos de la clase Persona
persona1 = Persona("Juan")
persona2 = Persona("Ana")

# Mostrar los nombres
persona1.mostrar_nombre()
persona2.mostrar_nombre()
