class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidad = 0
        self.encendido = False
        self.historial_velocidades = [0]

    def mostrar_estado(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.ano)
        print("Velocidad actual:", self.velocidad)
        print("Encendido:", self.encendido)
        print("Historial de velocidades:", self.historial_velocidades)
        print("--------------------")
        print("")

    def encender(self):
        print("Modelo:", self.modelo)
        print("Estado del carro:", self.encendido)
        if self.encendido == True:
            print("El carro ya está encendido.")
        else:
            self.encendido = True
            print("El carro ha sido encendido.")        

        print("--------------------")
        print("")