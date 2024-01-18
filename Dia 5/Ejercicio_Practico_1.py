def devolver_distintos(*args):
    suma = []
    for arg in args:
        suma.append(arg)
        suma.sort()

    total = sum(suma)

    if total > 15:
        return(max(suma))
    elif 10 <= total <= 15:
        return(suma[1])
    else:
        return(min(suma))

print(devolver_distintos(1,12,2))

