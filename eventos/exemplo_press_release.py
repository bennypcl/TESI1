import tkinter as tk

class Tela:
    def keypress(self, event):  # event é um objeto da classe Event
        self.lbl.config(text=event.char)

    def keyrelease(self, event):
        self.lbl.config(text='')

    def __init__(self, master):
        self.janela = master

        self.btn = tk.Button(self.janela, text='Clique!')
        # Associa o evento ao widget
        self.btn.bind('<KeyPress>', self.keypress)
        self.btn.bind('<KeyRelease>', self.keyrelease)
        self.btn.pack()

        self.lbl = tk.Label(self.janela)
        self.lbl.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
