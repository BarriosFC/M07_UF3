"""
Crear una funció que rebi, per paràmetres, una funció i una llista. 
Ha de crear una llista nova amb el nou contingut i mostrar-la per pantalla.
Passes:
Crear una funció que calculi el quadrat d’un número passat per paràmetre.
Crear una segona funció que agafi cada número de la llista 
(passat per paràmetre) i truqui a la funció anterior i guardar el resultat a una llista.
"""

def cuadrado(num):
    return num*num

def cuadrado_lista(lista, custom_function = cuadrado):
    new_lista = []
    for i in lista:
        new_lista.append(custom_function(i))
    
    print(new_lista)