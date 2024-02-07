"""
Demanar a l’usuari que posi 10 números separats per espais. 
Afegir aquests números a una llista. 
Calcular la suma de tots els números i la seva mitjana 
i afegir aquests 2 números a la llista. 
Mostrar per pantalla la llista.

Exemple mostra per pantalla.
Números de l’usuari:
suma total:
mitjana:

"""

texto = input("Ingresa 10 números separados por espacios> ")
text_array = texto.split(' ')
numeros = []
suma = 0

for element in text_array:
    numeros.append(float(element))
    suma += float(element)

print("Números de l’usuari:",texto)
print("Suma total:",suma)
print("Mitjana:",suma/len(numeros))