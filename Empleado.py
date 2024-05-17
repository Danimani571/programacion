from Persona import Persona
class Empleado(Persona):
    contador_empleados = 0

    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__empleado_eliminado = False
        Empleado.contador_empleados += 1
#encapsulamiento
    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo(self):
        return self.__sueldo

    @property
    def empleado_eliminado(self):
        return self.__empleado_eliminado

    @empleado_eliminado.setter
    def empleado_eliminado(self, eliminado):
        self.__empleado_eliminado = eliminado

    def eliminar_empleado(self):
        self.empleado_eliminado = True
        Empleado.contador_empleados -= 1

daniel = Empleado("Daniel", 50000)
alissa = Empleado("Alissa", 55000)
gerardo = Empleado("Gerardo", 60000)
vanessa = Empleado("Vanessa", 52000)
#metodo str
print(f"Total de empleados creados: {Empleado.contador_empleados}")
print(f"Nombre de Daniel: {daniel.nombre}")
print(f"Sueldo de Vanessa: {vanessa.sueldo}")