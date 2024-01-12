lista = ['a','b','c']

for indice,item in enumerate(lista):
    print(indice,item)

for index,val in enumerate(range(50,55)):
    print(index,val)

mis_tuples = list(enumerate(lista))
print(mis_tuples)

print(mis_tuples[1][0])