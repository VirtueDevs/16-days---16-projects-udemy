mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

resultado = mi_texto[9]
print(resultado)

resultado = mi_texto[-6]
print(resultado)

resultado = mi_texto.index("n")
print(resultado)

resultado = mi_texto.index("prueba")
print(resultado)

# Index sólamente busca de izquierda a derecha y se detiene al encontrar
# El primer resultado

#resultado = mi_texto.index("a", 5,10)  #No es inclusivo, hasta antes de empezar el caracter 10, por eso devuelve error.
#print(resultado)

#---------------------------------------------------------------------------------------------------

#Reverse
resultado = mi_texto.rindex("a")
print(resultado)

resultado = mi_texto.rindex("b")
print(resultado)