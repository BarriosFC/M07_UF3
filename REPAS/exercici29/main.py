from exercici29 import intervalo

texto = input("Ingrese 2 números (separados por un espacio) y mostraremos los intermedios> ")
numeros = texto.split(' ')
print("Intervalo:",intervalo(numeros[0],numeros[1]))