class livro:
    def_init_(self, titulo, autor, ano_publicacao, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn
        self.disponivel = true

    def emprestar(self):
        if self.disponivel:
            self.disponivel = false
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não está disponivel para emprestimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = true
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não estava emprestado. ")

def exibir_informacoes(self):
    print
