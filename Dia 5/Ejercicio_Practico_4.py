def contar_primos(numero):
    primos = []
    for elemento in range(2, numero):
        es_primo = True
        for i in range(2, int(elemento ** 0.5) + 1):
            if elemento % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(elemento)
    
    return len(primos)
            
print(contar_primos(10))
            
