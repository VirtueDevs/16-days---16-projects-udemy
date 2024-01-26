from pathlib import Path
import os

lista_catergorias = ["Carnes", "Ensaladas", "Pastas", "Postres"]
ruta_receta = Path("C:\\Users\\Andres\\Desktop\\Recetas")

def leer_receta():
    
    elegir_categoria = input("¿Qué categoría quieres ver?:\n 1.Carnes\n 2. Ensaladas\n 3. Pastas\n 4. Postres\n ")

    if elegir_categoria == "1":
        lista_carnes = []
        ruta_carnes = Path(ruta_receta, Path('Recetas\\Carnes'))
        elementos_carnes = os.listdir(ruta_carnes)
        numero_recetas_carnes = len(elementos_carnes)
        print(f"Ingresaste a la categoría {lista_catergorias[0]}. Actualmente hay {numero_recetas_carnes} recetas")
        for elemento_carnes in elementos_carnes:
            lista_carnes.append(elemento_carnes)
        print(f"Las recetas disponibles son: {lista_carnes}")
        






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