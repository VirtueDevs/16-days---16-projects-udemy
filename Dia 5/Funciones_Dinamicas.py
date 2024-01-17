def chequear_3_cifras(numero):
    return numero in range(100,1000) #Verificar con IN se está realizando una comparacion booleana

suma = 586 +402

resultado = chequear_3_cifras(658)
print(resultado)
resultado1 = chequear_3_cifras(68)
print(resultado1)

resultado3 = chequear_3_cifras(suma)
print(resultado3)

def chequear_3_cifra(lista):
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            pass

    return False

result = chequear_3_cifra([299, 30,500])
print(result)
