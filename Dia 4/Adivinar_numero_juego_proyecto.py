from random import *

nombre_jugador = input("Bienvenido \n Digita tu nombre por favor: ")

numero = randint(1,100)

print(f"{nombre_jugador}, he pensado un número entre el 1 y el 100\n tienes 8 intentos para adivinar cuál cees que es el número.\n ")

intentos = list(range(1,9))

for intento in intentos:
    eleccion = int(input(f"Este es el intento {intento}, por favor indica el número: "))

    if eleccion < 1 or eleccion > 100:
        print("El numero elegido no está permitido")
    elif eleccion < numero:
        print("El número elegido es menor al número que he pensado")
    elif eleccion > numero:
        print("El número elegido es mayor al número que he pensado")
    else:
        print(f"Haz acertado correctamente, te ha tomado {intento} intentos \n")
        break
    print("\n")

if eleccion != numero:
    print(f"Lo siento, se han agotado el número de intentos. El número secreto era {numero}")

print("El juego ha terminado")


