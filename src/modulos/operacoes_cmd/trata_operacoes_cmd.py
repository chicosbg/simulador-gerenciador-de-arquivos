from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.models.arquivo import Arquivo
from modulos.diretorios.diretorio import Diretorio
from typing import Union, List

class TratadorComandosCMD():
    def __init__(self) -> None:
        self.gerenciador_diretorios = GerenciadorDiretorios()
    
    def ls(self, comando: str, diretorio_atual) -> List[Union[Diretorio, Arquivo]]:
        comando = comando.strip().split(' ')
        if(comando[0] == 'ls'):
            return self.gerenciador_diretorios.lista_diretorio_atual(raiz=diretorio_atual)
        raise Exception("comando invalido.")

    def pwd(self, comando: str, diretorios_atual: Diretorio) -> str:
        comando = comando.strip().split(' ')
        if(comando[0].lower() == 'pwd' and len(comando) == 1):
            return self.gerenciador_diretorios.path_absoluto_diretorios_atual(diretorios_atual)

        raise Exception("comando invalido.")
    
    def cd(self, comando: str, diretorio_atual: Diretorio) -> Diretorio:
        comando = comando.strip().split(' ')
        
        if(comando[0].lower() == 'cd' and len(comando) == 2):
            return self.gerenciador_diretorios.caminha_para_diretorios(comando[1], diretorio_atual)
            
        raise Exception("comando invalido.")

    def mkdir(self, comando: str, diretorio_atual: Diretorio) -> Diretorio:
        comando = comando.strip().split(' ') 
        if(len(comando) == 2):
            path_dir = comando[1].replace('\\', '/').split('/')
            nome_diretorio = path_dir[-1]
            path_dir.pop() # remove o nome do diretorio para não dar ruim
            
            diretorio_atual = self.gerenciador_diretorios.caminha_para_diretorios(path_dir, diretorio_atual)

            novo_diretorio = Diretorio()
            novo_diretorio.set_nome(nome_diretorio)
            if(diretorio_atual != None):
                if(not diretorio_atual.add_diretorio(novo_diretorio)): 
                    return diretorio_atual
            
            print("diretorio criado!")
            return novo_diretorio
        
        raise Exception("comando invalido.")

    def create(self, comando: str, diretorio_atual: Diretorio):
        comando = comando.strip().split(" ")
        if(len(comando) == 3):
            nome_arquivo = comando[1]
            tamanho_em_blocos_arquivo = comando[2]
            self.gerenciador_diretorios.cria_arquivo(nome_arquivo, tamanho_em_blocos_arquivo, diretorio_atual)
        
        raise Exception("comando invalido.")
        