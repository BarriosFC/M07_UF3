meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre")

numero = int(input("Ingrese un número del 1 al 12> "))
if numero != 0:
    print(meses[numero-1])