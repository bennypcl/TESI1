import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk


class Tela:
    def __init__(self, master):
        self.janela = master

        self.btn = tk.Button(self.janela, text='Abrir arquivo')
        self.btn.bind('<Button-1>', self.abrir_arquivo)
        self.btn.pack()

        self.lbl = tk.Label(self.janela)

    def abrir_arquivo(self, event):
        tipos = (('JPEG', '.jpg'), ('JPG', '.jpg'), ('PNG', '.png'), ('Todos', '.*'))
        arquivo = fd.askopenfile(filetypes=tipos)

        imagem_caminho = Image.open(arquivo.name)
        imagem_menor = imagem_caminho.reduce(2)
        imagem_tk = ImageTk.PhotoImage(imagem_menor)
        self.lbl.pack()
        self.lbl.config(image=imagem_tk)
        self.lbl.image=imagem_tk


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
