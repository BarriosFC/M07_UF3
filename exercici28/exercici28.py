"""
Crear una funció que passats dos números per paràmetre 
(demanats a l’usuari) ens mostri per pantalla un número 
aleatori entre aquests dos números.
"""
import random

def aleatori(num1, num2):
    valor = random.randint(0, 1)
    return num1 if valor == 0 else num2