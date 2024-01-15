palabra = 'python'

"""lista = []

for letra in palabra:
    lista.append(letra)

print(lista)"""

#Otra forma:

lista = [letra for letra in palabra] # "letra" es una variable interna. Podria funcionar = [xx for xx in palabra]
# lista = [letra for letra in 'python']
"""lista = [n for n in range(0,21,2)]""" #Lista de numeros dessde 0 a 20 de 2 en 2
"""lista = [n / 2 for n in range(0,21,2)]""" #Lista de numeros divido en 2 entre el rango de 0 a 20
"""lista = [n for n in range(0,21,2) if n * 2 > 10]"""
"""lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]"""
print(lista)


pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)