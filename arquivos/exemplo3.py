import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText


class Tela:
    def __init__(self, master):
        self.janela = master

        self.btn = tk.Button(self.janela, text='Abrir arquivo')
        self.btn.bind('<Button-1>', self.abrir_arquivo)
        self.btn.pack()

        self.sct = ScrolledText(self.janela)
        self.sct.pack()

        self.btn_salvar = tk.Button(self.janela, text='SALVEWWW')
        self.btn_salvar.bind('<Button-1>', self.salvar_arquivo)
        self.btn_salvar.pack()

    def salvar_arquivo(self, event):
        # pegar o conteudo
        linhas = self.sct.get(0.0, tk.END)
        # escolher o local para salvar
        tipos = (('Texto', '.txt'), ('Python', '.py'), ('TODOS', '.*'))
        nome_arquivo = fd.asksaveasfilename(filetypes=tipos)
        # preencher o arquivo
        with open(nome_arquivo, 'w') as arq:
            arq.write(linhas)

    def abrir_arquivo(self, event):
        tipos = (('Texto', '.txt'), ('Python', '.py'), ('Todos', '.*'))
        nome_arquivo = fd.askopenfilename(initialdir="/home/benny.lopes", filetypes=tipos)  # por ser caminho, vai mudar de pc para pc
        mb.showinfo('Informação', nome_arquivo)

        arquivo = fd.askopenfile(filetypes=tipos)
        with open(nome_arquivo, 'r') as arq:  # tambem pode usar arquivo.nome
            for linha in arq:
                self.sct.insert(tk.END, linha)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
