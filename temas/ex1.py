import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Tela:
    def __init__(self, master):
        self.janela = master

        self.frm_central = ttk.Frame(self.janela, padding=5)
        self.frm_central.pack()

        self.lbl_titulo = ttk.Label(self.frm_central, text='Superhero', font=400)
        self.lbl_titulo.pack(side=TOP, anchor=W)

        self.lblfrm = ttk.Labelframe(self.frm_central, text='Alguns widgets do tkinter', padding=5)
        self.lblfrm.pack(side=LEFT, anchor=W, expand=True, fill=BOTH)

        self.lbl = ttk.Label(self.lblfrm, text='Widget Label')
        self.lbl.grid(row=0, column=0)

        self.ent = ttk.Entry(self.lblfrm)
        self.ent.insert('', 'Widget Entry')
        self.ent.grid(row=1, column=0)

        self.spn = ttk.Spinbox(self.lblfrm)
        self.spn.insert('', 'Widget Spinbox')
        self.spn.grid(row=1, column=1)

        self.btn = ttk.Button(self.lblfrm, text='Botão')
        self.btn.grid(row=1, column=2)

        # self.lblfrm_temas = ttk.Labelframe(self.lblfrm, text='Temas do TTk Bootstrap', padding=5)
        # self.lblfrm_temas.grid(row=2, column=0, sticky=)

        self.lbl_teste1 = ttk.Label(self.lblfrm_temas, text='Aqui estarão os radiobuttons.')
        self.lbl_teste1.pack()

        # temas = [i.get() for i in ]
        # for i in temas:


janela = ttk.Window(themename="superhero")
app = Tela(janela)
janela.mainloop()
