"""
Crear una funció per calcular el total d’una factura amb l’IVA. 
La funció ha de rebre (per paràmetre) la quantitat sense IVA 
i l’IVA a aplicar (introduïts per l’usuari). 
En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%) 
s’aplicarà directament el 21%. 
Es mostra per pantalla el valor sense IVA, l’IVA i el total.
"""

def iva(num1, num2):
    try:
        porcentaje = int(num2)
    except:
        porcentaje = 21
    
    valor_final = int(num1) + (int(num1)*porcentaje/100)
    print("Precio:",num1," IVA:",porcentaje," Precio con IVA:",valor_final)