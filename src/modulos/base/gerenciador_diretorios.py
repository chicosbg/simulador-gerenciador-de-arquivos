from modulos.diretorios.diretorio import Diretorio
from modulos.models.arquivo import Arquivo
from typing import List

class GerenciadorDiretorios():
    def __init__(self) -> None:
        return 
    
    def cria_diretorios(self, nome, raiz: Diretorio|None = None):
        novo_diretorio = Diretorio()
        novo_diretorio.nome = nome
        novo_diretorio.raiz = raiz
        if(raiz):
            raiz.add_diretorio(diretorio=novo_diretorio)
        
    def pesquisa_arquivo(self, raiz: Diretorio, arquivo_pesquisado: Arquivo, caminho_percorrido: List[Diretorio] = []):
        arquivos_diretorios = []

        caminho_percorrido.append(raiz)
        
        for dir in raiz.sub_diretorios:
            arquivos_diretorios_anterior = self.pesquisa_arquivo(dir, arquivo_pesquisado=arquivo_pesquisado, caminho_percorrido=caminho_percorrido) # vai até o final da arvore
            arquivos_diretorios.extend(arquivos_diretorios_anterior)
            
        if(caminho_percorrido[-1] != raiz):
            caminho_percorrido.pop() 
        
        for i,arquivo in enumerate(raiz.arquivos):
            if arquivo.nome == arquivo_pesquisado.nome:
                arquivos_diretorios.append({"nome": arquivo.nome, "posicao_lista_arquivos":i, "caminho_percorrido": caminho_percorrido})
        
        
        return arquivos_diretorios
    
    
    def lista_diretorio_atual(self, raiz: Diretorio):
        diretorios_e_arquivos = []
        diretorios_e_arquivos.extend(raiz.sub_diretorios)
        diretorios_e_arquivos.extend(raiz.arquivos)
        return diretorios_e_arquivos # retorna todos os diretorios e arquivos
    
    def path_absoluto_diretorios_atual(self, diretorio_atual:Diretorio):
        path = []
        dir_atual = diretorio_atual
        path.append(dir_atual)
        while True:
            if(dir_atual.raiz == None): break
            dir_atual = dir_atual.raiz
            
            path.append(dir_atual)
            
        path.reverse()
        path_str = '/'.join(p.nome for p in path)
        return path_str
    
    def caminha_para_diretorios(self, path: str, diretorio_atual: Diretorio) -> Diretorio:
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
                if(dir.get_nome() == dir_atual.get_nome()):
                    dir_atual = dir
                    encontrou_diretorio = True

            if(not encontrou_diretorio):
                raise Exception("Diretorio invalido.")

        return dir_atual
            
            
                
            
            
            
        
        