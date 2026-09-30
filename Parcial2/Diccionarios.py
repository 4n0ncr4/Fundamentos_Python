taquerias = {
    "Taquería 1" : {
        "Nombre" :  "Tacos Emilio",
        "Empleados" : 12,
        "Combos" : ["2 por 1", "Otro combito"]
    },
    "Taquería 2" : {
        "Nombre" :  "Taqueria Grillos",
        "Empleados" : 5,
        "Combos" : ["2 por 2", "Otro combito 2"]
    }
}

for clave,valor in taquerias.items():
    print("===============================")
    print(clave)
    print(valor["Nombre"])
    print(valor["Empleados"])
    for lista in valor["Combos"]:
        print("cada combo: ", lista)