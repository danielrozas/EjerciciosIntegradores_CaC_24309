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

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, porcentaje):
        self.bonificacion = porcentaje    

    def mostrar(self, porcentaje):
        print("Cuenta Joven")
        print("Bonificación:", self.bonificacion)
        print("\n")
        
class Valida():        
    def es_titular_valido(edad):
        if 18 < edad < 25:
            # Titular Valido = True
            return True
        else:
            # Titular Valido = False
            return False     


# Ejemplo de uso:
if __name__ == "__main__":
 
    print("\n")
    titular = input("Ingrese Nombre del Titular: ")
    edad_titular = int(input("Ingrese Edad:"))
    print("\n")
    
    valor = 125
    
    resultado = Valida.es_titular_valido(edad_titular)
 
    bonificacion = 10

   # Crear una instancia de la clase Cuenta 
    cuentajoven = CuentaJoven(titular, valor, bonificacion)

    if  resultado == True:
        cuentajoven.retirar(20)
        cuentajoven.mostrar(bonificacion)
        

    