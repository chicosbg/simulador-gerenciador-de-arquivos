import cmd
import os
import time

class InterfaceComando(cmd.Cmd):

    def __init__(self, console):
        super().__init__() # Deve-se iniciar a classe mãe (Cmd)
        self.comando = ""
        self.prompt = 'Sistema de Arquivos - SO []>'
        self.console = console

    def set_diretorio_atual(self, path_dir_atual):
        self.prompt = f'Sistema de Arquivos - SO [{path_dir_atual}]> '

    def do_cd(self, line):
        """ 
            Muda Diretório.
        """
        self.comando = f"cd {line}"
        print(self.comando)
        return True
    
    def do_mkdir(self, line):
        """ 
            Cria Diretório.
        """
        self.comando = f"mkdir {line}"
        print(self.comando)
        return True

    def do_ls(self, line):
        """
            Lista Diretórios.
        """
        self.comando = f"ls {line}"
        print(self.comando)
        return True

    def do_pwd(self, line):
        """
            Informa caminho atual.
        """
        self.comando = f"pwd {line}"
        print(self.comando)
        return True

    def do_touch(self, line):
        """
            Cria arquivo com qualquer extensão
        """
        self.comando = f"touch {line}"
        print(self.comando)
        return True

    def do_rm(self, line):
        """
            Deleta arquivo ou diretório (não é preciso -r).
        """
        self.comando = f"rm {line}"
        print(self.comando)
        return True

    def do_open(self, line):
        """
            Abre um arquivo para visualização e edição.
        """
        self.comando = f"open {line}"
        print(self.comando)
        return True

    def do_status(self, line):
        """
            Exibe informações do sistema de arquivos (ex.: tamanho do disco, espaço livre, estrutura hierarquica).
        """
        self.comando = "status"
        print(self.comando)
        return True

    def do_exit(self, line):
        """
            Encerra simulador.
        """
        self.console.log("\nEncerrando sistema...")
        a = self.console.export_text(clear=True, styles=False)
        
        with open(f"./logs/log{time.time().as_integer_ratio()[0]}.txt", "w", encoding="UTF-8") as file:
             file.write(a)
        exit()
    
    def do_clear(self, line):
        """
            Limpa o terminal.
        """
        os.system("clear")