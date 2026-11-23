class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")



carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Honda", "Civic", 2021)

carro1.exibir()
carro2.exibir()