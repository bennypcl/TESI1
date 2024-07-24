import tkinter as tk


class Tela:
    def clicou(self):
        self.lbl_clicou = tk.Label(self.janela, text='Clicou')
        self.lbl_clicou.pack()

    def __init__(self, master):
        self.janela = master
        self.lbl_usuario = tk.Label(self.janela, text='Nome Usuário:',
                                 # bg='grey',
                                 # fg='black',
                                 # font=('Ubuntu', 24, 'bold'),
                                 # padx=20,
                                 # pady=50,
                                 # width=100,
                                 # height=3,
                                 )
        self.lbl_usuario.pack()
        self.ent_usuario = tk.Entry(self.janela)
        self.ent_usuario.pack()
        self.lbl_senha = tk.Label(self.janela, text='Senha:')
        self.lbl_senha.pack()
        self.ent_senha = tk.Entry(self.janela)
        self.ent_senha.pack()
        self.btn_acessar = tk.Button(self.janela, text='Login', command=self.clicou, font=('Ubuntu', 10, 'italic'),
                                     bg='cyan', fg='black')
        self.btn_acessar.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
