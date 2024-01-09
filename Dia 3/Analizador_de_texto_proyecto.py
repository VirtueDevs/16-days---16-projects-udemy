texto = input("Por favor indique el texto: ")
texto = texto.lower()
lista_texto = list(texto)

letras = []

letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la primera letra: ".lower()))

print("\n")

count_letra_1 = lista_texto.count(letras[0])
count_letra_2 = lista_texto.count(letras[1])
count_letra_3 = lista_texto.count(letras[2])

print("\n")
print("CANTIDAD DE LETRAS REPETIDAS")
print(f"""La letra {letras[0]} se encuentra {count_letra_1} veces.\nLa letra {letras[1]} se encuentra {count_letra_2} veces.\nLa letra {letras[2]} se encuentra {count_letra_3} veces.""")

print("\n")
print("TOTAL DE PALABRAS EN EL TEXTO")
texto_a_lista = texto.split()
count_texto = len(texto_a_lista)
print(f"hay un total de {count_texto} palabras en el texto ")

print("\n")
print("LETRA INICIAL Y LETRA FINAL")
print(f"Primera letra del texto es {lista_texto[0]}")
print(f"La ultima letra del texto es {lista_texto[-1]} ")

print("\n")
print("TEXTO AL REVÉS")
texto_a_lista.reverse()
texto_invertido = ' '.join(texto_a_lista)
print(f"Tu texto al revés es: '{texto_invertido}'")

print("\n")
print("PYTHON SE ENCUENTRA EN EL TEXTO?")
python_is_here = bool("python" in texto)
dic = {True:"si", False:"no"}
print(f"'Python' se encuentra en el texto? \n {dic[python_is_here]} \n")