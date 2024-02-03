"""
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
La funció ha de crear l’XML, crear les etiquetes i inserir text segons 
les següents especificacions:

a. Un root de nom students.
b. Cinc childs (del root) amb nom student.
c. Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
d. Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
e. El text de cada etiqueta serà de la vostra elecció.

"""
# Aunque del 22 al 24 diga "crea una función", dado que la parte de funciones va 
# más adelante, haré los ejercicios SIN funciones. 
# El resultado de ejecución será el mismo, que es lo importante
import xml.etree.ElementTree as ET

chamacos = ET.Element('students')
contador = 1
while contador < 6:
    student = ET.SubElement(chamacos, 'student')
    
    name = ET.SubElement(student, 'name')
    name.set("type","text")
    name.text = "Nombre del chango"

    surname = ET.SubElement(student, 'surname')
    surname.set("type","text")
    surname.text = "Apellido del chango"

    email = ET.SubElement(student, 'email')
    email.set("type","email")
    email.text = "email@email.com"

    dni = ET.SubElement(student, 'dni')
    dni.set("type","number")
    dni.text = str(contador)

    contador += 1


ET.indent(chamacos)
tree = ET.ElementTree(chamacos)
tree.write('students.xml')
ET.dump(chamacos)