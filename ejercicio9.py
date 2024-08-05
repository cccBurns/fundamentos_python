# Escribe un programa que tome dos listas, una de claves y otra de valores, y cree un diccionario a partir de ellas.

# Definir las listas de claves y valores
claves = ['nombre', 'edad', 'ciudad']
valores = ['Juan', 28, 'Madrid']

# Crear el diccionario
diccionario = dict(zip(claves, valores))

# Imprimir el resultado
print(f"El diccionario creado es: {diccionario}")