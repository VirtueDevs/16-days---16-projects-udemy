from random import shuffle

# Lista inicial
palitos = ['-','--','---','----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# pedirle intento al usuario
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

# comprobar intento
def chequear_intento(lista,intento):

    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

#Practica 1: 

from random import randint

def lanzar_dados():
    
    valor1 = randint(1,6)
    valor2 = randint(1,6)
    
    return valor1,valor2

def evaluar_jugada(valor1,valor2):
    
    suma_dados = valor1 + valor2
    
    if suma_dados <= 6:
        return(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 6 < suma_dados < 10:
        return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

#Practica 2:

lista_numeros = [2,3,4,5,4,25]


def reducir_lista(lista_numeros):
    max_value = max(lista_numeros)
    lista_numeros.remove(max_value)
    
    nueva_lista = []
    for numero in lista_numeros:
        if numero not in nueva_lista:
            nueva_lista.append(numero)
        else:
            pass
        
    return nueva_lista

def promedio(nueva_lista):
    suma = sum(nueva_lista)
    elementos = len(nueva_lista)
    resultado_promedio = suma/elementos
    
    return resultado_promedio

#Practica 3:

from random import choice

def lanzar_moneda():
    lado = ['Cara','Cruz']
    resultado_lanzamiento = choice(lado)
    
    return resultado_lanzamiento

def probar_suerte(resultado_lanzamiento,lista_numeros):
    if resultado_lanzamiento == 'Cara':
        print("La lista se autodestruirá")
        lista_numeros.clear()
        return(lista_numeros)
    else:
        print("La lista fue salvada")
        return(lista_numeros)

lista_numeros = list(range(1,10))
        
resultado_lanzamiento = lanzar_moneda()
lista_resultante = probar_suerte(resultado_lanzamiento,lista_numeros)