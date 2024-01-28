# ##
# @file reemplazar-ultima-coincidencia.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com//python/rxxx/
# @description Reemplazaremos la última coincidencia de la frase mediante rfind y rsplit
# ##

cadena = "Hola Víctor, ¿Cómo estás?. Quería comentarte Víctor."
buscar = "Víctor"
reemplazarpor = "Marta"

# 1. Mediante rfind
indice = cadena.rfind(buscar)
cadenareemplazada = cadena[0:indice]  + reemplazarpor + cadena[indice+len(buscar):]
print (cadenareemplazada)

# 2. rsplit
dividida = cadena.rsplit(buscar,1)
cadenareemplazada = reemplazarpor.join(dividida)
print (cadenareemplazada)