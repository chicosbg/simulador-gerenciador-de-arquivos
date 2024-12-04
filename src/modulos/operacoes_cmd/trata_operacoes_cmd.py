from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.models.arquivo import Arquivo
from modulos.diretorios.diretorio import Diretorio
from typing import Union, List

class TratadorComandosCMD():
    def __init__(self) -> None:
        self.gerenciador_diretorios = GerenciadorDiretorios()
    
    def ls(self, comando: str, diretorio_atual) -> List[Union[Diretorio, Arquivo]]:
        comando = comando.split(' ')
        if(comando[0] == 'ls'):
            return self.gerenciador_diretorios.lista_diretorio_atual(raiz=diretorio_atual)
        raise Exception("comando invalido.")

    def pwd(self, comando: str, diretorios_atual: Diretorio) -> str:
        comando = comando.split(' ')
        if(comando[0].lower() == 'pwd' and len(comando) == 1):
            return self.gerenciador_diretorios.path_absoluto_diretorios_atual(diretorios_atual)

        raise Exception("comando invalido.")
    
    def cd(self, comando: str, diretorio_atual: Diretorio) -> Diretorio:
        comando = comando.split(' ')
        
        if(comando[0].lower() == 'cd' and len(comando) == 2):
            return self.gerenciador_diretorios.caminha_para_diretorios(comando[1], diretorio_atual)
            
        raise Exception("comando invalido.")

    def mkdir(self, comando: str, diretorio_atual: Diretorio) -> Diretorio:
        comando = comando.split(' ') 
        if(len(comando) == 2):
            nome_diretorio = comando[1].replace('\\', '/').split('/')
            novo_diretorio = Diretorio()
            novo_diretorio.set_nome(nome_diretorio)
            diretorio_atual.add_diretorio(novo_diretorio)
            return 
        
        raise Exception("comando invalido.")

    def create(self, comando: str, diretorio_atual: Diretorio):
        comando = comando.split(" ")
        if(len(comando) == 3):
            nome_arquivo = comando[1]
            tamanho_em_blocos_arquivo = comando[2]
            self.gerenciador_diretorios.cria_arquivo(nome_arquivo, tamanho_em_blocos_arquivo, diretorio_atual)
        
        raise Exception("comando invalido.")
        