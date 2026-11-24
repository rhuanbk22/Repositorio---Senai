
class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        print(f"O veículo {self.marca} está se movendo.")


class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas

    def mover(self):
        print(f"O carro {self.marca} está andando a até {self.velocidade_max} km/h.")
        print(f"Possui {self.num_portas} portas.")


class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas

    def mover(self):
        print(f"A bicicleta {self.marca} está pedalando.")
        print(f"Possui {self.num_marchas} marchas.")



carro1 = Carro("Toyota", 180, 4)
bicicleta1 = Bicicleta("Caloi", 40, 21)


carro1.mover()
print("-------------------")
bicicleta1.mover()
