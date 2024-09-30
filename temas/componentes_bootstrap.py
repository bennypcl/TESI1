import ttkbootstrap as ttk
from datetime import datetime


class Tela:
    def __init__(self, master):
        self.janela = master

        self.cbt1 = ttk.Checkbutton(self.janela, text='Bolo', style='success.roundtoggle')
        self.cbt1.pack()

        self.cbt2 = ttk.Checkbutton(self.janela, text='Café', style='danger.squaretoggle')
        self.cbt2.pack()

        dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        self.cbx1 = ttk.Combobox(self.janela, values=dias, style='info')
        self.cbx1.pack()

        self.lbl_date = ttk.Label(self.janela, text='Data:', style='danger')
        self.lbl_date.pack()
        self.den = ttk.DateEntry(self.janela, dateformat='%Y-%m-%d',
                                 firstweekday=0, startdate=datetime(2024, 12, 10),
                                 bootstyle='danger')
        self.den.pack()

        self.meter = ttk.Meter(self.janela, interactive=True, subtext='Velocidade', bootstyle='warning',
                               subtextstyle='danger', stepsize=10, metersize=150)
        self.meter.pack()

        self.fdg = ttk.Floodgauge(self.janela, mode='determinate', value=0, mask='{}% de transferência',
                                  maximum=100,)
        self.fdg.pack()

        self.btn1 = ttk.Button(self.janela, text='Start', style='success', command=self.fdg.start)
        self.btn1.pack()

        self.btn2 = ttk.Button(self.janela, text='Stop', style='danger', command=self.fdg.stop)
        self.btn2.pack()

        self.btn3 = ttk.Button(self.janela, text='Step', style='info', command=self.fdg.step)
        self.btn3.pack()


janela = ttk.Window(themename='solar')
app = Tela(janela)
janela.mainloop()
