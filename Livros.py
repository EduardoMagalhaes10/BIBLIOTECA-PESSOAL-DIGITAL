class livros:
    __init__(self, titulo, genero, autor, num_paginas):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor  
        self.num_paginas = num_paginas
    
    def cadastrar (self):
        return f"Livro cadastrado: {self.titulo}, Gênero: {self.genero}, Autor: {self.autor}, Número de Páginas: {self.num_paginas}"
