# Escribe un programa que tome una lista de números y encuentre el número mayor.# Definir una lista de números

numeros = [4, 1, 8, 7, 2, 9, 5]

# Inicializar el número mayor
mayor = numeros[0]

# Encontrar el número mayor
for numero in numeros:
    if numero > mayor:
        mayor = numero

# Imprimir el resultado
print(f"El número mayor en la lista es: {mayor}")