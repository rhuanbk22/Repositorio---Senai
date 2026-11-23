class produto:
    def __init__(self, nome, preço, estoque):
        self.name = nome
        self.preço = preço
        self.estoque = estoque

        p1 = produto("arroz", 5.99, 30)
        p2 = produto("Macarrão", 8.5, 80)

        print(type(p1))
        print(p1)
        print(p1 == p2)



        print(p1.nome)
        print(p1.preço)
        print(p1.estoque)

      def exibir(self):
        print(f"produo: {self.nome}")
        print(f"preço: {self.preço}")
        print(f"Estoque: {self.estoque}")
        print("-" * 80)

p1 = produto("arroz", 5.99, 30)
p2 = produto("Macarrão",  8.5, 80)