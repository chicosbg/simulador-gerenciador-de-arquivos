import random
class Bloco():
    def __init__(self):
        self.proximo = None
        self.deletado = False  
        self.id = int(round(random.random()), 16)