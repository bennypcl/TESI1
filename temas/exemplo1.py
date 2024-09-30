import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, master):
        self.janela = master

        self.ts = ttk.Style() # instância que define os temas
        temas = self.ts.theme_names() # os nomes dos temas
        self.tema = tk.StringVar()
        self.cbx = ttk.Combobox(self.janela, textvariable=self.tema, values=temas)
        self.cbx.pack()
        self.cbx.bind('<<ComboboxSelected>>', self.alterar_tema)
        self.btn = ttk.Button(self.janela, text='Botão')
        self.btn.pack()

    def alterar_tema(self, event):
        self.ts.theme_settings('self.tema.get()', {
            "map": {"TButton": {
                "configure": {"background": 'red'}
            }}
        })

        self.ts.theme_use(self.tema.get())


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
