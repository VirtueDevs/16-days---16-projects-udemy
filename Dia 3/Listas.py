mi_lista = ['a','b','c']
#otra_lista = ['hola',55,6.1]
print(type(mi_lista))

print(len(mi_lista))

print(mi_lista[0])

print(mi_lista[0:1])

print(mi_lista[0:2])

print(mi_lista[0:])

mi_lista2 = ['d','e','f']

print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2

print(mi_lista3)

mi_lista3[0] = 'alfa'

print(mi_lista3)

mi_lista3.append('g')

print(mi_lista3)

mi_lista3.pop() #Eliminar el ultimo de los elementos

print(mi_lista3)

eliminado = mi_lista3.pop(0) #Elimina un elemento en especifico

print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']

lista.sort() #Ordena alfabeticamente

print(lista)

lista.reverse()

print(lista)