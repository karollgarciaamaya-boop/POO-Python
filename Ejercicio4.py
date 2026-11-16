class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")


class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


class Gato(Mascota):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")


class Cachorro(Perro):
    def jugar(self):
        print(f"{self.nombre} está jugando con la pelota")


perro = Perro("Firulais", "Labrador")
gato = Gato("Michi", "negro")

perro.comer()
perro.ladrar()
gato.comer()
gato.maullar()

c = Cachorro("Toby", "Pug")
c.comer()
c.ladrar()
c.jugar()

# Un Cachorro hereda directamente de la clase Perro
# y también hereda indirectamente de la clase Mascota,
# porque Perro es hija de Mascota.