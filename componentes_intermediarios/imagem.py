import tkinter as tk
from PIL import Image, ImageTk


class Tela:
    def __init__(self, master):
        self.janela = master

        # self.img = tk.PhotoImage(file='rebaixado.png')
        # self.img = self.img.subsample(2, 2)
        # Usando a biblioteca PILLOW
        arquivo = Image.open('hamster.jpg')
        self.img = ImageTk.PhotoImage(arquivo)
        self.lbl = tk.Label(self.janela, image=self.img)
        self.lbl.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
