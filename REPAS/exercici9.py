texto = input("Ingresa 2 palabras y verás la magia> ")

array = texto.split(' ')
primera = array[0]
segunda = array[1]
print(segunda[0:2]+primera[2:],"y",primera[0:2]+segunda[2:])