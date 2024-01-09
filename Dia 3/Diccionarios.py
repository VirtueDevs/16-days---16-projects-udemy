diccionario = {'c1':'valor1','c2':'valor2'}

print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']

print(resultado)

cliente = {'nombre':'Andrés','apellido':'Ávila','peso':55,'altura':1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic1 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic1['c2'][1].upper())
print(dic1['c1'][1].upper())

dic2 = {1:'a',2:'b'}
print(dic2)

dic2[3] = 'c'
print(dic2)

dic2[2] = 'B' #Sobrescribir la que ya existe
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())