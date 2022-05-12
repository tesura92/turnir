from tkinter import *
from tkinter import ttk
import datetime as dt
import random
import math


class Tournament:

    def __init__(self,players,typeoftournament):
        self.player_list = players
        self.__tournament_id__ = None
        self.__tournament__ = typeoftournament

    def set_tournament_id(self,a):
        self.__tournament_id__ = a

    def set_tournament(self, a,):
        self.__tournament__ = a

    def tournmanetwindow(self,listofplayer):







def popwinner(player_list):
    window = Tk()
    window.title('Error massage!')
    window.geometry('400x100')
    msg = Label(window, text=f'Pobednik je : {player_list[0]}')
    msg.pack()
    okey = Button(window, text='Ok', command=lambda: window.destroy())
    okey.pack()
    window.mainloop()


def popmsg():
    window = Tk()
    window.title('Error massage!')
    window.geometry('400x100')
    msg = Label(window, text="Turnir nije moguce pokrenuti sa 0 igraca!")
    msg.pack()
    okey = Button(window, text='Ok', command=lambda: window.destroy())
    okey.pack()
    window.mainloop()


def turnir(a, window2):
    if len(listofplayer) < 1:
        popmsg()
    typeoft = a.get()
    window2.destroy()
    random.shuffle(listofplayer)
    random.shuffle(listofplayer)
    random.shuffle(listofplayer)
    print(listofplayer)

    t=Tournament(listofplayer,typeoft)


    if typeoft == "SingleElimination":
        window3 = Tk()
        window3.title('SignleElimination')
        window3.geometry('600x600')


    elif typeoft == "DoubleElimination":
        print('2')

    elif typeoft == "Leaderboard":
        print('3')

    elif typeoft == "Swiss":
        print('4')

    elif typeoft == "FreeForAll":
        print('5')


def player(a, window2):
    listofplayer.append(a.get())
    t = Label(window2, text=a.get())
    t.pack()
    labelista.append(t)


def removep(a):
    for i in labelista:
        if i['text'] == a.get():
            listofplayer.pop(listofplayer.index(a.get()))
            labelista.pop(labelista.index(i))
            i.destroy()


def ntournament():
    window2 = Tk()
    window2.title(e_t.get())
    window2.geometry('600x600')

    vojd2 = Label(window2, text="Unesite igrace:", font=20)
    vojd2.pack(pady=10)

    names = Entry(window2)
    names.pack(pady=10)

    addnames = Button(window2, text="Add Player", command=lambda: player(names, window2))
    addnames.pack()

    deletenames = Button(window2, text="Delete Player", command=lambda: removep(names))
    deletenames.pack()

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

    start = Button(window2, text="Start Tournament", command=lambda: turnir(typeoft, window2))
    start.pack()

    window2.mainloop()


labelista = []
listofplayer = []
root = Tk()
root.title("Turniri")
root.geometry('300x500')

welcome = Label(root, text='\nDobro dosli! \n Vreme je da organizujemo Vas prvi turnir !\n')
welcome.pack()

date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
entry = Label(root, text=format_date)
entry.pack()

vojd = Label(root, text='\n Unesite ime turnira:')
vojd.pack()

e_t = Entry(root)
e_t.pack()

newtournament = Button(root, text="Novi Turnir", command=ntournament)
newtournament.pack()

root.mainloop()
