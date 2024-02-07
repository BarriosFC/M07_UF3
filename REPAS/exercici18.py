"""
Demanar a l’usuari posar 2 paraules. 
Afegir aquestes a una tupla i mostrar per pantalla 
quantes vegades apareix cada lletra.
"""
# Las añado como palabras, haciendo una tupla de 2 elementos?
# O las añado individualmente a 2 tuplas separadas para luego concatenarlas en 1 sola?
# Voy a hacer lo segundo :)

letras = "abcdefghijklmnopqrstuvwxyz"
cantidades = []
for i in letras:
    cantidades.append(0)
    

texto = input("Ingresa 2 palabras> ")
array = texto.split(' ')
tupla1 = tuple(array[0])
tupla2 = tuple(array[1])
tuplaFinal = tupla1 + tupla2
print(tuplaFinal)


for element in array:
    for i in element:
        cantidades[letras.find(i)] += 1
        
        
for letra in letras:
    if cantidades[letras.find(letra)] > 0:
        print("Cantidad de "+letra+"'s: "+str(cantidades[letras.find(letra)]))
