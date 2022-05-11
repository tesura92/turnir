from tkinter import *
from tkinter import ttk
import datetime as dt


def player(a):
    lista=[]
    lista.append(a)
    print(lista)
def tournament():
    listofplayer = []
    window2=Tk()
    window2.title(e_t.get())
    window2.geometry('600x600')

    vojd2 = Label(window2, text="Unesite igrace:", font=20)
    vojd2.pack(pady=10)

    names = Entry(window2)
    names.pack(pady=10)
    a=names.get()
    addnames=Button(window2, text="Add Player", command=player(a))
    addnames.pack()


    options = ['SingleElimination',
               'DoubleElimination',
               'Leaderboard',
               'Swiss',
               'FreeForAll'
               ]
    vojd1 = Label(window2, text="Izaberite tip turnira:", font=20)
    vojd1.pack()

    typeoft = ttk.Combobox(window2, value=options, font=20)
    typeoft.current(0)
    typeoft.pack()


    window2.mainloop()


root = Tk()
root.title("Turniri")
root.geometry('300x500')

welcome = Label(root, text= '\nDobro dosli! \n Vreme je da organizujemo Vas prvi turnir !\n')
welcome.pack()

date=dt.datetime.now()
format_date=f"{date:%a, %b %d %Y}"
entry=Label(root,text=format_date)
entry.pack()

vojd=Label(root, text='\n Unesite ime turnira:')
vojd.pack()

e_t=Entry(root)
e_t.pack()

newtournament= Button(root, text="Novi Turnir" , command=tournament)
newtournament.pack()

root.mainloop()