"""
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. 
S’haura de demanar a l’usuari que posi contactes (noms i edats). 
Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.
"""

# Entiendo que pondrán un solo nombre y que la edad será realmente un número
# Si se ingresa "stop" se dejan de añadir 

dictio = {}
while True:
    datos = input("Ingrese un nombre y edad. Escriba 'stop' para finalizar> ")
    if datos == 'stop':
        break
    else:
        array = datos.split(' ')
        dictio[array[0]] = array[1]
    
print(dictio)