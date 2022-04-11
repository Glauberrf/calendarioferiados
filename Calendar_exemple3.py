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


root = tk.Tk()
def example2():

    #top = tk.Toplevel(root)

    cal = Calendar(root, selectmode='none')
    #date = cal.datetime.today() + cal.timedelta(days=2)
    
    date = cal.datetime(2022,3,29)
    print("DATAS: ",date)
    #cal.calevent_create(date, 'Hello World', 'message')
    #cal.calevent_create(date, 'Reminder 2', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    #cal.calevent_create(date, 'Reminder 1', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
    print(data[0])
    for dia in data:
        print("dia:",int(dia[0:4]),",",int(dia[5]),",",int(dia[7:9]))
        date = cal.datetime(int(dia[0:4]),int(dia[5]),int(dia[7:9]))
        cal.calevent_create(date, 'Reminder 2', 'reminder')
        cal.tag_config('reminder', background='red', foreground='black')

        cal.pack(fill="both", expand=True)
        ttk.Label(root, text=dia[7:9]+"/"+dia[5]+"/"+dia[0:4]).pack()


    #cal.tag_config('reminder', background='red', foreground='pink')

    #cal.pack(fill="both", expand=True)
    #ttk.Label(root, text="Hover over the events.").pack()
    #ttk.Label(root, text="Hover over the events.").pack()



example2()
#ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
#ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)


root.mainloop()