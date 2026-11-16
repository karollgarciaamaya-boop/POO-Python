class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un {self.especie}")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

perro = Mascota("Firulais", "perro", 2)
gato = Mascota("Michi", "gato", 5)

perro.presentarse()
gato.presentarse()

perro.cumplir_anios()
perro.cumplir_anios()