import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')

        self.btn1 = ttk.Button(self.janela, text='Botão1', bootstyle=SUCCESS)
        self.btn1.pack(anchor='center')

        self.btn2 = ttk.Button(self.janela, text='Botão2', bootstyle=(INFO, OUTLINE))
        self.btn2.pack(anchor='center')


janela = ttk.Window(themename='vapor')  # tk.Tk()
app = Tela(janela)
janela.mainloop()
