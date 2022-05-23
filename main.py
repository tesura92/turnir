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
        """
        Startuje se Single eliminacija. Prvo proveravamo ako se funkcija startovala samo sa jednim igracem da odma
        izbaci da je on pobedio. Proveramo da li je durgi tip turnira jer se koristi i u Duploj eliminaciji.

        Moramo dodati igrace da bude jednako stepenu dvojke Single eliminacija uparuje ljude sa drugih krajeva zreba,
        delimo igrace u 2 lista,a druga lista okrece unazad.
        npr n=8:   1-8 ; 2-7 ; 3-6 ; 4-5

        :return:
        """
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
        """
        Uzimamo izabrane pobednike i setujemo listu igraca da bude samo sa pobednicima.
        :param window: Prozor u kome se nalaze sve informacije
        :param submitresults: Prosledjujemo dugme "submitresults" kako bi ga unistili kad se klikne
        :param boxes: Lista pobednika
        :return:
        """
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
        """
        Unistavamo prethodni prozor i startujemo ponovo single eliminacujy == rekurzija
        :param window: Prozor u kome se nalaze sve informacije
        :return:
        """
        window.destroy()
        self.start()


class DoubleElimination(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)

    def start(self):
        """
        Igrac turnira ispada tek nakon izgubljena 2 meca.
        Od gubitnika iz Glavnog dela turnira se formira "Gubitnicki zreb" gde pobednik ima sansu da se takmici protiv
        pobednika iz prvog dela turnira ali ga mora pobediti dva puta.
        :return:
        """
        loserbracket = self.player_list
        tournament1 = SingleElimination(self.player_list, self.get_typeoft())
        tournament1.start()
        winner = tournament1.player_list[0]
        loserbracket.pop(loserbracket.index(winner))
        tournament2 = SingleElimination(loserbracket, self.get_typeoft())
        tournament2.start()
        wloser = tournament2.player_list
        tournament3 = SingleElimination([winner, wloser], self.get_typeoft())
        tournament3.start()
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
        """
        Dok traje turnir unose se poeni, na kraju ko ima najvse poena pobedjuje.Prvo proveravamo ako se funkcija
        startovala samo sa jednim igracem da odma izbaci da je on pobedio.

        :return:
        """

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
        """
        Setujemo score i pokrecemo sledecu rundu/ zavrsavamo turnir
        :param window: Prozor u kome se nalaze sve informacije
        :param submitresults: Prosledjujemo dugme "submitresults" kako bi ga unistili kad se klikne
        :param boxes: Lista pobednika
        :return:
        """
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
        """
        :param window: Unistavamo window jer se igra samo 1 runda i izpisujemo pobednika
        """
        window.destroy()
        a = self.score.index(max(self.score))
        self.player_list = self.player_list[a]
        popwinner(self.player_list)


class Swiss(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)
        if len(self.player_list) % 2 == 1:
            self.player_list.append('bye')
        a = len(self.player_list)
        self.drzac = [2 ** i for i in range(10) if len(self.player_list) <= 2 ** i]
        self.duelecheck = np.eye(a)
        self.pointcheck = [0]*a
        self.roundnumber = 0

    def start(self):
        """
        Swiss sistem. Sistem rundi i poena. Broj rundi se igra u odnosu na broj igraca koji je najblizi stepenu dvojke.
        8 igraca 2**3 - 3 runde ; 9-16 igraca 2**4 - 4 runde ;...;
        Zbog potrebe takmicenja mora da postoji paran broj igraca. zbog toga se dodaje "bye".
        Ko dobije da igra protim "bye" dobija automatsku pobedu.
        Pobeda donosi 3 poena, nereseno po 1 poen i gubitak 0 poena
        Drzac nam odredjuje koliko se rundi igra.
        :return:
        """
        if self.roundnumber == self.drzac[0]+1:
            popwinner(self.player_list)
            return

        window = Tk()
        window.geometry('300x600')
        boxes = []

        if self.roundnumber == 0:
            lista1 = self.player_list[:len(self.player_list) // 2]
            lista2 = self.player_list[len(self.player_list) // 2:]
            lista2.reverse()

            for i in range((len(self.player_list)) // 2):
                verus = [lista1[i], lista2[i], 'Tie']
                tlabel = Label(window, text=f'{lista1[i]} VS {lista2[i]}')
                one = self.player_list.index(lista1[i])
                two = self.player_list.index(lista2[i])
                self.duelecheck[one][two] += 1
                tlabel.grid(row=i, column=0, padx=2, pady=2)
                t = ttk.Combobox(window, values=verus)
                t.grid(row=i, column=1, padx=2, pady=2)
                boxes.append(t)
                c = Checkbutton(window, text='Started')
                c.grid(row=i, column=2, padx=2, pady=2)
                submitresults = Button(window, text='Submit Results',
                               command=lambda: self.choice_sel(window, submitresults, boxes, lista1, lista2))
                submitresults.grid(row=((len(self.player_list)) // 2) + 1, column=0)
        else:
            midlist=[]
            for i in reversed(range(self.drzac[0]*3)):
                if i in self.pointcheck:
                    a=self.pointcheck.index(self.pointcheck(i))
                    midlist.append(self.player_list.index(a))
            print(midlist)





        window.mainloop()

    def choice_sel(self, window, submitresults, boxes, lista1, lista2):
        """

        :param window: Prozor u kome se nalaze sve informacije
        :param submitresults: Prosledjujemo dugme "submitresults" kako bi ga unistili kad se klikne
        :param boxes: Lista pobednika
        :param lista1, lista2: liste igraca
        """
        y = (len(self.player_list) // 2) + 1
        if self.roundnumber == 0:
            submitresults.destroy()
            i = 0
            for box in boxes:
                if box.get() == '':
                    return
                if box.get() == 'Tie':
                    one = self.player_list.index(lista1[i])
                    two = self.player_list.index(lista2[i])
                    self.pointcheck[one] += 1
                    self.pointcheck[two] += 1
                else:
                    z = self.player_list.index(box.get())
                    self.pointcheck[z] += 3
                    i += 1
        print(self.pointcheck)

        nextround = Button(window, text='Next Round', command=lambda: self.nextround(window))
        nextround.grid(row=y, column=1)

    def nextround(self, window):
        window.destroy()
        self.roundnumber += 1
        self.start()
        pass


class FreeForAll(Tournament):
    def __init__(self, players, typeoft):
        Tournament.__init__(self, players, typeoft)
        self.score = [0] * len(players)

    def set_score(self, a):
        for i in a:
            z = self.player_list.index(i)
            self.score[z] += 1

    def start(self):
        """
        Svako igra sa svakim.Pravimo listu nula gde dodajemo broj pobeda. Igraci imaju isti index kao i u listi poena.
        Ko ima najvise poena pobedjuje
        :return:
        """
        if len(self.player_list) == 1:
            popwinner(self.player_list)
            return

        window = Tk()
        window.geometry('600x600')
        main_frame = Frame(window)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        boxes = []
        z = 1

        for i in range(len(self.player_list)):
            for y in range(i + 1, len(self.player_list)):
                verus = [self.player_list[i], self.player_list[y]]
                tlabel = Label(second_frame, text=f'{self.player_list[i]} VS {self.player_list[y]}')
                tlabel.grid(row=z, column=0, padx=2, pady=2)
                t = ttk.Combobox(second_frame, values=verus)
                t.grid(row=z, column=1, padx=2, pady=2)
                boxes.append(t)
                c = Checkbutton(second_frame, text='Started')
                c.grid(row=z, column=2, padx=2, pady=2)
                z += 1
        submitresults = Button(second_frame, text='Submit Results',
                               command=lambda: self.choice_sel(boxes, second_frame, submitresults))
        submitresults.grid(row=z, column=0)

    def choice_sel(self, boxes, window, submitresults):
        """
        :param window: Prozor u kome se nalaze sve informacije
        :param submitresults: Prosledjujemo dugme "submitresults" kako bi ga unistili kad se klikne
        :param boxes: Lista pobednika
        :return:
        """
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
        """
        :param window: Unistavamo prozaor i izbacujemo pobednuika
        """
        window.destroy()
        a = self.score.index(max(self.score))
        self.player_list = self.player_list[a]
        popwinner(self.player_list)

        window.mainloop()


def popwinner(player_list):
    """
    Prima pobednika da bi izbacio poruku ko je pobedio
    :param player_list: Pobednik
    :return:
    """
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
    """
    Izbacivanje poruke da nije moguce pokrenuti turnir za ni jednim igracem.
    :return:
    """
    window = Tk()
    window.title('Error massage!')
    window.geometry('400x100')
    msg = Label(window, text="Turnir nije moguce pokrenuti sa 0 igraca!")
    msg.pack()
    okey = Button(window, text='Ok', command=lambda: window.destroy())
    okey.pack()
    window.mainloop()


def turnir(a, window2):
    """
    Primamo tim turnira i pravimo isti.
    :param a: Pretstavlja tip turnira kako bi se pokrenulo odgovarajuci turnir
    :param window2: Prosledjujemo drugi prozor kako bi ga zatvorili da neko ne bi menjao parametre u sred programa/
    :return:
    """
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
    """
    Funkcija za ispisivanje dodatik igraca u window radi pregleda ucesnika
    :param a: ime igraca
    :param window2: window u kome dodajemo igrace kako bi ispisali u istom ime igraca
    """
    listofplayer.append(a.get())
    t = Label(window2, text=a.get())
    t.pack()
    labelista.append(t)


def removep(a):
    """
    Nakon izbora da se neki igrac izbrise dobijamo info objekata u windowu da bi obrisali.
    :param a: Ime igraca
    """
    for i in labelista:
        if i['text'] == a.get():
            listofplayer.pop(listofplayer.index(a.get()))
            labelista.pop(labelista.index(i))
            i.destroy()


def ntournament():
    """
    Ubacivanje i izbacivanje igraca kao i odabil vrste turnira
    :return:
    """
    window2 = Tk()
    window2.title(e_t.get())
    window2.geometry('400x600')

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
