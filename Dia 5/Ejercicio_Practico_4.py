def contar_primos(numero):
    for elemento in range(2, numero):
        if numero % elemento == 0:
            return False
    return True

print(contar_primos(12))

