texto = input("Ingrese entre 1 y 3 palabras> ")
array = texto.split(' ')

for palabra in array:
    print("La palabra ",palabra," tiene " , len(palabra), "caracteres. El 1ro es: ",
          palabra[0]," y el último es: ", palabra[-1])