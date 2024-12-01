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
            
        
        for i,arquivo in enumerate(raiz.arquivos):
            if arquivo.nome == arquivo_pesquisado.nome:
                arquivos_diretorios.append({"nome": arquivo.nome, "posicao_lista_arquivos":i, "caminho_percorrido": caminho_percorrido})
        
        
        return arquivos_diretorios
    
    
#