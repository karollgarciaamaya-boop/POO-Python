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

class Contador:
    total=0#numero de clase
    def __init__(self):
        Contador.total +=1#modifica el valor compartido
        self.numero=Contador.total#de e instacia
a=Contador()
b=Contador()
print(a.numero, b.numero, Contador.total)# 1 2 2 

#NOTAAAAA!!!
#LOs atributos privados (__nombre) no se pueden acceder directamente

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # privado
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto
    def retirar(self, monto):
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto
    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.consultar_saldo()) # 1500
# print(cuenta.__saldo) # AttributeError

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius # pasa por el setter
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter #Esto son decoradores

    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Por debajo del cero absoluto")
        self._celsius = valor
    @property
    def fahrenheit(self): # propiedad calculada, solo lectura
       return self._celsius * 9 / 5 + 32

t = Temperatura(25)
print(t.fahrenheit) # 77.0
t.celsius = 30 # usa el setter con validación


#HERENCIAAAAAAAAA!

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def descripcion(self):
        return f"{self.nombre} gana ${self.salario:,.0f}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario) # inicializa la parte del padre
        self.equipo = equipo
    def descripcion(self): # sobrescritura (override)
        base = super().descripcion()
        return f"{base} y dirige a {len(self.equipo)} personas"



g = Gerente("Marta", 8_000_000, ["Luis", "Sara"])
print(g.descripcion())
print(isinstance(g, Empleado)) # True
print(issubclass(Gerente, Empleado)) # True

#Polimorfismo por herencia!!!!!
class Figura:
    def area(self):
        raise NotImplementedError

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base, self.altura = base, altura
def area(self):
    return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14159 * self.radio ** 2
    
figuras = [Rectangulo(3, 4), Circulo(2)]
for f in figuras:
    print(f.area()) # mismo mensaje, resultado distinto