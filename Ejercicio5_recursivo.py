# Ejercicio 5
# Forma recursiva

def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: Por favor ingrese un valor entero válido.")
        return get_int()

numero_entero = get_int()
print("El valor entero ingresado es:", numero_entero)