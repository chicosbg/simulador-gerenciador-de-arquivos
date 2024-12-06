from typing import List
from modulos.models.arquivo import Arquivo
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo

class Diretorio(Arquivo):
    def __init__(self, console) -> None:
        self.sub_diretorios: List[Diretorio] = [] # uma lista de Diretorio
        self.raiz: Diretorio|None = None # se é None a classe em questão é a raiz, caso contrario passa a classe pai 
        self.arquivos: List[Arquivo] = []
        self.console = console    
    def add_diretorio(self, diretorio):
        for dir in self.sub_diretorios:
            if (dir.nome == diretorio.nome):
                self.console.log("Diretorio presente.") 
                return False

        diretorio.raiz = self
        
        self.sub_diretorios.append(diretorio)
        return True
    
    def add_arquivo(self, arquivo: Arquivo, gerenciador_dispositivo: GerenciadorDispositivo):
        for arq in self.arquivos:
            if (arq.nome == arquivo.nome):
                raise Exception("Arquivo presente.") 
                
        bloco = gerenciador_dispositivo.alocar(arquivo.tamanho_blocos)
        
        self.console.log(gerenciador_dispositivo.disco.blocos_memoria)
        
        if bloco == None:
            raise Exception("Erro ao alocar blocos.")
        
        arquivo.blocos = bloco        
         
        self.arquivos.append(arquivo)    
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome