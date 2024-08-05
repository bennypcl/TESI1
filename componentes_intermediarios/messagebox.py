import tkinter as tk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master

        self.btn = tk.Button(self.janela, text='Abrir',
                             command=self.abrir_mensagem)
        self.btn.pack()

    def abrir_mensagem(self):
        messagebox.showinfo('Informação', 'Você clicou no btn Abrir')
        messagebox.showwarning('Aviso', 'Você foi avisado')
        messagebox.showerror('Erro catastrófico', 'Você errou')
        resposta = messagebox.askquestion('Confirmação', 'Deseja continuar?')
        if resposta == 'yes':
            messagebox.showinfo('confirmou', 'Informação confirmada')
        else:
            self.janela.destroy()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
