from modulos.models.disco import Disco
from modulos.models.bloco import Bloco

class GerenciadorDispositivo():
    def __init__(self):
        self.disco = Disco(150)
        
    def alocar(self, numero_blocos):
        if(numero_blocos > self.disco.numero_blocos_livres):
            raise Exception("Nao ha espaco para alocar o arquivo.")

        self.disco.numero_blocos_livres = self.disco.numero_blocos_livres - numero_blocos

        primeiro_bloco = None
        bloco_atual = None
        for b in range(numero_blocos):
            bloco = Bloco()
            
            if(bloco_atual):
                bloco_atual.proximo = bloco
                
            if(primeiro_bloco == None):
                primeiro_bloco = bloco    

            bloco_atual = bloco
            
            
            if(not self.disco.add_bloco(bloco)):
                raise Exception("Erro ao alocar.")
            
        return primeiro_bloco

    def liberar(self, bloco_inicial: Bloco, numero_blocos: int):
        if(self.disco.busca_bloco(bloco_inicial) == None):
            raise Exception("Arquivo nao alocado corretamente (erro: 0x123)")
        
        self.disco.numero_blocos_livres = self.disco.numero_blocos_livres + numero_blocos

        bloco_atual = bloco_inicial
        for i in range(numero_blocos):
            if(bloco_atual == None): break
            
            self.disco.remove_bloco(bloco_atual)
            bloco_atual = bloco_atual.proximo
            
        print("Blocos removidos da memoria")