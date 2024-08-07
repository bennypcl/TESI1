import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Escolha')

        dias = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom')
        self.cbx_dias = ttk.Combobox(self.janela, values=dias, state='readonly')
        self.cbx_dias.current(0) # ja mostra um elemento específico da lista de values
        self.cbx_dias.set('Dias da Semana') # deixa algo explicativo mostrando no cbx sem adicioná-lo na lista
        self.cbx_dias.pack()

        self.btn_dias = tk.Button(self.janela, text='Confirmar', command=self.clicou)
        self.btn_dias.pack()

    def clicou(self):
        if self.cbx_dias.get() == 'Dias da Semana':
            messagebox.showwarning('Atenção', 'Escolha um dia da semana!')

        elif self.cbx_dias.get() == 'Sex':
            self.toplevel = tk.Toplevel(self.janela)
            self.toplevel.title('Como é meu chapa?')
            arquivo = Image.open('../componentes_intermediarios/hamster.jpg')
            self.img = ImageTk.PhotoImage(arquivo)
            self.lbl_ham = tk.Label(self.toplevel, image=self.img)
            self.lbl_ham.pack()

        else:
            messagebox.showinfo('Festinha', f'Você escolheu {self.cbx_dias.get()}')


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
