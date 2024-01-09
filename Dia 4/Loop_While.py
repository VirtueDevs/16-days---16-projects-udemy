monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más dinero")

print("\n")
respuesta = 's'

while respuesta == 's':
    respuesta = input ("quieres seguir? (s/n): ")
else:
    print("Gracias")

# PASS -> No hace nada
    

while respuesta == 's':
    pass

print("hola")

# BREAK -> Interrumpir

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

# CONTINUE -> Interrumpe la iteración actual pero no interrumpe el loop en si mismo, sino vuelve al comienzo y continua con la interaccion siguiente
print("\n")    
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)