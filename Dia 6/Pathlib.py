from pathlib import Path, PureWindowsPath

carpeta = Path("/Users/Andres/Desktop/python/Python1/Dia 6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(carpeta.read_text()) # Leer el archivo
print(carpeta.name) # Obtener el nombre del archivo
print(carpeta.suffix) # Obtener la extensión del archivo
print(carpeta.stem) # Obtener el nombre del archivo sin la extensión

if not carpeta.exists():
    print("El archivo no existe")
else:
    print("El archivo existe")


print(ruta_windows)