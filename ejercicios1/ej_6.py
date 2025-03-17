'''
6) A CONTAR VOCALES!
Escribir una función que reciba como parámetro una frase y devuelva la cantidad de vocales que ésta tiene.
'''

def contar_vocales(frase):
    vocales = "aeiou"
    return len([letra for letra in frase.lower() if letra in vocales])

frase = input("Ingrese una frase > ")

print(f"La frase tiene {contar_vocales(frase)} vocales")