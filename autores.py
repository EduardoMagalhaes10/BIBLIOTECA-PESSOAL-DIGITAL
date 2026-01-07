class Autores:
    def __init__(self, nome, livros=None, revista=None, genero_livros=None, genero_revista=None):
        self.nome = nome
        self.livros = livros if livros else []
        self.revista = revista
        self.genero_livros = genero_livros
        self.genero_revista = genero_revista
        self.ativo = True

    def cadastrar(self):
        print(f"Autor(a) '{self.nome}' cadastrado(a) com sucesso!")

    def editar(self, novo_nome=None, novo_genero_l=None, novo_genero_r=None):
        if novo_nome: self.nome = novo_nome
        if novo_genero_l: self.genero_livros = novo_genero_l
        if novo_genero_r: self.genero_revista = novo_genero_r
        print(f"Dados de '{self.nome}' atualizados.")

    def remover(self):
        self.ativo = False
        print(f"O perfil de '{self.nome}' foi desativado do sistema.")

    def adotar(self, obra):
        """Simula a adoção de uma obra deste autor por uma instituição ou leitor"""
        print(f"A obra '{obra}' do autor {self.nome} foi oficialmente adotada para leitura.")