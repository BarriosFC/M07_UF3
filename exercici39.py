n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

"""
L3. el rango está mal definido. no es (j,1,-1) si no (i,0,-2)
el primer parámetro es a partir de qué número se empieza, o sea desde el valor actual de i
(para que tenga forma de triángulo). 
el segundo parámetro es el final del bucle (sin incluír ese número), lo cual debe ser 0 no 1
el último parámetro es el valor del step o "salto". debe ser -2, no -1 (sólo impares)
"""
