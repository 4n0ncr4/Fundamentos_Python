while True:
	print("------Menú------")
	print("1. Hamburguesas")
	print("2. Pizzas")
	print("3. Pasta")
	print("4. Postres")

	opcion = input("Escoge una categoría (1-4): ")

	match opcion:
		case "1":
			categoria = [
				"Hamburguesa doble de queso: $300",
				"Hamburguesa vegana: $250",
				"Hamburguesa de pollo: $225",
			]
		case "2":
			categoria = [
				"Pizza solo de Queso: $150",
				"Pizza de Pepperoni: $180",
				"Pizza de Champiñones: $160",
			]
		case "3":
			categoria = [
				"Espaguetis a la Boloñesa: $200",
				"Fettuccine Alfredo: $220",
				"Pesto pasta: $180",
			]
		case "4":
			categoria = [
				"Pastel de Chocolate: $120",
				"Cheesecake: $100",
				"Ensalada de Frutas: $80",
			]
		case _:
			print("Opción inválida. Escoge un número del 1 al 4.")
			continue

	for numero, item in enumerate(categoria, start=1):
		print(f"{numero}. {item}")

	seleccion = int(input("Escoge un producto (1-3): "))
	match seleccion:
		case 1 | 2 | 3:
			print(categoria[seleccion - 1])
			break
		case _:
			print("Opción inválida. Escoge un número del 1 al 3.")