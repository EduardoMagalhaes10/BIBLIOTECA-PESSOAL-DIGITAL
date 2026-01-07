class Bibliotecario:
    def __init__(self):
        self.livros = []
        self.revistas = []
        self.leitores = []

    def cadastrar(self, lista, item):
        getattr(self, lista).append(item)

    def editar(self, lista, antigo, novo):
        l = getattr(self, lista)
        if antigo in l: l[l.index(antigo)] = novo

    def remover(self, lista, item):
        getattr(self, lista).remove(item)

    def adotar(self, leitor, livro):
        if livro in self.livros and leitor in self.leitores:
            print(f"{leitor} adotou {livro}")