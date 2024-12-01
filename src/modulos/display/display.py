from tkinter import *
from tkinter import ttk


class Display(): 
    def __init__(self) -> None:
        self.root = Tk(screenName="Simulador", className="Simulador de gerenciamento de arquivos")
        self.root.geometry("600x400")
    
    def set_text(self, text, col: int, row: int = 0, handler = None):    
        label = ttk.Label(self.root, text=text)
        label.grid(column=col, row=row)
        
        if handler:
            label.configure(cursor="hand2")
            label.bind("<Button-1>", handler)
        return label
    
    def set_frame(self, w, c=0, r=0, border: str|None = None):
        fram = ttk.Frame(self.root, padding=10)
        fram.grid(column=c, row=r)
        fram.configure(relief=border, width=w)
        return fram
    
    def set_button():
        pass
    
    def run(self):
        self.root.mainloop()
        
def abre_diretorio(display: Display, column = 1, row = 0):
    display.set_frame(60, column, row, "groove")
    display.set_text(f"sub_diretorio{column-1}", col=column+1, row=row, handler=lambda x: abre_diretorio(display=display, column=column+2, row=row))


if __name__ == "__main__":
    d = Display()
    a = [0,1,2,3,4,5]
    for i in a:
        print(d.set_text(f"diretorio_{i}", 0, row=i, handler=lambda event, i=i: abre_diretorio(d, row=i)))
    d.run()    