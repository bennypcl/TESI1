import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x100')

        lbl1 = tk.Label(self.janela, text='', bg='red')
        lbl1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        lbl2 = tk.Label(self.janela, text='', bg='blue')
        lbl2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        lbl3 = tk.Label(self.janela, text='', bg='white')
        lbl3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
