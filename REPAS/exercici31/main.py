from exercici31 import iva

precio = input("Ingrese un precio y su IVA correspondiente (separados por espacio. Iva sin %)> ")
valores = precio.split(' ')
iva(valores[0],valores[1])