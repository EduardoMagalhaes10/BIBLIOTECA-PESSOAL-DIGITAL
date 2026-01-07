class leitor: 
    def __init__(self, nome=None, l_lidos=None, r_lidos=None, l_alugados=None, r_alugados=None, prazo=None):
        self.nome = nome
        self.l_lidos = l_lidos
        self.r_lidos = r_lidos
        self.l_alugados = l_alugados
        self.r_alugados = r_alugados
        self.prazo = prazo
    
    def cadastrar(self):
        return f"Leitor {self.nome} cadastrado com sucesso!"