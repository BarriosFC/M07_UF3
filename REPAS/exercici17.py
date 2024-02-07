"""
Igual que l’anterior però a la tupla afegir la frase sense 
els caràcters repetits i mostrar el contingut de la tupla. 
Exemple: Usuari indica la paula caracteristica. 
Es mostra per pantalla carteis.
"""

frase = input("Ingrese una frase o palabra> ")
array = frase.split(' ')
temp = ""
temp_array = []

for palabra in array:
    temp += palabra

for i in temp:
    if i not in temp_array:
        temp_array.append(i)
tupla = tuple(temp_array)
print(tupla)