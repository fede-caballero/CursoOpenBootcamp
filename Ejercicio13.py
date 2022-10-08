class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
c1 = Coche("Negro", 4, 5, 180, 4.7)
print(f"El Coche de color {c1.color}, tiene {c1.ruedas} ruedas, {c1.puertas} puertas, alcanza una velocidad maxima de {c1.velocidad} km/h y tiene una cilindrada de {c1.cilindrada}L")
