print("Bienvenido al sistema de cálculo de comisiones")

nombre = input("Por favor indique su nombre completo :")
comision = input("Ingrese la venta total:")
comision_to_float = float(comision)

resultado_comision = (comision_to_float * (13 / 100))
total_comision = round(resultado_comision,3)

print(f"Empleado/a {nombre}, su comisión total es de {total_comision} pesos")
