def suma (**kwargs):
    print(type(kwargs))

suma(x=3,y=5,z=2)  #Pares de un nombre y un valor // no es diccionario, pero se imprime como un diccionario.

def suma (**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

suma(x=3,y=5,z=2)

def suma (**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(suma(x=3,y=5,z=2))

#--------------------------------------------------------------

def prueba(num1,num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [15,50,100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

#prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')
prueba(15,50,*args,**kwargs)

#Ejercicio1:

def cantidad_atributos(**kwargs):
    contador = len(kwargs)
    
    return contador

#Ejercicio2:

def lista_atributos(**kwargs):
    lista_1 = []
    for kwarg in kwargs:
        lista_1.append(kwargs[kwarg])
    
    return lista_1

#Ejercicio3:

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
