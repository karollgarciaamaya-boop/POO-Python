#atributos de clase: son caracteristicas comunes a todos los objetos de una clase.
#Se definen dentro de la clase pero fuera de cualquier metodo
#Se accede a ellos mediante la clase o mediante un objeto de la clase

class Perro:
    especie= "Canis familiaris"

    def __init__(self, nombre, edad):
        #Atributos de instancia;propios de cada objeto
        self.nombre=nombre
        self.edad=edad

    #esto es unmetodo de instancia ,que es una funcioon que pertenece
    #a la casa y que puede acceder a los atributos de instancia y de clase
    #siempre se definen con verbos en infinitivo(ar,er,ir)
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!" 

rex=Perro("Rex", 3)
luna=Perro("luna", 5)

#acceso a atributos de clase
print(f"Especie de {rex.nombre}:{rex.especie}")
print(f"Especie de {luna.nombre}:{luna.especie}")

#acceso a atributos de instancia

print(f"{rex.nombre} tiene {rex.edad} años.")
print(f"{luna.nombre} tiene {luna.edad} años.")

#llamada a metodos de instancia
print(rex.ladrar())
print(luna.ladrar())
