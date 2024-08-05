#Escribe un programa que tome un número como entrada del usuario y determine si es par o impar.

numero = int(input("introduce un numero"))

# Verificar si el numero es par o impar
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")