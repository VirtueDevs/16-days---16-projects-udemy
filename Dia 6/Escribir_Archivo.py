#archivo = open('prueba.txt', 'r')
archivo = open('prueba1.txt', 'w')

#archivo.write('soy el nuevo texto')
archivo.write('hola\n')
archivo.write('mundo\n')

archivo.close()

archive = open('prueba.txt', 'w')
archive.writelines(['hola',  'mundo', 'aquí', 'estoy'])
archive.close()

#lista = ['hola',  'mundo', 'aquí', 'estoy']

'''for p in lista:
    archivo.write(p + '\n')
archivo.close()'''

#prueba1
#archivo = open('prueba.txt', 'a') -> empieza a escribir desde el final del archivo