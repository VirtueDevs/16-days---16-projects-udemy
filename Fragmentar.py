texto = "ABCDEFGHIJKLM"
fragmento  = texto[2]
print(fragmento)


fragmento = texto[2:5]
print(fragmento)

fragmento = texto[2:]
print(fragmento)

fragmento = texto[:5]
print(fragmento)

fragmento = texto[2:10:2]   #El tercer parametro sirve para saltarse según el númer, las posiciones del str
print(fragmento)

fragmento = texto[::3]
print(fragmento)

fragmento = texto[::-2]
print(fragmento)