cantidad = int(input("Ingrese un número entre 10 y 100> "))
lista = []
valor = 0
while valor < cantidad:
    valor +=1
    lista.append(valor)

tupla = tuple(lista)

print(tupla)
