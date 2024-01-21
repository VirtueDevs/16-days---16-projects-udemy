lista_numeros = [2,3,4,5,6]

def cantidad_pares(lista_numeros):
    count = 0
    for elemento in lista_numeros:
        if elemento % 2 == 0:
            count += 1
        else:
            pass
        
    return count