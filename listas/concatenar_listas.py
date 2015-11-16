#Concatenar listas en Python
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

# Con operador +
lista1+=lista2
print "Con operador +"
print lista1

# Reseteamos
lista1 = [1,2,3,4]

# Con un append
lista1.extend(lista2)
print "Con metodo .extend()"
print lista1

