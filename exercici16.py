"""
Demanar a l’usuari una frase. 
El programa eliminarà els espais i s'afegirà a una tupla. 
Mostrar per pantalla el contingut de la tupla.
"""

frase = input("Ingrese una frase> ")
array = frase.split(' ')
tupla = tuple(array)

print(tupla)
