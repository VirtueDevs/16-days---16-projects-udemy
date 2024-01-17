'''def suma(a,b):
    return a+b

 print(suma(1,2,8)) -> ERROR '''

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(1,2,8,20,30,40,50,60,70,80,90,100))