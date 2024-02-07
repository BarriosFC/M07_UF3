"""
Crear una funció que llegeixi el JSON de l’exercici anterior  
i surti el resultat (en format json) per consola.
"""
# Si el fichero no existe, peta

import json

# dumps convierte un objeto python en string json
with open("books.json", "r") as fichero:
    jsonStr = json.load(fichero)
    print(json.dumps(jsonStr, indent=2))

