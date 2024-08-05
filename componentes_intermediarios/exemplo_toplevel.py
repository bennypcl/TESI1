import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Janela Principal')
        self.janela.geometry('300x200')

        self.frm_left = tk.LabelFrame(self.janela, text='Titulo', labelanchor='nw', bg='black')
        self.frm_left.pack(side=tk.LEFT)
        self.frm_right = tk.Frame(self.janela, bg='blue')
        self.frm_right.pack(side=tk.LEFT)

        self.btn1 = tk.Button(self.frm_left, text='Botão 1', command=self.abrir_janela)
        self.btn1.pack(side=tk.LEFT, padx=10, pady=10)

    def abrir_janela(self):
        # self.janela.withdraw()
        # self.janela.iconify()
        self.toplevel = tk.Toplevel(self.janela)
        self.toplevel.title("Janela Secundária")
        self.toplevel.geometry('250x150')

        self.btn_fechar = tk.Button(self.toplevel, text='Fechar', command=self.fechar_janela)
        self.btn_fechar.pack()
        self.toplevel.grab_set() # trava a tela principal
        self.janela.protocol('WM_DELETE_WINDOW', self.desabilita_fechar)
        self.toplevel.protocol('WM_DELETE_WINDOW', self.fechar_janela)

    def desabilita_fechar(self):
        pass

    def fechar_janela(self):
        self.toplevel.destroy()
        # self.janela.deiconify()
        self.janela.protocol('WM_DELETE_WINDOW', self.janela.destroy)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
