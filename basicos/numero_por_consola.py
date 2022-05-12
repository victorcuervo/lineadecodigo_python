# ##
# @file numero_por_consola.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   12/mayo/2022
# @url  http://lineadecodigo.com/python/numero-por-teclado-en-python/
# @description Controlar que los datos de entrada son numéricos
# ##

while True:
    try:
        valor = int(input("Inserta un valor que sea un número: "))
        break
    except ValueError:
        print("Lo que has introducido no es un número. Inténtalo de nuevo.")

print ("Gracias! Has introducido el número " + str(valor))


