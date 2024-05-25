# Ejercicio 1

def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x = 72
y = 6

print("El Máximo Común Divisor de", x, "y", y, "es:", maximo_comun_divisor(x, y))