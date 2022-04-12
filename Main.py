import tkinter as tk
from sqlalchemy import column
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import Calendar, DateEntry


feriados = []
data = []

data.append("2022,3,05")
data.append("2022,3,10")
data.append("2022,3,15")
data.append("2022,3,29")
data.append("2022,4,25")
data.append("2022,5,03")

feriados.append(data)



labelz = ""
def Janela_Inserir_Feriado():
    janela_inserir_feriado = tk.Toplevel()
    janela_inserir_feriado.title("Inserir feriado")

    label_data_registro = tk.Label(janela_inserir_feriado, text = "Data registro")
    label_data_registro.grid(row=0,column=0)

    label_data_feriado = tk.Label(janela_inserir_feriado, text = "Data feriado")
    label_data_feriado.grid(row=2,column=0)

    label_tipo = tk.Label(janela_inserir_feriado, text = "Tipo")
    label_tipo.grid(row=3,column=0)

    label_cidade = tk.Label(janela_inserir_feriado, text = "Cidade")
    label_cidade.grid(row=4,column=0)
    
    label_motivo = tk.Label(janela_inserir_feriado, text = "Motivo")
    label_motivo.grid(row=5,column=0)

    bt_voltar = tk.Button(janela_inserir_feriado,text ="Fechar", command=janela_inserir_feriado.destroy)
    bt_voltar.grid(row=6,column=0)

    #top = tk.Toplevel(root)

    
    #cal.calevent_create(date, 'Hello World', 'message')
    #cal.calevent_create(date, 'Reminder 2', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    #cal.calevent_create(date, 'Reminder 1', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
    
    



    #cal.tag_config('reminder', background='red', foreground='pink')

    #cal.pack(fill="both", expand=True)
    #ttk.Label(root, text="Hover over the events.").pack()
    #ttk.Label(root, text="Hover over the events.").pack()


janela = tk.Tk()
janela.geometry("800x600")

bt_inserir_feriado = tk.Button(janela, text = "Inserir feriados")
bt_inserir_feriado.grid(row=0,column=0)

cal = Calendar(janela, selectmode='none')

cal.grid(row = 7, column = 0)


#date = cal.datetime.today() + cal.timedelta(days=2)

date = cal.datetime(2022,3,29)

i = 0
for dia in data:
    print("dia:",int(dia[0:4]),",",int(dia[5]),",",int(dia[7:9]))
    date = cal.datetime(int(dia[0:4]),int(dia[5]),int(dia[7:9]))
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.tag_config('reminder', background='red', foreground='black')

    #cal.pack(fill="both", expand=True)
    labelz = ttk.Label(janela, text=dia[7:9]+"/"+dia[5]+"/"+dia[0:4])
    labelz.grid(row = i+10,column = 0)
    i = i + 1



janela.mainloop()