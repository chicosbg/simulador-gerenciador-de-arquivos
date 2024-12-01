from modulos.base.gerenciador_diretorios import GerenciadorDiretorios

class TrataOperacoesCMD():
    def __init__(self) -> None:
        self.gerenciador_diretorios = GerenciadorDiretorios()
    
    def ls(self, comando: str, diretorio_atual):
        comando.split(' ')
        if(comando[0] == 'ls'):
            return self.gerenciador_diretorios.lista_diretorio_atual(raiz=diretorio_atual)
        raise Exception("comando invalido.")

    def pwd(self, comando: str, diretorios_atual):
        