"""
Crear una funció que mostri, per consola, i guardi 
en un arxiu extern, un JSON amb una key de nom book 
que contindrà titel, cover, year i pages. 
Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 
"""

# Enunciado mal formulado. 
# Voy a hacer un json con 4 libros, cada uno tendrá titulo...paginas
# Pero cada uno tendra una key unica, no se pueden repetir las keys en json

import json

books = {}

for i in range(1, 5):
    books["book"+str(i)] = { "title": f"Titulo{i}", "cover": f"Portada{i}",
                "year": f"Anyo{i}", "pages": f"Paginas{i}" }
            

# dump escribe en el json. si el fichero no existe, lo crea
with open("books.json", "w") as fichero:
    json.dump(books, fichero, indent=2)
    
