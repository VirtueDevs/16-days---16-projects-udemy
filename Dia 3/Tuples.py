mi_tuple = (1,2,3,4)
print(type(mi_tuple))

t = (5,5.2,'ff',{'c1':5},[23,'ana'])

print(t[-2])

mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2][0])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

tupla = (1,2,3)
x,y,z = tupla

print(x,y,z)

print(len(mi_tuple))

print(mi_tuple.count(1))

print(mi_tuple.index(2))