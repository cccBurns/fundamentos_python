# Escribe un programa que verifique si una palabra dada por el usuario es un palíndromo (se lee igual de adelante hacia atrás y viceversa).

# Solicitar la entrada del usuario
palabra = input("Introduce una palabra: ")

# Verificar si la palabra es un palíndromo
es_palindromo = palabra == palabra[::-1]

# Imprimir el resultado
if es_palindromo:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")