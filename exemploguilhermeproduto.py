
class produto:
    def __init__(self, nome, categoria, preco, estoque):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R$ {self.preco}")
        print(f"Quantidade em estoque: {self.estoque}")

    def valor_total(self):
        return self.preco * self.estoque

    def aplicar_desconto(self, percentual):
        self.preco *= (1 - percentual / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preco:.2f}")

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente!")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} x {self.nome}.")
            print(f"Estoque restante: {self.estoque}")

    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Novo estoque: {self.estoque}")


p1 = produto("Fubá", "Alimentos", 2.99, 20)
p2 = produto("Caneta", "Papelaria", 1.99, 30)

p1.exibir_informacoes()
p2.exibir_informacoes()

p1.vender(5)
