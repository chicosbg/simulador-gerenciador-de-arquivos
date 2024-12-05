from datetime import datetime

"""
    justificativa da encadeada: achei legal, mas o de indices parece mais interessante ;)
"""
class Arquivo():
    def __init__(self) -> None:
        self.blocos = None
        self.tamanho_blocos = 0
        self.nome = ""
        self.data_criacao = datetime.now()