from modulos.models.bloco import Bloco
class Disco():
    def __init__(self, numero_blocos):
        self.numero_blocos = numero_blocos
        self.numero_blocos_livres = numero_blocos
        self.blocos_memoria = [-1 for i in range(numero_blocos)] #add todos os blocos como livre
        
    def add_bloco(self, bloco):
        posicao_livre = -1 
        
        for i, b in enumerate(self.blocos_memoria):
            if(b == -1):
                posicao_livre = i
                break
        
        if (posicao_livre == -1): 
            return False
        
        self.blocos_memoria.insert(posicao_livre, bloco)
        return True

    def busca_bloco(self, bloco: Bloco):
        for p, b in enumerate(self.blocos_memoria):
            if b == -1: continue
            if(b.id == bloco.id): 
                return (bloco, p)
        
        return None
    
    def remove_bloco(self, bloco):
        bloco_memoria = self.busca_bloco(bloco)
        bloco = bloco_memoria[0]
        posicao = bloco_memoria[1]
        bloco.deletado = True # {nao sei para que vai ser usado isso} 
        
        self.blocos_memoria[posicao] = -1
        
        
