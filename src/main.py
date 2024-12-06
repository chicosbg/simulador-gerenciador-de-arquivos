from modulos.interface_comando.InterfaceComando import InterfaceComando
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo
from modulos.base.so import SO
from rich.console import Console
import time
import signal

def handle_sigint(signum, frame):
        console.log("\nEncerrando sistema...")
        a = console.export_text(clear=True, styles=False)
        
        with open(f"./logs/log{time.time().as_integer_ratio()[0]}.txt", "w", encoding="UTF-8") as file:
             file.write(a)
        exit(0)

if __name__ == '__main__':
    console = Console(record=True)
    sistema = SO(GerenciadorDispositivo(), console)
    interface = InterfaceComando(console)
    sistema.diretorios_atual = sistema.tratador_comandos.mkdir('mkdir raiz', sistema.diretorios_atual)

    signal.signal(signal.SIGINT, handle_sigint)
    
    while True:
        interface.set_diretorio_atual(sistema.path_atual())
        interface.cmdloop()
        try:
            sistema.comando_cmd(interface.comando)
        except Exception as e:
            console.log(f"Erro: {e}")