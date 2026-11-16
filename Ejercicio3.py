class Mascota:
    def __init__(self, nombre, dueno, edad, peso):
        self.nombre = nombre
        self._dueno = dueno
        self.__edad = edad
        self.__peso = peso

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: la edad no puede ser negativa")

    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0 and nuevo_peso <= 100:
            self.__peso = nuevo_peso
        else:
            print("Error: el peso debe ser mayor que 0 y maximo 100 kg")


m = Mascota("Firulais", "Ana", 3, 20)

print(m.nombre)
print(m._dueno)
m.set_edad(-5)
m.set_edad(4)
print(m.get_edad())


m.set_peso(150)
m.set_peso(25)
print(m.get_peso())