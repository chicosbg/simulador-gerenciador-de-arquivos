from modulos.operacoes_cmd.trata_operacoes_cmd import TratadorComandosCMD

class SO():
    def __init__(self):
        self.diretorios_atual = None
        self.trador_comandos = TratadorComandosCMD()
        
    def comando_cmd(self, comando: str):
        comando = comando.split(' ')
        if(comando[0].lower() == 'cd'):
            dir_atual = self.trador_comandos.cd(comando, self.diretorios_atual)   
            self.diretorios_atual = dir_atual
        
        if(comando[0].lower() == 'ls'):
            dirs = self.trador_comandos.ls(comando, self.diretorios_atual)    
            for diretorio in dirs:
                print(diretorio.nome) 
            
        if(comando[0].lower() == 'pwd'):
            print(self.trador_comandos.pwd(comando, self.diretorios_atual))    
             