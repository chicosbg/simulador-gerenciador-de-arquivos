from datetime import datetime
import math

"""
    justificativa da encadeada: achei legal, mas o de indices parece mais interessante ;)
"""
class Arquivo():
    id_estatico = 0
    def __init__(self) -> None:
        self.blocos = None
        self.tamanho_blocos = 0
        self.nome = ""
        self.data_criacao = datetime.now()
        self.ref_arquivo = f"arquivos/arquivo{Arquivo.id_estatico}.txt"

        try:
            arquivo = open(self.ref_arquivo, 'w')
            arquivo.close()
        except Exception as e:
            print(str(e))

        Arquivo.id_estatico += 1

    def atualiza_tamanho(self):
        self.tamanho_blocos = math.ceil((os.stat(self.ref_arquivo).st_size) / 512)