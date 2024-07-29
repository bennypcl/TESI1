import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x100')

        lbl1 = tk.Label(self.janela, text='REDDDDDD', bg='red')
        lbl1.grid(row=0, column=0)
        self.janela.columnconfigure(1, weight=1)
        self.janela.columnconfigure(2, weight=2)

        lbl2 = tk.Label(self.janela, text='BLUE', bg='blue')
        lbl2.grid(row=1, column=0, columnspan=3, sticky=tk.EW)

        lbl3 = tk.Label(self.janela, text='GREEN', bg='green')
        lbl3.grid(row=2, column=2)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
