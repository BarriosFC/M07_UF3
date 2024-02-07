"""
Crear una funció que rebi una frase per paràmetre. 
Aquesta frase es demana a l’usuari. 
Ha de retornar un diccionari amb les paraules que conte 
i la longitud de cada paraula.
"""

def dictio(frase):
    palabras = frase.split(' ')
    diccionario = {}
    for i in palabras:
        diccionario[i] = len(i)

    return diccionario