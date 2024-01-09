mi_set1 = set([1,2,3,4,5])
print(type(mi_set1))
print(mi_set1)


otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

mi_set = set([1,2,(1,2,3),3,4,5])
print(mi_set)

print(len(mi_set1))
print(2 in mi_set1)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add('4')
print(s1)

s1.remove(3)
print(s1)

s1.discard(6)  #No borra el elemento que no existe, sigue el proceso.
print(s1)

sorteo = s1.pop()
print(sorteo)

s1.clear()
print(s1)