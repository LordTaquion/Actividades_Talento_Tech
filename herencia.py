# Ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

persona1 = Persona("Juan", 25)

alumno1 = Alumno("María", 20, "A12345")

print("Nombre de la persona:", persona1.nombre)
print("Edad de la persona:", persona1.edad)

print("Nombre del alumno:", alumno1.nombre)
print("Edad del alumno:", alumno1.edad)
print("Matrícula del alumno:", alumno1.matricula)

# Ejercicio 2

class Animal:
    def __init__(self, edad, nombre, cantidad_de_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_de_patas = cantidad_de_patas

class Perro(Animal):
    def __init__(self, edad, nombre, cantidad_de_patas, raza):
        super().__init__(edad, nombre, cantidad_de_patas)
        self.raza = raza

animal = Animal(5, "Pelusa", 4)

perro = Perro(3, "Max", 4, "Labrador")

print("Edad del animal:", animal.edad)
print("Nombre del animal:", animal.nombre)
print("Cantidad de patas del animal:", animal.cantidad_de_patas)

print("Edad del perro:", perro.edad)
print("Nombre del perro:", perro.nombre)
print("Cantidad de patas del perro:", perro.cantidad_de_patas)
print("Raza del perro:", perro.raza)

# Ejercicio 3

class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando.")
    
    def frenar(self):
        print("El vehículo está frenando.")

class Automovil(Vehiculo):
    pass  

vehiculo = Vehiculo()

automovil = Automovil()

automovil.acelerar()
automovil.frenar()
