#archivo = open('prueba.txt', 'r')
archivo = open('prueba1.txt', 'w')

#archivo.write('soy el nuevo texto')
archivo.write('hola\n')
archivo.write('mundo\n')

archivo.close()

archive = open('prueba.txt', 'w')
archive.writelines(['hola',  'mundo', 'aquí', 'estoy'])
archive.close()