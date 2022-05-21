import tkinter
from tkinter import *
from tkinter import ttk
import datetime as dt
import random
import math


class Tournament:

    def __init__(self, players, typeoft):
        self.player_list = self.shuffleplayers(players)
        self.__tournament__ = typeoft

    def set_playerlist(self, new_list):
        self.player_list = new_list

    def shuffleplayers(self, players):
        random.shuffle(players)
        random.shuffle(players)
        random.shuffle(players)
        return players


class SingleElimination(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):

        if len(self.player_list) == 1 and self.typeoft == 'SingleElimination':
            popwinner(self.player_list)
            return

        window = Tk()
        window.geometry('300x600')

        drzac = [2 ** i for i in range(10) if len(self.player_list) <= 2 ** i]
        while len(self.player_list) < drzac[0]:
            self.player_list.append('bye')
        if len(self.player_list) == 1:
            return self.player_list
        print(self.player_list)
        lista1 = self.player_list[:len(self.player_list) // 2]
        lista2 = self.player_list[len(self.player_list) // 2:]
        lista2.reverse()
        boxes = []
        for i in range((len(self.player_list)) // 2):
            verus = [lista1[i], lista2[i]]
            tlabel = Label(window, text=f'{lista1[i]} VS {lista2[i]}')
            tlabel.grid(row=i, column=0, padx=2, pady=2)
            t = ttk.Combobox(window, values=verus)
            t.grid(row=i, column=1, padx=2, pady=2)
            boxes.append(t)
        submitresults = Button(window, text='Submit Results',
                               command=lambda: choice_sel(self, boxes, window, submitresults))
        submitresults.grid(row=((len(self.player_list)) // 2) + 1, column=0)

        window.mainloop()

    def nextround(self, window):
        window.destroy()
        self.start()


class DoubleElimination(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):

        gubitnici = self.player_list

        while len(self.player_list) > 1:
            tournament1 = SingleElimination(self.player_list, self.typeoft)
            tournament1.start()

        gubitnici.pop(gubitnici.index(self.player_list))
        listagubitnika = SingleElimination(gubitnici)
        print(f'Unesite broj poena {self.player_list[0]} vs {listagubitnika[0]}')
        a = int(input(f'Uneti broj poena za {self.player_list[0]} : '))
        b = int(input(f'Uneti broj poena za {listagubitnika[0]} : '))
        if a >= b:
            return self.player_list[0]
        else:
            return listagubitnika[0]

        window = Tk()
        window.geometry('300x600')

        window.mainloop()


class Leaderboard(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        """
        print()
        rezultat = []
        for i in range(len(ucesnici)):
            a = int(input(f'Unesti rank {ucesnici[int(i)]}'))
            rezultat.append(a)
        a = rezultat.index(min(rezultat))
        print(f'Pobednik je {ucesnici[a]}')
        """

        window = Tk()
        window.geometry('300x600')

        window.mainloop()


class Swiss(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        """
        a = [2 ** i for i in range(10) if len(ucesnici) <= 2 ** i]
        while len(ucesnici) < a[0]:
            ucesnici.append('bye')
        b = int(math.log(a, 2))
        drzac = [[] * b] * (b + 1)
        drzac[0] = ucesnici
        for i in range(1, b + 1):  # ovde prolazimo kroz runde
            for y in range(0, len(drzac[0]) + 1, 2):
                print(f'Unesite broj poena {drzac[i - 1][y]} vs {drzac[i - 1][y + 1]}')
                a = int(input(f'Uneti broj poena za {drzac[i - 1][y]} : '))
                b = int(input(f'Uneti broj poena za {drzac[i - 1][y + 1]}: '))
                if a >= b:
                    return
                else:
                    return
        """

        window = Tk()
        window.geometry('300x600')

        window.mainloop()


class FreeForAll(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        '''
        drzac = [0] * len(self.player_list)
        for i in range(len(self.player_list)):
            for y in range(i + 1, len(self.player_list)):
                print(f'Unesite broj poena {self.player_list[i]} vs {self.player_list[y]}')
                drzac[i] = drzac[i] + int(input(f'{self.player_list[i]} : '))
                drzac[y] = drzac[y] + int(input(f'{self.player_list[y]} : '))
        
        print(drzac)
        a = drzac.index(max(drzac))
        print(f'Pobednik je {self.player_list[a]} sa {drzac[a]} bodova')
        '''

        window = Tk()
        window.geometry('300x600')

        window.mainloop()


def choice_sel(tournament, boxes, window, submitresults):
    i = (len(tournament.player_list) // 2) + 1
    lista = []
    for box in boxes:
        if box.get() == '':
            return
        lista.append(box.get())
    tournament.set_playerlist(lista)
    submitresults.destroy()
    nextround = Button(window, text='Next Round', command=lambda: tournament.nextround(window))
    nextround.grid(row=i, column=1)
    print(tournament.player_list)


def popwinner(player_list):
    root.destroy()
    window = Tk()
    window.title('Winner!!!')
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
    elif len(listofplayer) == 1:
        window2.destroy()
        popwinner(listofplayer)
        root.destroy()
    typeoft = a.get()
    window2.destroy()
    tournament = None
    if typeoft == 'SingleElimination':
        tournament = SingleElimination(listofplayer, typeoft)

    elif typeoft == 'DoubleElimination':
        tournament = SingleElimination(listofplayer, typeoft)

    elif typeoft == 'Leaderboard':
        tournament = SingleElimination(listofplayer, typeoft)

    elif typeoft == 'Swiss':
        tournament = SingleElimination(listofplayer, typeoft)

    elif typeoft == 'FreeForAll':
        tournament = FreeForAll(listofplayer, typeoft)
    if tournament:
        tournament.start()
    else:
        root.destroy()
        return


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
