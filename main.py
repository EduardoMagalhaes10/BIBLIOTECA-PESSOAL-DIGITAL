from src.bibliotecario import Bibliotecario

from src.leitor import leitor

from src.Livros import livros

bibliotecario = Bibliotecario()

livro1 = bibliotecario.cadastrar_livro()

leitor1 = bibliotecario.cadastrar_leitor()

emprestar1 = bibliotecario.emprestar_livro()

listar1 = bibliotecario.listar_cadastros()