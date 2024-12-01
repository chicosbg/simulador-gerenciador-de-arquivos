from datetime import datetime

"""
    justificativa da encadeada: achei legal, mas o de indices parece mais interessante ;)
"""
class Arquivo():
    def __init__(self) -> None:
        self.blocos = [{"id": 0, "posicao_alocado_disco": 0, "posicao_proximo_disco": 0}, {"id":2, "posicao_alocado_disco": 0, "posicao_proximo_disco": 0}]
        self.nome = "??"
        self.atributos = {"??":"??"}
        self.tipo = "??"
        self.metodo_acesso = "??"
        self.operacoes = "??"
        self.tamanho_bytes = 0
        self.data_criacao = datetime.now()
        