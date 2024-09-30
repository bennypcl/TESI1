import tkinter as tk
from tkinter import StringVar, IntVar, Radiobutton, Label, Scale
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Labelframe, Checkbutton

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Tela:
    def __init__(self, master):
       self.janela = master
       self.janela.title("Widgets Legados do Tkinter com TTk Bootstrap")

       self.frm_central = ttk.Frame(self.janela, padding=5)
       self.frm_central.pack()

       self.lbl_titulo = ttk.Label(self.frm_central, text='Teste de Temas', font=400)
       self.lbl_titulo.pack(side=TOP, anchor=W)

       self.lblfrm = ttk.Labelframe(self.frm_central, text='Alguns widgets do tkinter', padding=5)
       self.lblfrm.pack(side=LEFT, anchor=W, expand=True, fill=BOTH)

       self.lbl = ttk.Label(self.lblfrm, text='Widget Label')
       self.lbl.grid(row=0, column=0, sticky='w')

       self.ent = ttk.Entry(self.lblfrm, width=30)
       self.ent.insert('', 'Widget Entry')
       self.ent.grid(row=1, column=0, sticky='w')

       self.spn = ttk.Spinbox(self.lblfrm, width=30)
       self.spn.insert('', 'Widget Spinbox')
       self.spn.grid(row=1, column=0)

       self.btn = ttk.Button(self.lblfrm, text='Botão', width=25)
       self.btn.grid(row=1, column=0, sticky='e')

       # Label Frame Temas ---------------------------------------------------------------------------------------------
       self.lblfrm_temas = ttk.Labelframe(self.lblfrm, text='Temas do TTk Bootstrap', padding=5)
       self.lblfrm_temas.grid(row=2, column=0, sticky="n")

       # self.lbl_teste1 = ttk.Label(self.lblfrm_temas, text='Aqui estarão os radiobuttons.')
       # self.lbl_teste1.pack()

       self.temas = {0:'Morph', 1:'Journal', 2:'Darkly', 3:'Superhero', 4:'Solar', 5:'Cyborg', 6:'Vapor', 7:'Simplex', 8:'Cerculean',
                9:'Cosmo', 10:'Flatly', 11:'Litera', 12:'Minty', 13:'Lumen', 14:'Sandstone', 15:'Yeti', 16:'Pulse', 17:'United'}
       self.tema = IntVar()
       r = 0
       c = 0
       for c, t in self.temas.items():
            self.rbt = ttk.Radiobutton(self.lblfrm_temas, text=t,value=c, variable=self.tema, command=self.select_tema)
            if c < 9:
                self.rbt.grid(row=0, column=c)
                c += 1
            else:
                c -= 10
                self.rbt.grid(row=1, column=c+1)

       # Label Frame dias da semana ------------------------------------------------------------------------------------
       semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
       self.lblfrm_semana = Labelframe(self.lblfrm, text='Widgets Checkbuttons', labelanchor='ne')
       self.lblfrm_semana.grid(row=3, column=0, sticky='n')
       c = 0
       for i in semana:
           self.cbt_semana = Checkbutton(self.lblfrm_semana, text=i, padding=5)
           self.cbt_semana.grid(row=0, column=c)
           c += 1

       # Widget Scale -----------------------------------------------------
       self.lbl_scale = Label(self.lblfrm, text='Widget Scale')
       self.lbl_scale.grid(row=4, sticky='n')

       self.valor_scale = IntVar()
       self.scl = Scale(self.lblfrm, orient='horizontal', length=500, from_=0, to=100, variable=self.valor_scale, command=self.atualiza_scl_v)
       self.scl.grid(row=5, column=0, sticky='n')
       self.scl_v = Label(self.lblfrm)
       self.scl_v['text'] = self.valor_scale.get()
       self.scl_v.grid(row=5, column=0, sticky='e')
       # print(self.scl.get())

       # Widget Text com Scrollbar
       texto = '''The Zen of Python, by Tim Peters
       
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
       '''
       self.lbl_scrtxt = Label(self.lblfrm, text='Widget Text com Scrollbar')
       self.lbl_scrtxt.grid(row=6, sticky='n')
       self.scrtxt = ScrolledText(self.lblfrm, height=5)
       self.scrtxt.insert(tk.END, texto)
       self.scrtxt.grid(row=7)


    def select_tema(self):
        for i, j in self.temas.items():
            if self.tema.get() == i:
                self.janela.style.theme_use(j.lower())
                # self.janela.themename = j
                self.lbl_titulo['text'] = j
                print(j)
        print(self.tema.get())

    def atualiza_scl_v(self, valor):
        self.scl_v['text'] = self.valor_scale.get()

janela = ttk.Window()
app = Tela(janela)
janela.mainloop()

