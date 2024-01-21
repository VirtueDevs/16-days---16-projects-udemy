mi_archivo = open('prueba.txt')

#print(mi_archivo.read())

una_linea = print(mi_archivo.readline())
print(una_linea.strip())

una_linea = print(mi_archivo.readline())
print(una_linea.strip())

una_linea = print(mi_archivo.readline())
print(una_linea.strip())

mi_archivo.close()
