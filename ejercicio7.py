# Escribe un programa que genere una lista de números pares del 1 al 20.

# Inicializar la lista de números pares
numeros_pares = []

# Generar los números pares
for numero in range(1, 21):
    if numero % 2 == 0:
        numeros_pares.append(numero)

# Imprimir el resultado
print(f"La lista de números pares del 1 al 20 es: {numeros_pares}")