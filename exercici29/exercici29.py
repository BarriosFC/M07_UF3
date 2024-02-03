"""
Crear una funció que passats dos números per paràmetre 
(demanats a l’usuari) ens mostra per pantalla tots els números (enters) 
que hi ha entre ells. 
També mostrarà per pantalla la suma d’aquests números enters.
"""

def intervalo(num1,num2):
    if num1 < num2:
        primero = int(num1)
        segundo = int(num2)
    else:
        primero = int(num2)
        segundo = int(num1)
    
    lista = []

    for i in range(primero+1,segundo):
        lista.append(i)
    
    return lista