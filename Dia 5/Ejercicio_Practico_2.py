def recibe_cadena(cadena):

    cadena = cadena.lower()
    lista_cadena = []
    caracteres = list(cadena)

    for elemento in caracteres:

        if elemento not in lista_cadena:
            lista_cadena.append(elemento)
            lista_cadena.sort()
        else:
            pass
        
    return lista_cadena

print(recibe_cadena("Entretenido"))
        