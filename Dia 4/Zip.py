nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Bogotá','Madrid']

combinados = list(zip(nombres,edades,ciudades))

print(combinados)
print(type(combinados))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")