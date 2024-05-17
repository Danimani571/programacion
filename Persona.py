class Persona:
    contador_personas = 0

    def __init__(self, nombre, genero, edad, direccion):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

        Persona.contador_personas += 1

    def obtener_nombre(self):
        return self._nombre

    def obtener_genero(self):
        return self._genero

    def obtener_edad(self):
        return self._edad

    def obtener_direccion(self):
        return self._direccion

    def mostrar_datos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Género: {self._genero}")
        print(f"Edad: {self._edad}")
        print(f"Dirección: {self._direccion}")

persona1 = Persona("Vanessa", "Femenino", 19, "28 de Mayo")
persona2 = Persona("Daniel", "Masculino", 25, "Daule")
persona2 = Persona("Gerardo", "Masculino", 18, "Entrada de la 8")
persona1 = Persona("Alissa", "Femenino", 21, "Santa elena")

persona1.mostrar_datos()
persona2.mostrar_datos()

print(f"Total de personas creadas: {Persona.contador_personas}")
