from random import shuffle


class NazwaError(Exception):
    pass


class UjemnyWynikError(Exception):
    def __init__(self, wynik):
        super().__init__('Wynik nie moze byc ujemny')
        self.wynik = wynik


class Plytka:
    def __init__(self, litera):
        self._litera = litera.upper()
        litery_wartosci = {
            'A': 1,
            'Ą': 5,
            'B': 3,
            'C': 2,
            'Ć': 6,
            'D': 2,
            'E': 1,
            'Ę': 5,
            'F': 5,
            'G': 3,
            'H': 3,
            'I': 1,
            'J': 3,
            'K': 2,
            'L': 2,
            'Ł': 3,
            'M': 2,
            'N': 1,
            'Ń': 7,
            'O': 1,
            'Ó': 5,
            'P': 2,
            'R': 1,
            'S': 1,
            'Ś': 5,
            'T': 2,
            'U': 3,
            'W': 1,
            'Y': 2,
            'Z': 1,
            'Ź': 9,
            'Ż': 5,
            '#': 0
        }
        self._wartosc = litery_wartosci[self._litera]

    def litera(self):
        return self._litera

    def wartosc(self):
        return self._wartosc


class PulaLiter:
    def __init__(self):
        self._plytki = []
        self.dodaj_poczatkowa_pule_liter()

    def plytki(self):
        return self._plytki

    def dodaj_plytki(self, plytka, ilosc):
        for i in range(ilosc):
            self._plytki.append(plytka)

    def dodaj_poczatkowa_pule_liter(self):
        self.dodaj_plytki(Plytka('A'), 9)
        self.dodaj_plytki(Plytka('Ą'), 1)
        self.dodaj_plytki(Plytka('B'), 2)
        self.dodaj_plytki(Plytka('C'), 3)
        self.dodaj_plytki(Plytka('Ć'), 1)
        self.dodaj_plytki(Plytka('D'), 3)
        self.dodaj_plytki(Plytka('E'), 7)
        self.dodaj_plytki(Plytka('Ę'), 1)
        self.dodaj_plytki(Plytka('F'), 1)
        self.dodaj_plytki(Plytka('G'), 2)
        self.dodaj_plytki(Plytka('H'), 2)
        self.dodaj_plytki(Plytka('I'), 8)
        self.dodaj_plytki(Plytka('J'), 2)
        self.dodaj_plytki(Plytka('K'), 3)
        self.dodaj_plytki(Plytka('L'), 3)
        self.dodaj_plytki(Plytka('Ł'), 2)
        self.dodaj_plytki(Plytka('M'), 3)
        self.dodaj_plytki(Plytka('N'), 5)
        self.dodaj_plytki(Plytka('Ń'), 1)
        self.dodaj_plytki(Plytka('O'), 6)
        self.dodaj_plytki(Plytka('Ó'), 1)
        self.dodaj_plytki(Plytka('P'), 3)
        self.dodaj_plytki(Plytka('R'), 4)
        self.dodaj_plytki(Plytka('S'), 4)
        self.dodaj_plytki(Plytka('Ś'), 1)
        self.dodaj_plytki(Plytka('T'), 3)
        self.dodaj_plytki(Plytka('U'), 2)
        self.dodaj_plytki(Plytka('W'), 4)
        self.dodaj_plytki(Plytka('Y'), 4)
        self.dodaj_plytki(Plytka('Z'), 5)
        self.dodaj_plytki(Plytka('ź'), 1)
        self.dodaj_plytki(Plytka('ż'), 1)
        self.dodaj_plytki(Plytka('#'), 2)
        shuffle(self._plytki)

    def wez_plytke(self):
        return self._plytki.pop()

# class PulaLiter:
#     def __init__(self):
#         self._litery = {
#             'A': 9,
#             'Ą': 1,
#             'B': 2,
#             'C': 3,
#             'Ć': 1,
#             'D': 3,
#             'E': 7,
#             'Ę': 1,
#             'F': 1,
#             'G': 2,
#             'H': 2,
#             'I': 8,
#             'J': 2,
#             'K': 3,
#             'L': 3,
#             'Ł': 2,
#             'M': 3,
#             'N': 5,
#             'Ń': 1,
#             'O': 6,
#             'Ó': 1,
#             'P': 3,
#             'R': 4,
#             'S': 4,
#             'Ś': 1,
#             'T': 3,
#             'U': 2,
#             'W': 4,
#             'Y': 4,
#             'Z': 5,
#             'Ź': 1,
#             'Ż': 1,
#             'BLANK': 2
#         }

#     def litery(self):
#         return self._litery

#     def wez_litere(self):
#         litera = choice(self._litery.keys())
#         while self._litery[litera] == 0:
#             litera = choice(self._litery.keys())

#         self._litery[litera] -= 1
#         return litera

#     def dodaj_litere(self, litera):
#         self._litery[litera] += 1

#     def wymien_litere(self):
#         pass


class Stojak:
    def __init__(self, pula_liter):
        self._plytki = []
        # for i in range(7):
        #     self._plytki.append(pula_liter.wez_plytke())
        self.uzupelnij_stojak(pula_liter)

    def __str__(self):
        str = ''
        for plytka in self._plytki:
            str += plytka.litera()
            str += ', '
        return str[:-2]

    def plytki(self):
        return self._plytki

    def dodaj_plytke_z_puli(self, pula):
        if self.ilosc_plytek() < 7:
            self._plytki.append(pula.wez_plytke())

    def dodaj_plytke(self, plytka):
        if self.ilosc_plytek() < 7:
            self._plytki.append(plytka)

    def wez_plytke(self, plytka):
        if plytka in self._plytki:
            self._plytki.remove(plytka)
            # return plytka

    def ilosc_plytek(self):
        return len(self._plytki)

    def uzupelnij_stojak(self, pula):
        while self.ilosc_plytek() < 7:
            self.dodaj_plytke_z_puli(pula)


class Gracz:
    def __init__(self, nazwa, uklad_liter=None, wynik=0):
        if not nazwa:
            raise NazwaError('Nazwa nie moze byc pusta')
        self._nazwa = nazwa
        self._uklad_liter = uklad_liter if uklad_liter else []
        if wynik < 0:
            raise UjemnyWynikError
        self._wynik = wynik

    def nazwa(self):
        return self._nazwa

    def set_nazwa(self, nowa_nazwa):
        if not nowa_nazwa:
            raise NazwaError('Nazwa nie moze byc pusta')
        self._nazwa = nowa_nazwa

    def uklad_liter(self):
        return self._uklad_liter

    def set_uklad_liter(self, nowy_uklad_liter):
        self._uklad_liter = nowy_uklad_liter

    def wynik(self):
        return self._wynik

    def set_wynik(self, nowy_wynik):
        if nowy_wynik < 0:
            raise UjemnyWynikError
        self._wynik = nowy_wynik

    def oblicz_wynik(self):
        pass


class Plansza:
    pass


class Slowo:
    pass


class Bot(Gracz):
    pass
