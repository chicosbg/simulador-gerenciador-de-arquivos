from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo
from modulos.models.arquivo import Arquivo
from modulos.diretorios.diretorio import Diretorio
from typing import Union, List
import os

class TratadorComandosCMD():
    def __init__(self, gerenciador_dispositivo: GerenciadorDispositivo, console) -> None:
        self.gerenciador_diretorios = GerenciadorDiretorios(gerenciador_dispositivo, console)
        self.gerenciador_dispositivos = gerenciador_dispositivo
        self.console = console
        
    def ls(self, comando: str, diretorio_atual: Diretorio) -> List[Union[Diretorio, Arquivo]]:
        comando = comando.strip().split(' ')
        if(comando[0] == 'ls'):
            if(len(comando) == 2):
                diretorio_atual = self.gerenciador_diretorios.caminha_para_diretorios(comando[1], diretorio_atual)
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

            novo_diretorio = Diretorio(self.console)
            novo_diretorio.set_nome(nome_diretorio)
            if(diretorio_atual != None):
                if(not diretorio_atual.add_diretorio(novo_diretorio)): 
                    return diretorio_atual
            
            self.console.log("diretorio criado!")
            return novo_diretorio
        
        raise Exception("comando invalido.")

    def touch(self, comando: str, diretorio_atual: Diretorio):
        comando = comando.strip().split(" ")
        if(len(comando) == 2):
            nome_arquivo = comando[1]
            self.gerenciador_diretorios.cria_arquivo(nome_arquivo, 4, diretorio_atual)
            self.console.log("Arquivo criado!")
            return

        raise Exception("comando invalido.")

    def rm(self, comando: str, diretorio_atual: Diretorio):
        comando = comando.strip().split(' ') 
        if(len(comando) == 2):
            path_dir = comando[1].replace('\\', '/').split('/')

            if path_dir[-1] != '':
                nome_arquivo = path_dir[-1]
            else:
                nome_arquivo = path_dir[-2]

            path_dir.pop()
            diretorio_atual = self.gerenciador_diretorios.caminha_para_diretorios(path_dir, diretorio_atual)

            if(diretorio_atual != None):
                for i, p in enumerate(diretorio_atual.sub_diretorios):
                    if(p.get_nome() == nome_arquivo):
                        diretorio_atual.sub_diretorios.pop(i)
                        return

                for i, p in enumerate(diretorio_atual.arquivos):
                    if(p.nome == nome_arquivo):
                        self.gerenciador_dispositivos.liberar(p.blocos, p.tamanho_blocos)
                        diretorio_atual.arquivos.pop(i)
                        return
        
            raise Exception("arquivo ou diretório inexistente.")

    def open(self, comando:str, diretorio_atual: Diretorio):
        comando = comando.strip().split(' ') 
        if(len(comando) == 2):
            path_dir = comando[1].replace('\\', '/').split('/')

            if path_dir[-1] != '':
                nome_arquivo = path_dir[-1]
            else:
                nome_arquivo = path_dir[-2]

            path_dir.pop()
            diretorio_atual = self.gerenciador_diretorios.caminha_para_diretorios(path_dir, diretorio_atual)

            if(diretorio_atual != None):
                for i, p in enumerate(diretorio_atual.arquivos):
                    if(p.nome == nome_arquivo):
                        os.system(f"vi {p.ref_arquivo}")
                        return

            raise Exception("arquivo inexistente.")