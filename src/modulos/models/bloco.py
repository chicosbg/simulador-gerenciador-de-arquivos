import time
class Bloco():
    def __init__(self):
        self.proximo = None
        self.deletado = False  
        self.id = time.time_ns() 