import cmd
import os

class InterfaceComando(cmd.Cmd):
    prompt = 'Sistema de Arquivos - SO> '

    def __init__(self):
        super().__init__() # Deve-se iniciar a classe mãe (Cmd)
        self.comando = ""

    def do_cd(self, line):
        """ 
            Muda Diretório
        """
        self.comando = f"cd {line}"
        print(self.comando)
        return True
    
    def do_mkdir(self, line):
        """ 
            Cria Diretório
        """
        self.comando = f"mkdir {line}"
        print(self.comando)
        return True

    def do_ls(self, line):
        """
            Lista Diretórios
        """
        self.comando = f"ls {line}"
        print(self.comando)
        return True

    def do_pwd(self, line):
        """
            Informa caminho atual
        """
        self.comando = f"pwd {line}"
        print(self.comando)
        return True

    def do_exit(self, line):
        """
            Encerra
        """
        return True
    
    def do_clear(self, line):
        """
            Limpa o terminal
        """
        os.system("clear")