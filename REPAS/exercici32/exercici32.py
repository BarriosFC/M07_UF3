"""
Crear una funció que agafi una llista amb 10 números, 
i retorni una altra llista amb els seus quadrats.
"""

# funciona con decimales
def quadrats(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(float(i)*float(i))
    
    print(nueva_lista)