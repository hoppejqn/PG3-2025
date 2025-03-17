'''4) ORDEN POR FAVOR!
Realizar una función, que reciba como parámetro una lista compuesta por números enteros y que nos
devuelva otra lista con el mismo contenido pero ordenada de mayor a menor.'''

lista = [1, 5, 3, 2, 4, 6, 7, 8, 9, 10]

def ordenar_lista(lista):
    lista.sort(reverse=True)
    return lista

print(ordenar_lista(lista))