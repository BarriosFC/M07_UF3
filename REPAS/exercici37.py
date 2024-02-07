ftotal = input('Introdueix el preu de tot el carrito: ')

def amb_iva(ftotal, iva = 21):
    ftotal += ftotal * iva / 100  
    return ftotal 

print(amb_iva(int(ftotal)))

"""
L3. la función no está definida aún, el print debe ir bajo la función
L3. no hace falta pasar el iva como parámetro, porque la función tiene un default para eso
L3. el parámetro pasado es un str, debería ser un int
L6. el cálculo está mal
"""
