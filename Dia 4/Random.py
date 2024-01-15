from random import *

aleatorio = randint(1,50) #Desde el 1 hasta el 50
print(aleatorio)

decimal_aleatorio = round(uniform(1,5),1) #Numeros decimales aleatorios, ENTRE 1 Y 5 CON UN DECIMAL DESPUES DEL PUNTO.
print(decimal_aleatorio)

numero_random = random()
print(numero_random)

colores = ['azul','rojo','verde','amarillo'] # eleccion aleatoria en una lista
aleatorio = choice(colores) 
print(aleatorio)

numeros = list(range(5,50,5)) #Combinacion de la lista (cambiando orden)
shuffle(numeros) ##Shuffle no se puede almacenar en una lista - > no se puede usar con strings porque son objetos inmutables
print(numeros)