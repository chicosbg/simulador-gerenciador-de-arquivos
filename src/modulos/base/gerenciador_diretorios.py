from modulos.diretorios.diretorio import Diretorio
from modulos.models.arquivo import Arquivo
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo
from typing import List

class GerenciadorDiretorios():
    def __init__(self, gerenciador_dispositivo: GerenciadorDispositivo, console) -> None:
        self.gerenciador_dispositivo = gerenciador_dispositivo
        self.console = console
    
    def cria_arquivo(self, nome: str, tamanho_blocos: int, diretorio_atual: Diretorio):
        novo_arquivo = Arquivo()
        novo_arquivo.nome = nome
        novo_arquivo.tamanho_blocos = tamanho_blocos
        
        diretorio_atual.add_arquivo(novo_arquivo, self.gerenciador_dispositivo)
    
    def cria_diretorios(self, nome, raiz: Diretorio|None = None):
        novo_diretorio = Diretorio(self.console)
        novo_diretorio.nome = nome
        novo_diretorio.raiz = raiz
        
        if(raiz):
            raiz.add_diretorio(diretorio=novo_diretorio)
        # print(self.gerenciador_dispositivo.disco.blocos_memoria)
        return novo_diretorio
    
    def lista_diretorio_atual(self, raiz: Diretorio):
        diretorios = []
        arquivos = []
        diretorios.extend(raiz.sub_diretorios)
        arquivos.extend(raiz.arquivos)
        return (diretorios, arquivos) # retorna todos os diretorios e arquivos
    
    def path_absoluto_diretorios_atual(self, diretorio_atual:Diretorio):
        path = []
        dir_atual = diretorio_atual
        
        path.append(dir_atual.nome)
        while True:
            if(dir_atual.raiz == None):
                break
            
            dir_atual = dir_atual.raiz
            
            path.append(dir_atual.nome)
            
        path.reverse()
        
        path_str = '/'.join(path)
        return path_str
    
    def caminha_para_diretorios(self, path: str|List[str], diretorio_atual: Diretorio) -> Diretorio:
        if(type(path) == str):
            path = path.split('/')

        dir_atual = diretorio_atual
        
        for i, p in enumerate(path):    
            if (p == "." or (p == '' and i == (len(path)-1))):
                continue
            
            if(p == ".."):
                if(dir_atual.raiz == None):
                    continue
                
                dir_atual = dir_atual.raiz
                continue
            
            encontrou_diretorio = False
            for dir in dir_atual.sub_diretorios:
                if(dir.get_nome() == p):
                    dir_atual = dir
                    encontrou_diretorio = True

            if(not encontrou_diretorio):
                raise Exception("Diretorio invalido.")

        return dir_atual