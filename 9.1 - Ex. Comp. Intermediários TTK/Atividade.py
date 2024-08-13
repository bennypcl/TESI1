import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Ex. Comp. Inter. TTK')
        self.janela.geometry('1000x500')

        # Alteração do ícone da janela
        self.icone = tk.PhotoImage(file='UFAC.png')
        self.janela.wm_iconphoto(False, self.icone)

        self.conta = 0

        # Configuração do Menu
        self.menu_bar = tk.Menu(self.janela)
        self.menu_cadastro = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_informacoes = tk.Menu(self.menu_bar, tearoff=0)

        self.menu_bar.add_cascade(label='Cadastro', menu=self.menu_cadastro)  # label
        self.menu_bar.add_cascade(label='Informações', menu=self.menu_informacoes)  # label

        self.menu_cadastro.add_command(label='Funcionários', command=self.cadastro)
        self.menu_informacoes.add_command(label='Funcionários', command=self.informacoes)

        # Background colorido da tela
        self.lbl1 = tk.Label(self.janela, text='', bg='#0c4da2')
        self.lbl1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.lbl2 = tk.Label(self.janela, text='', bg='#0c4da2')
        self.lbl2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.lbl3 = tk.Label(self.janela, text='', bg='#0c4da2')
        self.lbl3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lbl4 = tk.Label(self.janela, text='', bg='#0c4da2')
        self.lbl4.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        janela.config(menu=self.menu_bar)  # Adiciona o Menu na Janela

        # Configuração do Treeview
        colunas = ('nome', 'nascimento', 'cpf', 'email', 'telefone')

        self.frm_informacoes = tk.Frame(self.janela, padx=10, pady=10)

        self.tvw = ttk.Treeview(self.frm_informacoes, columns=colunas, show='headings', height=5)

        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('nascimento', text='Nascimento')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='E-mail')
        self.tvw.heading('telefone', text='Telefone')

        self.tvw.column('nome', width=200)
        self.tvw.column('nascimento', width=80)
        self.tvw.column('cpf', width=80)
        self.tvw.column('email', width=150)
        self.tvw.column('telefone', width=90)

        self.scr_bar_frm_info = tk.Scrollbar(self.frm_informacoes)

    def cadastro(self):
        self.frm_cadastro = tk.Frame(self.janela)
        self.frm_cadastro.pack(anchor='center', pady=10, padx=10)

        # Titulo
        self.lbl = tk.Label(self.frm_cadastro, text='Cadastro de Funcionário')
        self.lbl.grid(row=0, columnspan=4, pady=10)

        # Componentes Nome
        self.label_nome = tk.Label(self.frm_cadastro, text='Nome: ')
        self.label_nome.grid(row=1, column=0)
        self.ent_nome = tk.Entry(self.frm_cadastro)
        self.ent_nome.grid(row=1, column=1)

        # Componentes Data Nascimento
        self.label_data_nasc = tk.Label(self.frm_cadastro, text='Data Nascimento: ')
        self.label_data_nasc.grid(row=2, column=0)
        self.frm_data = tk.Frame(self.frm_cadastro)
        self.frm_data.grid(row=2, column=1)
        self.sbx_dia_nasc = tk.Spinbox(self.frm_data, width=3, from_=1, to=31, wrap=True, state='readonly')
        self.sbx_dia_nasc.pack(side=tk.LEFT)
        self.sbx_mes_nasc = tk.Spinbox(self.frm_data, width=3, from_=1, to=12, wrap=True, state='readonly')
        self.sbx_mes_nasc.pack(side=tk.LEFT)
        self.ent_ano_nasc = tk.Entry(self.frm_data, width=5)
        self.ent_ano_nasc.pack(side=tk.LEFT)

        # Componentes CPF
        self.label_cpf = tk.Label(self.frm_cadastro, text='CPF: ')
        self.label_cpf.grid(row=3, column=0)
        self.ent_cpf = tk.Entry(self.frm_cadastro, width=12)
        self.ent_cpf.grid(row=3, column=1)

        # Componentes E-mail
        self.label_email = tk.Label(self.frm_cadastro, text='E-mail: ')
        self.label_email.grid(row=4, column=0)
        self.ent_email = tk.Entry(self.frm_cadastro)
        self.ent_email.grid(row=4, column=1)

        # Componentes Telefone
        self.label_tel = tk.Label(self.frm_cadastro, text='Telefone: ')
        self.label_tel.grid(row=5, column=0)
        self.ent_tel = tk.Entry(self.frm_cadastro)
        self.ent_tel.grid(row=5, column=1)

        # Botão Concluir
        self.btn_concluir = tk.Button(self.frm_cadastro, text='Concluir',
                                      background='black',
                                      fg='white',
                                      activebackground='grey',
                                      command=self.concluir)
        self.btn_concluir.grid(row=6, columnspan=4)

    def concluir(self):
        # Gets dos dados de cadastro
        self.nome_fecha = self.ent_nome.get()
        self.nascimento_fecha = f'{self.sbx_dia_nasc.get()}/{self.sbx_mes_nasc.get()}/{self.ent_ano_nasc.get()}'
        self.cpf_fecha = self.ent_cpf.get()
        self.email_fecha = self.ent_email.get()
        self.tel_fecha = self.ent_tel.get()
        self.frm_cadastro.destroy()
        messagebox.showinfo('Sucesso', 'Cadastro feito com sucesso!')

        self.insercao()

    def informacoes(self):
        # if AttributeError(Tela):  # isso não deu certo
        #     messagebox.showwarning('Atenção', 'Tabela vazia, adicione dados para vizualização.')

        self.frm_cadastro.destroy()

        # Faz aparecer o Frame com o TreeView
        self.frm_informacoes.pack(anchor='center')

        # Faz aparecer o Próprio TreeView
        self.tvw.grid(row=0, column=0)

    def insercao(self):
        # Inserção dos dados na tabela
        self.tvw.insert('', self.conta, values=(self.nome_fecha,
                                                self.nascimento_fecha,
                                                self.cpf_fecha,
                                                self.email_fecha,
                                                self.tel_fecha))
        self.conta += 1


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
