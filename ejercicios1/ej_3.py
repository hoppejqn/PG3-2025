'''3) PINTAMEEEEEE
Escriba un programa que pida ancho y alto de un rectángulo y el caracter a utilizar en el dibujo.
Ejemplo:
Pedido:
Ancho: 5
Alto: 4
Caracter: 'A'
Imprime:
A A A A A
A A A A A
A A A A A
A A A A A'''

ancho = int(input("Ingrese el ancho del rectángulo > "))
alto = int(input("Ingrese el alto del rectángulo > "))
caracter = input("Ingrese el caracter a utilizar en el dibujo > ") 

for i in range(alto):
    print(caracter * ancho)