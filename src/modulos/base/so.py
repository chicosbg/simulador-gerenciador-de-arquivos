from modulos.operacoes_cmd.trata_operacoes_cmd import TratadorComandosCMD

class SO():
    def __init__(self):
        self.diretorios_atual = None
        self.tratador_comandos = TratadorComandosCMD()
        
    def comando_cmd(self, comando: str):
        comando_tratado = comando.strip().split(' ')
        instrucao_digitada = comando_tratado[0]
        if(instrucao_digitada.lower() == 'cd'):
            dir_atual = self.tratador_comandos.cd(comando, self.diretorios_atual)   
            self.diretorios_atual = dir_atual
        
        if(instrucao_digitada.lower() == 'ls'):
            dirs = self.tratador_comandos.ls(comando, self.diretorios_atual)    
            print('.')
            print('..')
            for diretorio in dirs:
                print(diretorio.nome) 
            
        if(instrucao_digitada.lower() == 'pwd'):
            print(f'/{self.tratador_comandos.pwd(comando, self.diretorios_atual)}')    
             
        if(instrucao_digitada.lower() == 'mkdir'):
            self.diretorios_atual = self.tratador_comandos.mkdir(comando, self.diretorios_atual)
            
    def path_atual(self):
        return f'/{self.tratador_comandos.pwd('pwd', self.diretorios_atual)}'
            