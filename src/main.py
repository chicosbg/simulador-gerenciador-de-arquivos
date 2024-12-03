from modulos.interface_comando.InterfaceComando import InterfaceComando
from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo
from modulos.base.so import SO

if __name__ == '__main__':
    sistema = SO()
    interface = InterfaceComando()

    while True:
        interface.cmdloop()
        sistema.comando_cmd(interface.comando)