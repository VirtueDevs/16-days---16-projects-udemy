'''def suma(a,b):
    return a+b

 print(suma(1,2,8)) -> ERROR '''

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    
    return total
    #return sum(args)

print(suma(1,2,8,20,30,40,50,60,70,80,90,100))

# Practica1:

def suma_cuadrados(*args):
    total = 0
    
    for arg in args:
        cuadrado = arg*arg
        total += cuadrado
    
    return total
    
print(suma_cuadrados(1,2,3))
    
# Practica2:

def suma_absolutos(*args):
    suma = 0
    absoluto = 0
    for arg in args:
        if arg < 0:
            absoluto = arg * (-1)
            suma += absoluto
        else:
            suma += arg
    
    return suma
            
print(suma_absolutos(1,2,-1)) 

#Practica3: 

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'