# ##
# @file formato-cadenas.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   17/septiembre/2023
# @url  http://lineadecodigo.com/python/pdte/
# @description Uso de % y de la función format para dar formato a una cadena
# ##


# %s %f para cadenas y números flotantes
s = "Los números son %d y %d." % (5, 10)
print(s) #Los números son 5 y 10.

s2 = "Te llamas {nombre}".format(nombre="Victor")
print (s2)

s = "Cadena {} + {}".format(5,1)
print (s)