import tkinter as tk


class Tela:
    def mostrar_tecla(self, event):
        self.txt_teclas.insert(tk.END, event.char)

    def limpar_tela(self, event):
        pass

    def __init__(self, master):
        self.janela = master
        self.janela.title('Qualquer tecla')

        self.btn_tecla = tk.Button(text='Precione qualquer tecla')
        self.btn_tecla.bind('<KeyPress>', self.mostrar_tecla)
        self.btn_tecla.pack()

        self.txt_teclas = tk.Text(self.janela)
        self.txt_teclas.pack()

        self.btn_limpar = tk.Button(self.janela, text='Limpar Tela')
        self.btn_limpar.bind('<Button-1>', self.limpar_tela)
        self.btn_limpar.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
