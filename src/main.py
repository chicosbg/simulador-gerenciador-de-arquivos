from modulos.interface_comando.InterfaceComando import InterfaceComando
from modulos.base.gerenciador_diretorios import GerenciadorDiretorios
from modulos.base.gerenciador_dispositivo import GerenciadorDispositivo
from modulos.base.so import SO

if __name__ == '__main__':
    sistema = SO()
    interface = InterfaceComando()
    sistema.diretorios_atual = sistema.tratador_comandos.mkdir('mkdir raiz', sistema.diretorios_atual)

    while True:
        interface.set_diretorio_atual(sistema.path_atual())
        interface.cmdloop()
        try:
            sistema.comando_cmd(interface.comando)
        except Exception as e:
            print(f"Erro: {e}")