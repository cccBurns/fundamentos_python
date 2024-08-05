# Bucle For

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
    
#Escribe un programa que imprima cada elemento de la lista [10, 20, 30, 40, 50] utilizando un bucle for.
numeros = [10, 20, 30, 40, 50]
for numero in numeros:
    print(numero)    
    
#Escribe un programa que imprima cada carácter de la cadena "Python" utilizando un bucle for.
cadena = "Python"
for caracter in cadena:
    print(caracter)    
    
#Escribe un programa que cuente cuántas veces aparece el carácter 'a' en la cadena "anaconda".
cadena = "anaconda"
contador = 0
for caracter in cadena:
    if caracter == 'a':
        contador += 1
print(f"El carácter 'a' aparece {contador} veces en la cadena.")

