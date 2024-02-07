"""
Crear un arxiu de nom vehicle.py. 
En aquest arxiu s’ha de crear una class de nom vehicle. 
Aquesta class ha de tindre:

Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

"""

class vehicle:
    def __init__(self, marca, model, color, traccio, motor, puertas):
        self.marca = marca
        self.model = model
        self.color = color
        self.traccio = traccio
        self.motor = motor
        self.puertas = puertas

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    
    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getTraccio(self):
        return self.traccio
    def setTraccio(self, traccio):
        self.traccio = traccio

    def getMotor(self):
        return self.motor
    def setMotor(self, motor):
        self.motor = motor

    def getPuertas(self):
        return self.puertas
    def setPuertas(self, puertas):
        self.puertas = puertas

    
    def parts(self):
        print("Marca:", self.marca)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Tracció:", self.traccio)
        print("Motor:", self.motor)
        print("Nro de Puertas:", self.puertas)

    def to_dict(self):
        dictio = """{
    "marca": self.marca,
    "model": self.model,
    "color": self.color,
    "traccio": self.traccio,
    "motor": self.motor,
    "puertas": self.puertas
}"""
        return dictio
