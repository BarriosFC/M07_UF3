valor = input("Introduzca un precio en Euros >")
iva = input("Entroduzca el IVA (sin %): 4, 10, 21 >")
valor_final = int(valor) * (int(iva)/100) + int(valor)
print(f"Valor: {valor}, IVA: {iva}, Valor con IVA agregado: {valor_final}")