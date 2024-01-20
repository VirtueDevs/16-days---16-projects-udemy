def devolver_distintos(a,b,c):
    suma = a+b+c
    total = [a,b,c]

    if suma > 15:
        return(max(total))
    elif suma < 10:
        return(min(total))
    else:
        total.sort()
        return(total[1])

print(devolver_distintos(1,12,3))

