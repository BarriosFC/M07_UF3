"""
Crear un arxiu de nom user.py. 
En aquest arxiu s’ha de crear una class de nom user. 
Aquesta class ha de tindre:

Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

"""

class user:
    def __init__(self, nombre, apellido, dni, edad, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getApellido(self):
        return self.apellido
    def setApellido(self, apellido):
        self.apellido = apellido

    def getDni(self):
        return self.dni
    def setDni(self, dni):
        self.dni = dni

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono

    
    def parts(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("DNI:", self.dni)
        print("Edad:", self.edad)
        print("Direccion:", self.direccion)
        print("Nro de telefono:", self.telefono)

    def to_dict(self):
        dictio = """{
    "nombre": self.nombre,
    "apellido": self.apellido,
    "dni": self.dni,
    "edad": self.edad,
    "direccion": self.direccion,
    "telefono": self.telefono
}"""
        return dictio
