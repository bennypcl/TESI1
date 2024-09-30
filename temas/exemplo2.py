import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.temas = self.janela.pixmap_themes
        self.tema = tk.StringVar()
        self.cbx = ttk.Combobox(self.janela, textvariable=self.tema, values=self.temas)
        self.cbx.pack()
        self.cbx.bind('<<ComboboxSelected>>', self.alterar_tema)
        self.btn = ttk.Button(self.janela, text='Botão')
        self.btn.pack()

    def alterar_tema(self, event):
        self.janela.set_theme(self.tema.get())


janela = ThemedTk(theme='black')#.tk.Tk()
app = Tela(janela)
janela.mainloop()
