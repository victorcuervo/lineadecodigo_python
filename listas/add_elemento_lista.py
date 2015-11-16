# Codigo que nos permite add un elemento a una lista

lista = [1,2,3,4,5]

# Metodo append
lista.append(6)
print lista

#Indicando el ultimo elemento
lista[len(lista):] = [7]  # Lo mismo que .append
print lista

# Metodo extend
lista.extend([8])
print lista