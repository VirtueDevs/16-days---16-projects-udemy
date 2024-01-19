def consecutivos(numero, *args):
    for i in range(len(args) - 1):
        if args[i] == numero == args[i + 1]:
            return True
    return False

numero = 0

print(consecutivos(numero, 1,1,9,0,2,3))