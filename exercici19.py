"""
Cal buscar la informació que es demana de la següent list:
areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, 
“Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)

Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
Imprimir el total de l’àrea del pis.

"""

areas_pis = [ "Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, 
             "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("1.",areas_pis[1])
print("2.",areas_pis[-1])
print("3.",areas_pis[areas_pis.index("Terrassa")+1])
print("4.",areas_pis[:3])
print("5.",areas_pis[2:])
print("6.",areas_pis[areas_pis.index("Habitació1")+1] + areas_pis[areas_pis.index("Habitació2")+1])
areas_pis[areas_pis.index("Lavabo")+1] = 9.05
print("7.",areas_pis)
areas_pis.extend(["Pati interior", 2.78])
print("8.",areas_pis)

areaFinal = 0
cantidad = 0
contador = 0
while contador < len(areas_pis):
    if contador % 2 == 1:
        areaFinal += areas_pis[contador]
        cantidad += 1
    contador += 1

print("9.",areaFinal/cantidad)