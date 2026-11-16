class Mascota:
    reino = "Animal"
    total_mascotas = 0
    def __init__(self, nombre, especie):

        self.nombre = nombre
        self.especie = especie

        Mascota.total_mascotas += 1

    def mostrar_total(self):
        print(f"Hay {Mascota.total_mascotas} mascotas registradas")



m1 = Mascota("Firulais", "perro")
m2 = Mascota("Michi", "gato")
m3 = Mascota("Piolín", "pájaro")

print(f"Total de mascotas: {Mascota.total_mascotas}")

print(m1.reino, m2.reino)

print(m1.nombre, m2.nombre, m3.nombre)

m1.mostrar_total()

#¿Qué pasa con el total si borras una mascota con del m1?
#El contador sigue mostrando 3 porque Python no disminuye
#automáticamente el total cuando se elimina una mascota.

#¿Cómo lo solucionarías?
#Utilizando el método __del__() para restar 1 al contador
#cada vez que se elimine una mascota.