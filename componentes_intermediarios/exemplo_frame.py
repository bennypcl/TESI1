import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.frm_left = tk.LabelFrame(self.janela, text='Titulo', labelanchor='nw', bg='black')
        self.frm_left.pack(side=tk.LEFT)
        self.frm_right = tk.Frame(self.janela, bg='blue')
        self.frm_right.pack(side=tk.LEFT)

        self.btn1 = tk.Button(self.frm_left, text='Botão 1')
        self.btn1.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn2 = tk.Button(self.frm_left, text='Botão 2')
        self.btn2.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn3 = tk.Button(self.frm_right, text='Botão 3')
        self.btn3.pack()
        self.btn4 = tk.Button(self.frm_right, text='Botão 4')
        self.btn4.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
