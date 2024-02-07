"""
Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla 
la seva taula de multiplicar fins el 10. 
Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
"""

numero = int(input("Ingrese un número del 1 al 10> "))
multi = [1,2,3,4,5,6,7,8,9,10]
resultado = ""

for i in multi:
    if i == 10:
        resultado += " i " + str(numero*i)
    else:
        resultado += str(numero*i)+", "

print(resultado)