from modulos.operacoes_cmd.trata_operacoes_cmd import TratadorComandosCMD

class SO():
    def __init__(self, gerenciador_dispositivo, console):
        self.diretorios_atual = None
        self.tratador_comandos = TratadorComandosCMD(gerenciador_dispositivo, console)
        self.console = console
    def comando_cmd(self, comando: str):
        comando_tratado = comando.strip().split(' ')
        instrucao_digitada = comando_tratado[0]
        if(instrucao_digitada.lower() == 'cd'):
            dir_atual = self.tratador_comandos.cd(comando, self.diretorios_atual)
            self.diretorios_atual = dir_atual
        
        if(instrucao_digitada.lower() == 'ls'):
            dirs = self.tratador_comandos.ls(comando, self.diretorios_atual)    
            self.console.log('.')
            self.console.log('..')
            for diretorio in dirs:
                self.console.log(diretorio.nome) 
            
        if(instrucao_digitada.lower() == 'pwd'):
            self.console.log(f'/{self.tratador_comandos.pwd(comando, self.diretorios_atual)}')    
             
        if(instrucao_digitada.lower() == 'mkdir'):
            # self.diretorios_atual = self.tratador_comandos.mkdir(comando, self.diretorios_atual)
            self.tratador_comandos.mkdir(comando, self.diretorios_atual)

        if(instrucao_digitada.lower() == 'touch'):
            self.tratador_comandos.touch(comando, self.diretorios_atual)

        if(instrucao_digitada.lower() == 'rm'):
            self.tratador_comandos.rm(comando, self.diretorios_atual)
        
        if(instrucao_digitada.lower() == 'open'):
            self.tratador_comandos.open(comando, self.diretorios_atual)

        if(instrucao_digitada.lower() == 'status'):
            pass
            
    def path_atual(self):
        return f'/{self.tratador_comandos.pwd("pwd", self.diretorios_atual)}'