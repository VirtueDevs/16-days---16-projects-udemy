precios_cafe = [('capuccino',1.5),('Expresso',2.5),('Latte',1.8),('Mocha',2.0),('Americano',1.0)]

'''for elemento in precios_cafe:
    print(elemento)

#for cafe,precio in precios_cafe:
    print(cafe)

#for cafe,precio in precios_cafe:
    print(precio * 0.45)'''

def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es {cafe} y cuesta {precio}")