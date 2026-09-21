elementos = ["PostgreSQL", "MongoDB", "InfluxDB", "MySQL", "Redis",
            "Prometheus", "SAP HANA", "Cassandra", "Oracle", "OpenTSDB"]

for i in range(len(elementos)):
    print(f"Cúal es la clasificación de {elementos[i]}? ")
    print("Relacional, ", "No Relacional, ", "Series temporales")
    clasificacion = input("= ")