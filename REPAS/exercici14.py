"""
Demanar a l’usuari que introdueixi 10 números separats per un espai. 
Al acabar, el programa els introduirà en una tupla i els ordenarà 
(major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.
"""

numStr = input("Ingrese 10 numeros separados por un espacio> ")
lista = numStr.split(' ')
iterator = 0
for i in lista:
    lista[iterator] = int(i)
    iterator += 1

lista.sort()
tupla = tuple(lista)

print(tupla)