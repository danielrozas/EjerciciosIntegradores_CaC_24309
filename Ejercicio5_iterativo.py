# Ejercicio 5
# Forma iterativa

def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: Por favor ingrese un valor entero válido.")

numero_entero = get_int()
print("El valor entero ingresado es:", numero_entero)