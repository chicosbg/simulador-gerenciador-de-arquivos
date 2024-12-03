from modulos.operacoes_cmd.trata_operacoes_cmd import TratadorComandosCMD

class SO():
    def __init__(self):
        self.diretorios_atual = None
        self.tratador_comandos = TratadorComandosCMD()
        
    def comando_cmd(self, comando: str):
        comando_tratado = comando.split(' ')
        if(comando_tratado[0].lower() == 'cd'):
            dir_atual = self.tratador_comandos.cd(comando, self.diretorios_atual)   
            self.diretorios_atual = dir_atual
        
        if(comando_tratado[0].lower() == 'ls'):
            dirs = self.tratador_comandos.ls(comando, self.diretorios_atual)    
            for diretorio in dirs:
                print(diretorio.nome) 
            
        if(comando_tratado[0].lower() == 'pwd'):
            print(self.tratador_comandos.pwd(comando, self.diretorios_atual))    
             