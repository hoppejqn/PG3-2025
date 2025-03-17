'''5) PALINDROMOS
Escribir una función que reciba como parámetro una palabra, y devuelva True si esa palabra es un
palíndromo y False si no lo es.
Ejemplo:
esCapicua("neuquen") === True
esCapicua("jovenes") === False'''

def es_palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra > ")

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")