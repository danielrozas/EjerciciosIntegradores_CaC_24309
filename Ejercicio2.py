# Ejercicio 2

def minimo_comun_multiplo(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) 


x = 125
y = 15

print("El Mínimo Común Multiplo de", x, "y", y, "es:", minimo_comun_multiplo(x, y))