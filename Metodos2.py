def calcular_salario(salario_bruto):
    if (salario_bruto < 9500):
        return salario_bruto
    else:
        descuento = salario_bruto * 0.26
        return salario_bruto - descuento

def obtener_aguinaldo(salario_bruto):
    salario_diario = salario_bruto / 30
    print("Cuanto gano por día :( " + salario_diario)
    

print("Empresa: GAMA CONSULTORES IA")
print(calcular_salario(9000))
print(obtener_aguinaldo(9000))
print("Empresa: Desarrollador Java Full Stack Intermedio Senior ")
print(calcular_salario(36000))