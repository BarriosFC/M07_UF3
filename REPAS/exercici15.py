"""
El mateix que l’anterior exercici, 
però sense demanar un màxim de números. 
L’usuari indicarà quan ha acabat posant un 0.
"""

lista = []
while True:
    numero = int(input("Ingrese un número> "))
    if numero != 0:
        lista.append(numero)
    else:
        break

lista.sort()
tupla = tuple(lista)
print(tupla)