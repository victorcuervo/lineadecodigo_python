# ##
# @file ultimo-punto-frase.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   16/septiembre/2023
# @url  http://lineadecodigo.com/python/pdte/
# @description Encontrar el último punto en una frase con Python
# ##


# Tenemos una descripción
cadena = 'Estaba escribiendo un texto. Porque tenía que publicarlo. Era un texto demasiado largo.'

# Cortamos una parte para un resumen
cadena = cadena[0:40]

# Buscamos la posición del último punto para no dejar la frase a medias
print ("El último punto está en la posición "  + str(cadena.rfind('.')))
print (cadena[0:cadena.rfind('.')+1])