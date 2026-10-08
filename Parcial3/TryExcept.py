try:
    edad = int(input("Ingrese su edad: "))
    print(f"Edad registrada: {edad}")
except ValueError:
    print("Error: Debe ingresar un número entero")    

# try:
#    resultado = 10 / 0
#except ZeroDivisionError:
#    print("No se puede dividir entre cero.")
