from tkinter import *
from tkinter import ttk
import datetime as dt
import random
import numpy as np


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

    def get_typeoft(self):
        return self.__tournament__


class SingleElimination(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        if len(self.player_list) == 1 and self.get_typeoft() == 'SingleElimination':
            popwinner(self.player_list)
            return
        elif len(self.player_list) == 1 and self.get_typeoft() == 'DoubleElimination':
            try:
                root.destroy()
            except:
                pass
            return

        window = Tk()
        window.geometry('500x600')
        drzac = [2 ** i for i in range(10) if len(self.player_list) <= 2 ** i]
        while len(self.player_list) < drzac[0]:
            self.player_list.append('bye')
        if len(self.player_list) == 1:
            return self.player_list
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
            c = Checkbutton(window, text='Started')
            c.grid(row=i, column=2, padx=2, pady=2)

        submitresults = Button(window, text='Submit Results',
                               command=lambda: self.choice_sel(window, submitresults, boxes))
        submitresults.grid(row=((len(self.player_list)) // 2) + 1, column=0)
        window.mainloop()

    def choice_sel(self, window, submitresults, boxes):
        i = (len(self.player_list) // 2) + 1
        lista = []
        for box in boxes:
            if box.get() == '':
                return
            lista.append(box.get())
        self.set_playerlist(lista)
        submitresults.destroy()
        nextround = Button(window, text='Next Round', command=lambda: self.nextround(window))
        nextround.grid(row=i, column=1)

    def nextround(self, window):
        window.destroy()
        self.start()


class DoubleElimination(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        loserbracket = self.player_list
        print('stigli123')
        tournament1 = SingleElimination(self.player_list, self.get_typeoft())
        tournament1.start()
        winner = tournament1.player_list[0]
        loserbracket.pop(loserbracket.index(winner))
        print(loserbracket)
        tournament2 = SingleElimination(loserbracket, self.get_typeoft())
        tournament2.start()
        wloser = tournament2.player_list
        tournament3 = SingleElimination([winner, wloser], self.get_typeoft())
        tournament3.start()
        print(tournament3.player_list[0])
        if winner == tournament3.player_list[0]:
            window = Tk()
            window.title('Winner!!!')
            window.geometry('400x100')
            msg = Label(window, text=f'Pobednik je : {winner}')
            msg.pack()
            okey = Button(window, text='Ok', command=lambda: window.destroy())
            okey.pack()
            window.mainloop()
        else:
            tournament4 = SingleElimination([winner, wloser], self.get_typeoft())
            tournament4.start()
            window = Tk()
            window.title('Winner!!!')
            window.geometry('400x100')
            msg = Label(window, text=f'Pobednik je : {tournament4.player_list[0]}')
            msg.pack()
            okey = Button(window, text='Ok', command=lambda: window.destroy())
            okey.pack()
            window.mainloop()


class Leaderboard(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)
        self.score = [0] * len(players)

    def set_score(self, a):
        for i in range(len(self.player_list)):
            self.score[i] = a[i]

    def start(self):

        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        window = Tk()
        window.geometry('300x600')

        boxes = []
        for i in range(len(self.player_list)):
            tlabel = Label(window, text=f'{self.player_list[i]} ')
            tlabel.grid(row=i, column=0, padx=2, pady=2)
            t = Entry(window)
            t.grid(row=i, column=1, padx=2, pady=2)
            boxes.append(t)
            c = Checkbutton(window, text='Started')
            c.grid(row=i, column=2, padx=2, pady=2)
        submitresults = Button(window, text='Submit Results',
                               command=lambda: self.choice_sel(boxes, window, submitresults))
        submitresults.grid(row=len(self.player_list) + 1, column=0)

        window.mainloop()

    def choice_sel(self, boxes, window, submitresults):
        i = len(self.player_list) + 1
        lista = []
        for box in boxes:
            if box.get() == '':
                return
            lista.append(box.get())
        self.set_score(lista)
        submitresults.destroy()
        nextround = Button(window, text='Next Round', command=lambda: self.nextround(window))
        nextround.grid(row=i, column=1)

    def nextround(self, window):
        window.destroy()
        a = self.score.index(max(self.score))
        self.player_list = self.player_list[a]
        popwinner(self.player_list)


class Swiss(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return
        if len(self.player_list) % 2 == 1:
            self.player_list.append('bye')
        drzac = [2 ** i for i in range(10) if len(self.player_list) <= 2 ** i]
        print = np.array(len(self.player_list))
        a = drzac[0] * 3
        pointcheck = np.zer
        print(print)
        print(pointcheck)
        window = Tk()
        window.geometry('300x600')

        window.mainloop()


class FreeForAll(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)
        self.score = [0] * len(players)

    def set_score(self, a):
        for i in a:
            z = self.player_list.index(i)
            self.score[z] += 1

    def start(self):
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        window = Tk()
        window.geometry('300x600')
        boxes = []
        z = 1

        for i in range(len(self.player_list)):
            for y in range(i + 1, len(self.player_list)):
                verus = [self.player_list[i], self.player_list[y]]
                tlabel = Label(window, text=f'{self.player_list[i]} VS {self.player_list[y]}')
                tlabel.grid(row=z, column=0, padx=2, pady=2)
                t = ttk.Combobox(window, values=verus)
                t.grid(row=z, column=1, padx=2, pady=2)
                boxes.append(t)
                c = Checkbutton(window, text='Started')
                c.grid(row=z, column=2, padx=2, pady=2)
                z += 1
        submitresults = Button(window, text='Submit Results',
                               command=lambda: self.choice_sel(boxes, window, submitresults))
        submitresults.grid(row=z, column=0)

    def choice_sel(self, boxes, window, submitresults):
        n = len(self.player_list)
        i = ((n * (n - 1)) // 2) + 1
        lista = []
        for box in boxes:
            if box.get() == '':
                return
            lista.append(box.get())
        self.set_score(lista)
        submitresults.destroy()
        nextround = Button(window, text='Next Round', command=lambda: self.nextround(window))
        nextround.grid(row=i, column=1)

    def nextround(self, window):
        window.destroy()
        a = self.score.index(max(self.score))
        self.player_list = self.player_list[a]
        popwinner(self.player_list)

        window.mainloop()


def popwinner(player_list):
    root.destroy()
    window = Tk()
    window.title('Winner!!!')
    window.geometry('400x100')
    msg = Label(window, text=f'Pobednik je : {player_list}')
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
        tournament = DoubleElimination(listofplayer, typeoft)

    elif typeoft == 'Leaderboard':
        tournament = Leaderboard(listofplayer, typeoft)

    elif typeoft == 'Swiss':
        tournament = Swiss(listofplayer, typeoft)

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

    main_frame = Frame(window2)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    vojd2 = Label(second_frame, text="Unesite igrace:", font=20)
    vojd2.pack(pady=10)

    names = Entry(second_frame)
    names.pack(pady=10)

    addnames = Button(second_frame, text="Add Player", command=lambda: player(names, second_frame))
    addnames.pack(padx=100)

    deletenames = Button(second_frame, text="Delete Player", command=lambda: removep(names))
    deletenames.pack(padx=100)

    options = ['SingleElimination',
               'DoubleElimination',
               'Leaderboard',
               'Swiss',
               'FreeForAll'
               ]
    vojd1 = Label(second_frame, text="Izaberite tip turnira:", font=20)
    vojd1.pack(padx=100)

    typeoft = ttk.Combobox(second_frame, value=options, font=20)
    typeoft.current(0)
    typeoft.pack(padx=100)

    start = Button(second_frame, text="Start Tournament", command=lambda: turnir(typeoft, window2))
    start.pack(padx=100)

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
