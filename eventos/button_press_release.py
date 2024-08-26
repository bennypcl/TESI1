import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='BOTAO')
        self.btn.pack()
        self.btn.bind('<Button-1>', self.press)
        self.btn.bind('<ButtonRelease-1>', self.release)

        self.ent = tk.Entry(self.janela, show='*')
        self.ent.pack()

        self.lbl = tk.Label(self.janela, text='Label')
        self.lbl.pack()

        self.janela.bind_all('<Return>', self.mostrar)

    def mostrar(self, event):
        self.lbl.config(text=self.ent.get())

    def press(self, event):
        self.lbl.config(text='Press')

    def release(self, event):
        self.lbl.config(text='Release')
        self.btn.unbind('<Button-1>')


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
