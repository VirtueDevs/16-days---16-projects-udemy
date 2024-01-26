import os

#ruta = os.getcwd() -> Obtener la ruta actual
#ruta = os.chdir('C:\\Users\\Andres\\Desktop') # Acceder a carpetas especificas
#ruta = os.makedirs('C:\\Users\\Andres\\Desktop\\otra') # Crear carpetas  (Puede tener nombre de base (ruta) y el nombre del archivo 

#archivo = open('otro_archivo.txt', 'r')

#print(archivo.read())

ruta = 'C:\\Users\\Andres\Desktop\\Python\\Python1\\Dia 6\\prueba.txt'

#elemento = os.path.basename(ruta)  # Obtener el nombre del archivo
#elemento = os.path.dirname(ruta)    # Obtener la ruta del archivo
elemento = os.path.split(ruta)      # Obtener la ruta y el nombre del archivo
print(elemento)

#os.rmdir('C:\\Users\\Andres\\Desktop\\otra') # Eliminar carpetas


otro_archivo = open('C:\\Users\\Andres\\Desktop\\alternativo\\Otro_archivo.txt')
print(otro_archivo.read())


from pathlib import Path #mac, linux, windows

carpeta = Path('/Users/Andres/Desktop/alternativo') #windows, mac, linux
archivo = carpeta / 'Otro_archivo.txt'

#carpeta = Path('/Users/Andres/Desktop/alternativo') #windows, mac, linux / 'Otro_archivo.txt'
#mi_archivo = open(carpeta)

un_archivo = open(archivo)
print(un_archivo.read())