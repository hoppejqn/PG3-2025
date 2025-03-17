lista = ["banana","pedro","rama","s3"]

palabra = input("Ingrese la palabra a buscar > ")

for i in range(len(lista)):
    if palabra == lista[i]:
        print(f"La palabra {palabra} se encuentra en la posición {i} de la lista")
        break