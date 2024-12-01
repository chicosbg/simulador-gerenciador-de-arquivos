from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.models.arquivo import Arquivo
from modulos.diretorios.diretorio import Diretorio

from typing import Union, List
class TrataOperacoesCMD():
    def __init__(self) -> None:
        self.gerenciador_diretorios = GerenciadorDiretorios()
    
    def ls(self, comando: str, diretorio_atual) -> List[Union[Diretorio, Arquivo]]:
        comando = comando.split(' ')
        if(comando[0] == 'ls'):
            return self.gerenciador_diretorios.lista_diretorio_atual(raiz=diretorio_atual)
        raise Exception("comando invalido.")

    def pwd(self, comando: str, diretorios_atual) -> str:
        comando = comando.split(' ')
        if(comando[0].lower() == 'pwd'):
            return self.gerenciador_diretorios.path_absoluto_diretorios_atual(diretorios_atual)

        raise Exception("comando invalido.")