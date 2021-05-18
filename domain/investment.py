class Investment:
    def __init__(self, username: str, corretora: str, codigo: str, valor_medio: float, quantidade: int, tipo: str):
        self.username = username
        self.corretora = corretora
        self.codigo = codigo
        self.valor_medio = valor_medio
        self.quantidade = quantidade
        self.tipo = tipo

