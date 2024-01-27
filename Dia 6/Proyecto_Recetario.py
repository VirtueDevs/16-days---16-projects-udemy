from pathlib import Path
import os

lista_catergorias = ["Carnes", "Ensaladas", "Pastas", "Postres"]
ruta_receta = Path("C:\\Users\\Andres\\Desktop\\Recetas")

def leer_receta():
    return

def crear_receta():
    return

def editar_receta():
    return

def eliminar_receta():
    return



print("Bienvenido al recetario")
print("La ruta de las recetas es: ", ruta_receta)

while True:
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")
    eleccion = input("¿Qué quieres hacer? \n >")

    if eleccion == "1":
        leer_receta()
    elif eleccion == "2":
        crear_receta()
    elif eleccion == "3":
        editar_receta()
    elif eleccion == "4":
        eliminar_receta()
    elif eleccion == "5":
        break
    elif eleccion == "6":
        break
    else:
        print("Opción no válida")
        continue