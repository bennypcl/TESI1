# CORRIGIDO!
import tkinter as tk
import datetime


class Tela:
    def __init__(self, master):
        self.janela = master

        self.nome_lbl = tk.Label(self.janela, text='Nome: ')
        self.nome_lbl.pack()
        self.nome_ent = tk.Entry(self.janela)
        self.nome_ent.pack()

        self.data_nsc = tk.Label(self.janela, text='Data de nascimento: ')
        self.data_nsc.pack()
        # Dia
        self.dia = tk.IntVar()
        self.dia_spn = tk.Spinbox(self.janela, from_=1, to=31, wrap=True, width=2, textvariable=self.dia)
        self.dia_spn.pack()
        # Mês
        self.mes = tk.IntVar()
        self.mes_scl = tk.Scale(self.janela, from_=1, to=12, orient='horizontal')
        self.mes_scl.pack()
        # Ano
        self.ano = tk.StringVar()
        self.ano_ent = tk.Entry(self.janela, width=4, textvariable=self.ano)
        self.ano_ent.pack()

        self.btn_calcular = tk.Button(self.janela, text='Calcular Idade', command=self.calc_idade)
        self.btn_calcular.pack()
        self.lbl_idade = tk.Label(self.janela)
        self.lbl_idade.pack()

    def calc_idade(self):
        dia_nasc = self.dia.get()
        mes_nasc = self.mes.get()
        ano_nasc = int(self.ano.get())
        hoje = datetime.date.today()
        diff_dias = hoje.day - dia_nasc
        diff_meses = hoje.month - mes_nasc
        diff_anos = hoje.year - ano_nasc
        if diff_dias < 0:
            diff_dias = diff_dias + 31
            diff_meses = diff_meses - 1
        if diff_meses < 0:
            diff_meses = diff_meses + 12
            diff_anos = diff_anos - 1
        total = diff_anos * 365 + diff_meses * 12 + diff_dias
        resultado = f'Idade: {diff_anos} anos, {diff_meses} meses e {diff_dias} dias ou {total} dias.'
        self.lbl_idade.config(text=resultado)


janela = tk.Tk()
janela.title('Exercício Componentes Básicos 1')
janela.minsize(400, 100)
app = Tela(janela)
janela.mainloop()
