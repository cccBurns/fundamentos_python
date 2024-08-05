#Escribe un programa que cuente el número de vocales en una cadena dada por el usuario.

# Solicitar la entrada del usuario
cadena = input("Introduce una cadena: ")

# Inicializar el contador de vocales
contador_vocales = 0
vocales = "aeiouAEIOU"

# Contar las vocales
for char in cadena:
    if char in vocales:
        contador_vocales += 1

# Imprimir el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")