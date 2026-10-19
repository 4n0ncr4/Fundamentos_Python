class Carro:

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0
        self.encendido = False
        self.historial_velocidades = [0]

    def mostrar_estado(self):
        print("--------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)
        print("Velocidad actual:", self.velocidad, "km/h")
        print("Encendido:", self.encendido)
        print("Historial de velocidades:", self.historial_velocidades)
        print("--------------------")
        print("")

    def encender(self):
        print("Modelo:", self.modelo)
        print("Variable encendido:", self.encendido)
        if self.encendido == True:
            print("El carro ya está encendido ya puedes trabajar en él.")
        else:
            self.encendido = True
            print("El carro ha sido encendido.")        

        print("--------------------")
        print("")

    def acelerar(self, cantidad):
        if not self.encendido or cantidad <= 0:
            print("El carro está apagado o la cantidad es menor a 0. No se puede acelerar.")
            return
        for i in range(cantidad):
            self.velocidad += 10
            self.historial_velocidades.append(self.velocidad)
            print("Acelerando... Velocidad actual:", self.velocidad)