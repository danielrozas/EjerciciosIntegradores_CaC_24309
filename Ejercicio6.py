# Ejercicio 6

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")

    def get_nombre(self):
        return self._nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero no negativo.")

    def get_edad(self):
        return self._edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:  # Suponiendo que el DNI tiene 9 caracteres
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")

    def get_dni(self):
        return self._dni

    def mostrar(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, DNI: {self.get_dni()}")

    def es_mayor_de_edad(self):
        return self.get_edad() >= 18

# Ejemplo de uso
persona1 = Persona("Juan", 25, "12345678A")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.es_mayor_de_edad())
