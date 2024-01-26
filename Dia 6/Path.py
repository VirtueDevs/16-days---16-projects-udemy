from pathlib import Path


base = Path.home() # Obtener la ruta base
guia = Path(base,'Europa', 'España', Path('Barcelona','Sagrada_Familia.txt'))
#guia2 = guia.with_name('La_Pedrera.txt') # Cambiar el nombre del archivo
print(base)
print(guia)
#print(guia2)

print(guia.parent) # Obtener la ruta del archivo sin el nombre del archivo
print(guia.parent.parent) # Obtener la ruta del archivo sin el nombre del archivo y la carpeta anterior
print(guia.parent.parent.parent) # Obtener la ruta del archivo sin el nombre del archivo y las dos carpetas anteriores

guia3 = Path(Path.home(),'Europa')

for txt in Path(guia).glob("**/*.txt"):  # Obtener todos los archivos con extensión .txt
    print(txt)

guia4 = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')

en_europa = guia4.relative_to(Path('Europa')) #Devuelve la ruta relativa a la ruta base
en_espania = guia.relative_to(Path('Europa', 'España'))

print(en_europa)
print(en_espania)