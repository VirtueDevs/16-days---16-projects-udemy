def chequear_3_cifras(lista):
    lista_3_cifras = []

    for numero in lista:
        if numero in range(100,1000):
            lista_3_cifras.append(numero)
        else:
            pass

    return lista_3_cifras

result = chequear_3_cifras([299, 30,500, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900])
print(result)