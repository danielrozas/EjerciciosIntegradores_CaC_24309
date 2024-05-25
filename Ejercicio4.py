# Ejercicio 4

def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    frecuencia = {}

    for palabra in palabras:
        # Incrementar la frecuencia de la palabra en el diccionario 
        # o la establece en 1 si es la primera vez que aparece
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

def tupla_mas_repetida(diccionario):
    if not diccionario:
        return None, None

    valores = list(diccionario.values())
    indice_mayor_valor = valores.index(max(valores))
    return indice_mayor_valor


cadena = input("\nIngresa una frase: ")
print ("\n")

# Obtener el diccionario de frecuencias de palabras
resultado = contar_palabras(cadena)

# Imprimir el diccionario de frecuencias de palabras
print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

print ("\n")

indice = tupla_mas_repetida(resultado)

tuplas = list(resultado.items())


print("Tupla con palabras mas repetidas y su valor ", tuplas[indice])
