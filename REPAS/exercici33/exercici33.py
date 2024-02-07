"""
Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
Exemple llista compra: {100:10, 250:5, 1500:30, …}
on 100 és el preu i 20 el descompte a aplicar a aquests 100.
Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.
Exemple:
Producte 1: 
Producte 2: 
…

"""

def calcula(dictio,iva):
    for precio, descuento in dictio.items():
        pre_iva = precio-precio*descuento/100
        post_iva = pre_iva+pre_iva*iva/100

        print("Precio:",precio," Descuento:",descuento," IVA:", iva, " Precio final:",post_iva)
