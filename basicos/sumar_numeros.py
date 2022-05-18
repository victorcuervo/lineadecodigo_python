# ##
# @file sumar_numeros.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   13/octubre/2021
# @url  http://lineadecodigo.com/python/sumar-numeros-en-python/
# @description Sumar números por consola en Python
# ##

# Programa sin controles
print("Programa sin controles")
n1 = input("¿Dime el primer número?")
n2 = input("¿Dime el segundo número?")

# Suma de caracteres y no números
print (n1+n2)


print("Programa con controles")
# Controlar el error de conversión

while True:
    try:
        n1 = int(input("¿Dime el primer número?"))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")

while True:
    try:
        n2 = int(input("¿Dime el segundo número?"))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")

print ("La suma de los dos números es: " + str(n1+n2))