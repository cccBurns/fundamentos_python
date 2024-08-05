# Escribe un programa que calcule el factorial de un número dado por el usuario.

# Solicitar entrada
numero = int(input("introduce un numero: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i
    
print(f"El factorial de {numero} es {factorial}")

