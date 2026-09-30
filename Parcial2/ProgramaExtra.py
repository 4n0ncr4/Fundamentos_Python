longitud = int(input("Ingresa la cantidad de alumnos: "))

arreglo = []
for elemento in range(longitud):
	valor = input(f"Ingresa el nombre del alumno {elemento + 1}: ")
	arreglo.append(valor)

calificaciones = []
for elemento in range(len(arreglo)):
	valor = float(input(f"Ingresa la calificación de {arreglo[elemento]}: "))
	while valor < 0 or valor > 10:
		print("Favor de ingresar una calificación válida (0 al 10)")
		valor = float(input(f"Ingresa la calificación de {arreglo[elemento]}: "))
	calificaciones.append(valor)

print("Lista de calificaciones:")
for elemento in range(len(arreglo)):
	print(arreglo[elemento], calificaciones[elemento])