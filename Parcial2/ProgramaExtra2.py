categorias = ["Coche compacto", "SUV Estándar", "Minivan",
            "SUV Premium", "Furgoneta", "Camión de carga"]
precios = [600, 1000, 1600, 2000, 3000, 4000]

def mostrar_categorias():
    for i in range(len(categorias)):
        print(f"{i + 1}.- {categorias[i]} ${precios[i]} al día")

def seleccionar_categoria():
    opcion = int(input("Seleccione una categoría (1-6): "))
    while opcion < 1 or opcion > len(categorias):
        print("Opción inválida. Por favor, seleccione una categoría válida.")
        opcion = int(input("Seleccione una categoría (1-6): "))
    return opcion - 1

def dias_renta():
    dias = int(input("Cuántos días va a rentar el vehículo?: "))
    while dias < 1:
        print("Vuelve a ingresar el número de días (Mayor a 1): ")
        dias = int(input("Ingrese la cantidad de días que desea rentar el vehículo: "))
    return dias

def calcular_costo_total(indice, dias):
    return precios[indice] * dias

def mostrar_resultados(indice, dias):
    costo_total = calcular_costo_total(indice, dias)
    print(f"Categoría seleccionada: {categorias[indice]}")
    print(f"Días de renta: {dias}")
    print(f"Costo total: ${costo_total}")

print("Bienvenido! Esta es nuestra selección de vehículos disponibles:")
print()
mostrar_categorias()
indice = seleccionar_categoria()
dias = dias_renta()
mostrar_resultados(indice, dias)
