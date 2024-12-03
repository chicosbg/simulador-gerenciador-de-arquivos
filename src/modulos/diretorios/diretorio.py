from typing import List
from modulos.models.arquivo import Arquivo

class Diretorio(Arquivo):
    def __init__(self) -> None:
        self.sub_diretorios: List[Diretorio] = [] # uma lista de Diretorio
        self.raiz: Diretorio|None = None # se é None a classe em questão é a raiz, caso contrario passa a classe pai 
        self.arquivos: List[Arquivo] = []
        
    def add_diretorio(self, diretorio):
        for dir in self.sub_diretorios:
            if (dir.nome == diretorio.nome):
                print("Diretorio presente.") 
                return

        diretorio.raiz = self
        
        self.sub_diretorios.append(diretorio)
    
    def get_nome(self):
        return self.nome