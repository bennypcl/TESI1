import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Sistema Bancário')

        self.mnu_barra = tk.Menu(self.janela)
        self.mnu_banco = tk.Menu(self.mnu_barra, tearoff=0)

        # Opções do Menu
        self.mnu_barra.add_cascade(label='Banco', menu=self.mnu_banco)

        # Sub-opções do Banco (Menu)
        self.mnu_banco.add_command(label='Cadastrar', command=self.cadastro_banco)
        self.mnu_banco.add_command(label='Mostrar', command=self.mostra_banco)
        self.mnu_banco.add_command(label='Atualizar', command=self.atualiza_banco)

        # Exibir o menu na janela
        janela.config(menu=self.mnu_barra)

    def cadastro_banco(self):
        # Definição do toplevel
        self.toplevel = tk.Toplevel(self.janela)
        self.toplevel.title('Cadastro de Banco')

        self.lbl_cad_banco = ttk.Label(self.toplevel, text='Cadastro de Banco')
        self.lbl_cad_banco.pack()

        self.frm_cad_banco = ttk.Frame(self.toplevel)
        self.frm_cad_banco.pack(anchor='center')

        self.lbl_nome_banco = ttk.Label(self.frm_cad_banco, text='Nome:')
        self.lbl_nome_banco.grid(row=0, column=0)
        self.ent_nome_banco = ttk.Entry(self.frm_cad_banco)
        self.ent_nome_banco.grid(row=0, column=1)

        self.btn_concluir = ttk.Button(self.frm_cad_banco, text='Concluir')
        self.btn_concluir.grid(row=1, column=0, columnspan=2)

    def mostra_banco(self):
        self.toplevel2 = tk.Toplevel(self.janela)
        self.toplevel2.title('Lista de Bancos')

        colunas = ['numero', 'nome']
        self.tvw_bancos = Treeview(self.toplevel2, show='headings', columns=colunas)
        self.tvw_bancos.pack()

        self.tvw_bancos.heading('numero', text='Numero')
        self.tvw_bancos.heading('nome', text='Nome')

        self.tvw_bancos.column('nome')
        self.tvw_bancos.column('numero')

    def atualiza_banco(self):
        self.toplevel3 = tk.Toplevel(self.janela)
        self.toplevel3.title('Atualização de Banco')
        self.lbl_atu_banco = ttk.Label(self.toplevel3, text='Atualização de Banco')
        self.lbl_atu_banco.pack()

        self.frm_atu_banco = ttk.Frame(self.toplevel3, padding=3)
        self.frm_atu_banco.pack(anchor='center', ipady=3)

        self.lbl_nome_banco = ttk.Label(self.frm_atu_banco, text='Nome:')
        self.lbl_nome_banco.grid(row=0, column=0)
        self.ent_nome_banco = ttk.Combobox(self.frm_atu_banco)
        self.ent_nome_banco.grid(row=0, column=1)

        self.lbl_nome_banco2 = ttk.Label(self.frm_atu_banco, text='Novo:')
        self.lbl_nome_banco2.grid(row=1, column=0)
        self.ent_nome_banco2 = ttk.Entry(self.frm_atu_banco)
        self.ent_nome_banco2.grid(row=1, column=1)

        self.btn_concluir2 = ttk.Button(self.frm_atu_banco, text='Concluir')
        self.btn_concluir2.grid(row=2, column=0, columnspan=2)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
