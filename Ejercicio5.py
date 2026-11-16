from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} salta")


class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Muuu!")

    def moverse(self):
        print(f"{self.nombre} camina despacio")


class Pajaro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Pío!")

    def moverse(self):
        print(f"{self.nombre} vuela")


animales = [Perro("Firulais"), Gato("Michi"), Vaca("Lola"), Pajaro("Piolín")]

for a in animales:
    a.hacer_sonido()

for a in animales:
    a.moverse()
