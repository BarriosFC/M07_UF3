from exercici27 import suma

texto = input("Ingrese 2 números (separados por un espacio) que quiera sumar> ")
numeros = texto.split(' ')
print("Resultado:",suma(numeros[0],numeros[1]))