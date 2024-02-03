from exercici28 import aleatori

texto = input("Ingrese 2 números (separados por un espacio) y mostraremos uno random> ")
numeros = texto.split(' ')
print("Resultado:",aleatori(numeros[0],numeros[1]))