import tkinter as tk

class Tela:
    def clicou(self, event):  # event é um objeto da classe Event
        self.lbl.config(text='clicou')

    def log(self, event):
        print(event)

    def controlv(self, event):
        print('colou')

    def __init__(self, master):
        self.janela = master

        self.btn = tk.Button(self.janela, text='Clique!')
        # Associa o evento ao widget
        self.btn.bind('<Return>', self.clicou)
        self.btn.bind('<Button-1>', self.clicou)
        self.btn.bind('<Key>', self.log)
        self.btn.bind('<Control-v>', self.controlv)
        self.btn.pack()

        self.lbl = tk.Label(self.janela)
        self.lbl.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
