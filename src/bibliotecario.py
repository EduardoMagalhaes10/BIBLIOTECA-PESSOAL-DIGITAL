from src.leitor import leitor

from src.Livros import livros

class Bibliotecario:
    def __init__(self, livros=None, revistas=None, leitor=None):
        self.livros = []
        self.revistas = []
        self.leitor = []
    
    def cadastrar_livro(self):
        print("--- Cadastro de Livro ---")
        titulo = input("Digite o título do livro: ")
        genero = input("Digite o gênero do livro: ")
        autor = input("Digite o autor do livro: ")
        num_paginas = input("Digite o número de páginas do livro: ")

        novo_livro = livros(titulo, genero, autor, num_paginas)
        self.livros.append(novo_livro)
        print(f"Livro {titulo} cadastrado com sucesso!")
        return novo_livro

    def cadastrar_leitor(self):
        print("--- Cadastro de Leitor ---")
        nome = input("Digite o nome do Leitor: ")
        endereco = input("Digite o endereço do Leitor: ")

        if nome in self.leitor:
            print(f"O leitor {nome} já está cadastrado.")
            return

        novo_leitor = leitor(nome, endereco)
        self.leitor.append(novo_leitor)
        print(f"Leitor {nome} cadastrado com sucesso!")
        return novo_leitor
    
    def emprestar_livro(self):
        print("\n--- Registrar Empréstimo ---")
        nome_leitor = input("Nome do leitor: ")
        titulo_livro = input("Título do livro: ")

        # 1. Buscar o objeto leitor na lista
        leitor_encontrado = None
        for l in self.leitor:
            if l.nome.lower() == nome_leitor.lower():
                leitor_encontrado = l
                break

        # 2. Buscar o objeto livro na lista
        livro_encontrado = None
        for b in self.livros:
            if b.titulo.lower() == titulo_livro.lower():
                livro_encontrado = b
                break

        # 3. Validar e Relacionar
        if leitor_encontrado and livro_encontrado:
            # Atribuímos o objeto livro diretamente ao atributo do leitor
            leitor_encontrado.livro = livro_encontrado.titulo
            print(
                f"Sucesso: O livro '{livro_encontrado.titulo}' foi emprestado para {leitor_encontrado.nome}.")
        else:
            print("Erro: Leitor ou Livro não encontrado no sistema!")

    def listar_cadastros(self):
        print("\n" + "="*40)
        print("       RELATÓRIO DA BIBLIOTECA")
        print("="*40)

        # Listagem de Livros
        print("\n--- LIVROS EM ACERVO ---")
        if not self.livros:
            print("Nenhum livro cadastrado no momento.")
        else:
            for i, livro in enumerate(self.livros, 1):
                print(
                    f"{i}. Título: {livro.titulo} | Autor: {livro.autor} | Gênero: {livro.genero}")

        # Listagem de Leitores
        print("\n--- LEITORES CADASTRADOS ---")
        if not self.leitor:
            print("Nenhum leitor cadastrado no momento.")
        else:
            for i, l in enumerate(self.leitor, 1):
                # Verifica se o leitor tem um livro (baseado na sua def emprestar_livro)
                posse = l.livro if hasattr(
                    l, 'livro') and l.livro else "Nenhum"
                print(
                    f"{i}. Nome: {l.nome} | Endereço: {l.endereco} | Livro atual: {posse}")

        print("\n" + "="*40)
