# Ejercicio 3

def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    frecuencia = {}

    for palabra in palabras:
        # Incrementar la frecuencia de la palabra en el diccionario 
        # o la establece en 1 si es la primera vez que aparece
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

cadena = input("Ingresa una frase: ")

# Obtener el diccionario de frecuencias de palabras
resultado = contar_palabras(cadena)

# Imprimir el diccionario de frecuencias de palabras
print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")