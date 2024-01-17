lista_numeros = [1,50,500,5000,750]

def suma_menores(lista_numeros):
    suma_de_elementos = 0
    for elemento in lista_numeros:
        if 0 < elemento < 1000:
            suma_de_elementos += elemento
        else:
            pass
        
    return suma_de_elementos

print(suma_menores(lista_numeros))