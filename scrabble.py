from random import choice


class NazwaError(Exception):
    pass


class UjemnyWynikError(Exception):
    def __init__(self, wynik):
        super().__init__('Wynik nie moze byc ujemny')
        self.wynik = wynik


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


class PulaLiter:
    def __init__(self):
        self._litery = {
            'A': 9,
            'Ą': 1,
            'B': 2,
            'C': 3,
            'Ć': 1,
            'D': 3,
            'E': 7,
            'Ę': 1,
            'F': 1,
            'G': 2,
            'H': 2,
            'I': 8,
            'J': 2,
            'K': 3,
            'L': 3,
            'Ł': 2,
            'M': 3,
            'N': 5,
            'Ń': 1,
            'O': 6,
            'Ó': 1,
            'P': 3,
            'R': 4,
            'S': 4,
            'Ś': 1,
            'T': 3,
            'U': 2,
            'W': 4,
            'Y': 4,
            'Z': 5,
            'Ź': 1,
            'Ż': 1,
            'BLANK': 2
        }

    def litery(self):
        return self._litery

    def wez_litere(self):
        litera = choice(self._litery.keys())
        while self._litery[litera] == 0:
            litera = choice(self._litery.keys())

        self._litery[litera] -= 1
        return litera

    def dodaj_litere(self, litera):
        self._litery[litera] += 1

    def wymien_litere(self):
        pass


class Plansza:
    pass


class Bot(Gracz):
    pass
