import decimal

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular              # Atributo obligatorio
        self.cantidad = decimal.Decimal(cantidad)   # Atributo opcional
        
    def get_titular(self):
        return self.titular

    def set_titular(self, nombre):
        self.titular = nombre

    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, valor):
        if not isinstance(valor, (decimal, type(None))):
            raise ValueError("La cantidad debe ser un valor decimal o nada")
        self.cantidad = valor
        
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
        print("\n")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

# Ejemplo de uso:
if __name__ == "__main__":
    
    # Crear una instancia de la clase Cuenta 
 
    titular="Juan"
    valor= 125.50
    
    cuenta = Cuenta(titular, valor)

    # Mostrar los datos de la cuenta
    cuenta.mostrar()

    # Ingresar dinero en la cuenta
    cuenta.ingresar(100)
    cuenta.mostrar()

    # Retirar dinero de la cuenta
    cuenta.retirar(50)
    cuenta.mostrar()                