import random

secreto = random.randint(1,100)

intentos = 0

while (True):
    numero = int(input("Ingrese un número> "))
    intentos += 1
    if numero == secreto:
        print("Has adivinado el número",numero,"en",intentos,"intentos!")
        break
    elif numero > secreto:
        print("El número secreto es menor que",numero)
    else:
        print("El número secreto es mayor que",numero)