# Estructuras de If's

tipo_persona = input("Ingrese el tipo de persona: ") # Input de tipo string

if(tipo_persona == "estudiante"):
    print("Bienvenido lincito") 
    avance = int(input("Ingrese su avance: ")) # Se castea a entero (int)
    cantidad_materias = int(input("Cuantas materias tienes en especial? "))
    if(avance >= 80 and cantidad_materias == 0):
        print("Bienvenido a residencias")
elif(tipo_persona == "docente"):
    print("Bienvenido docente")
else:
    print("Ni si quiera se quien eres :()")
print("------------------------------")

print (5 == 2)
print (5 <= 2)
print (5 >= 2)
print (5 != 2)
print (5 < 2)
print (5 > 2)