from random import shuffle


class NazwaError(Exception):
    pass


class UjemnyWynikError(Exception):
    def __init__(self, wynik):
        super().__init__('Wynik nie moze byc ujemny')
        self.wynik = wynik


class UjemnePunktyError(Exception):
    def __init__(self, punkty):
        super().__init__('Punkty nie moga byc ujemne')
        self.punkty = punkty


class NieZnalezionoPlikuSlownikError(FileNotFoundError):
    pass


class BrakDostepuError(PermissionError):
    pass


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
        # self.dodaj_plytki(Plytka('#'), 2)
        shuffle(self._plytki)

    def wez_plytke(self):
        # if self._plytki:
        return self._plytki.pop()


class Stojak:
    def __init__(self, pula_liter):
        self._plytki = []
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
    def __init__(self, nazwa, pula_liter, wynik=0):
        if not nazwa:
            raise NazwaError('Nazwa nie moze byc pusta')
        self._nazwa = nazwa
        if wynik < 0:
            raise UjemnyWynikError(wynik)
        self._wynik = wynik
        if not pula_liter:
            raise ValueError('Nalezy podac pule liter')
        self._stojak = Stojak(pula_liter)

    def nazwa(self):
        return self._nazwa

    def set_nazwa(self, nowa_nazwa):
        if not nowa_nazwa:
            raise NazwaError('Nazwa nie moze byc pusta')
        self._nazwa = nowa_nazwa

    def stojak(self):
        return self._stojak

    def set_stojak(self, nowy_stojak):
        self._stojak = nowy_stojak

    def wynik(self):
        return self._wynik

    def set_wynik(self, nowy_wynik):
        if nowy_wynik < 0:
            raise UjemnyWynikError(nowy_wynik)
        self._wynik = nowy_wynik

    def dodaj_do_wyniku(self, punkty):
        if punkty < 0:
            raise UjemnePunktyError(punkty)
        else:
            self._wynik += punkty

    def oblicz_wynik(self):
        pass


class Bot(Gracz):
    def __init__(self, nazwa, pula_liter, wynik=0):
        super().__init__(nazwa, pula_liter, wynik)
        slowa_punkty = {}
        try:
            with open('slowa.txt', 'r') as handle:
                for slowo in handle:
                    slowo = slowo.rstrip('\n')
                    if len(slowo) <= 5 and 'x' not in slowo and 'v' not in slowo:
                        punkty = 0
                        slowo = slowo.upper()
                        for litera in slowo:
                            punkty += Plytka(litera)._wartosc
                        slowa_punkty[slowo] = punkty
        except FileNotFoundError:
            raise NieZnalezionoPlikuSlownikError('Brak pliku slownik.txt')
        except PermissionError:
            raise BrakDostepuError('Nie mozna odczytac pliku (brak dostepu)')

        posortowane_punkty = sorted(slowa_punkty.items(), key=lambda x:x[1], reverse=True)
        slowa_punkty = dict(posortowane_punkty)
        self._slownik_punkty = slowa_punkty

    def slowa_mozliwe_do_utworzenia(self):
        slownik = []
        try:
            with open('slowa.txt', 'r') as handle:
                for slowo in handle:
                    slowo = slowo.rstrip('\n')
                    if len(slowo) <= 5:
                        slownik.append(slowo)
        except FileNotFoundError:
            raise NieZnalezionoPlikuSlownikError('Brak pliku slownik.txt')
        except PermissionError:
            raise BrakDostepuError('Nie mozna odczytac pliku (brak dostepu)')

        slowa_mozliwe_do_utworzenia = []
        zgodne_litery = 0
        for slowo in slownik:
            for litera in slowo:
                litera = litera.upper()
                if litera not in str(self._stojak) or slowo.count(litera) > str(self._stojak).count(litera):
                    continue
                else:
                    zgodne_litery += 1
            if zgodne_litery == len(slowo):
                slowo = slowo.upper()
                slowa_mozliwe_do_utworzenia.append(slowo)
            zgodne_litery = 0
        return slowa_mozliwe_do_utworzenia

    def dodaj_punkty_do_slow(self, slowa_mozliwe_do_utworzenia):
        slowa_punkty = {}
        for slowo in slowa_mozliwe_do_utworzenia:
            punkty = 0
            for litera in slowo:
                punkty += Plytka(litera)._wartosc
            slowa_punkty[slowo] = punkty
        posortowane_punkty = sorted(slowa_punkty.items(), key=lambda x:x[1], reverse=True)
        slowa_punkty = dict(posortowane_punkty)
        return slowa_punkty

    def slowa_do_dodania(self):
        slowa_mozliwe_do_utworzenia = {}
        zgodne_litery = 0
        for slowo in self._slownik_punkty.keys():
            for litera in slowo:
                litera = litera.upper()
                if litera not in str(self._stojak) or slowo.count(litera) > str(self._stojak).count(litera):
                    continue
                else:
                    zgodne_litery += 1
            if zgodne_litery == len(slowo):
                slowo = slowo.upper()
                slowa_mozliwe_do_utworzenia[slowo] = self._slownik_punkty[slowo]
            zgodne_litery = 0
        return slowa_mozliwe_do_utworzenia

    def dodaj_slowo(self, plansza, pula_liter, numer_rundy, pominiete_tury, gracze):
        # slowa = self.slowa_mozliwe_do_utworzenia()
        # slowa_punkty = self.dodaj_punkty_do_slow(slowa)
        slowa_mozliwe_do_dodania = self.slowa_do_dodania().keys()
        wiersz_numer = 0
        kolumna_numer = 0
        for slowo in slowa_mozliwe_do_dodania:
            for wiersz in plansza._plansza:
                wiersz_numer += 1
                for litera in wiersz:
                    kolumna_numer += 1
                    # litera = litera.strip()
                    litera = litera[1:-1]
                    if litera in slowo:
                        wspolrzedne = (wiersz_numer-1, kolumna_numer-1-slowo.index(litera))
                        kierunek = 'prawo'
                        slowo_do_dodania = Slowo(self, plansza, numer_rundy, gracze, slowo, wspolrzedne, kierunek)
                        if slowo_do_dodania.sprawdz_slowo() is True:
                            return slowo, wspolrzedne, kierunek, self, pula_liter
                        else:
                            wspolrzedne = (wiersz_numer-1-slowo.index(litera), kolumna_numer-1)
                            kierunek = 'dol'
                            slowo_do_dodania = Slowo(self, plansza, numer_rundy, gracze, slowo, wspolrzedne, kierunek)
                            if slowo_do_dodania.sprawdz_slowo() is True:
                                return slowo, wspolrzedne, kierunek, self, pula_liter
                kolumna_numer = 0
            wiersz_numer = 0
        return '', (0, 0), 'dol', self, pula_liter


class Plansza:
    def __init__(self):
        self._plansza = [["   " for i in range(15)] for j in range(15)]
        self._plansza[7][7] = " * "

    def __str__(self):
        plansza_str = '      '
        for kolumna_cyfra in range(10):
            plansza_str += str(kolumna_cyfra)
            plansza_str += '     '
        for kolumna_cyfra in range(10, 15):
            plansza_str += str(kolumna_cyfra)
            plansza_str += '    '
        plansza_str += '\n   |-----------------------------------------------------------------------------------------|\n'

        plansza = self._plansza
        for wiersz_cyfra in range(len(plansza)):
            plansza_str += str(wiersz_cyfra)
            if wiersz_cyfra < 10:
                plansza_str += '  | '
            else:
                plansza_str += ' | '

            for letter in plansza[wiersz_cyfra]:
                plansza_str += letter
                plansza_str += ' | '
            plansza_str += '\n   |-----------------------------------------------------------------------------------------|\n'

        return plansza_str

    def plansza(self):
        return self._plansza

    def dodaj_slowo(self, slowo, wspolrzedne, kierunek, gracz, pula):
        kierunek = kierunek.lower()
        slowo = slowo.upper()

        potrzebne_plytki = ''
        litery_na_planszy = litery_z_planszy(slowo, kierunek, self, wspolrzedne)
        for i in range(len(slowo)):
            if litery_na_planszy[i] == ' ':
                potrzebne_plytki += slowo[i]

        for litera in potrzebne_plytki:
            for plytka in gracz._stojak._plytki:
                if plytka._litera == litera:
                    gracz._stojak.wez_plytke(plytka)
                    break
        gracz._stojak.uzupelnij_stojak(pula)

        if kierunek == 'prawo':
            for i in range(len(slowo)):
                self._plansza[wspolrzedne[0]][wspolrzedne[1]+i] = ' ' + slowo[i] + ' '

        if kierunek == 'dol':
            for i in range(len(slowo)):
                self._plansza[wspolrzedne[0]+i][wspolrzedne[1]] = ' ' + slowo[i] + ' '


class Slowo:
    def __init__(self, gracz, plansza, numer_rundy, gracze, slowo='', wspolrzedne=(0, 0), kierunek='prawo'):
        self._slowo = slowo.upper()
        self._wspolrzedne = wspolrzedne
        self._gracz = gracz
        self._kierunek = kierunek.lower()
        self._plansza = plansza
        self._numer_rundy = numer_rundy
        self._gracze = gracze

    def slowo(self):
        return self._slowo

    def set_slowo(self, nowe_slowo):
        self._slowo = nowe_slowo.upper()

    def wspolrzedne(self):
        return self._wspolrzedne

    def set_wspolrzedne(self, nowe_wspolrzedne):
        self._wspolrzedne = nowe_wspolrzedne

    def gracz(self):
        return self._gracz

    def kierunek(self):
        return self._kierunek

    def set_kierunek(self, nowy_kierunek):
        self._kierunek = nowy_kierunek.lower()

    def plansza(self):
        return self._plansza

    def numer_rundy(self):
        return self._numer_rundy

    def gracze(self):
        return self._gracze

    def sprawdz_slowo(self):
        slownik = wczytaj_caly_slownik()

        litery_na_planszy = ''
        potrzebne_plytki = ''

        if self._slowo != '':

            #  podanie litery w miejsce #

            #  sprawdzenie czy slowo znajduje sie w slowniku
            if self._slowo.lower() not in slownik:
                return 'Podane slowo nie znajduje sie w slowniku. Prosze sprobowac ponownie.'
            # czy_poprawne = czy_slowo_ze_slownika(self._slowo)
            # if not czy_poprawne:
            #     pass

            #  sprawdzenie czy wspolrzedne sa na planszy
            if self._wspolrzedne[0] > 14 or self._wspolrzedne[0] < 0 or self._wspolrzedne[1] > 14 or self._wspolrzedne[1] < 0:
                return 'Wspolrzedne poczatkowe nie znajduja sie na planszy.'

            #  Sprawdzenie czy slowo miesci sie na planszy
            if (self._kierunek == 'prawo' and (self._wspolrzedne[1] + len(self._slowo)) >= 16) or (self._kierunek == 'dol' and (self._wspolrzedne[0] + len(self._slowo)) >= 16):
                return 'Slowo wykracza poza granice planszy.'

            #  sprawdzenie aktualnie znajdujacych sie na planszy liter(w miejscu kladzenia nowego slowa)
            litery_na_planszy = litery_z_planszy(self._slowo, self._kierunek, self._plansza, self._wspolrzedne)
            # if self._kierunek == 'prawo':
            #     for i in range(len(self._slowo)):
            #         if self._plansza._plansza[self._wspolrzedne[0]][self._wspolrzedne[1]+i] == '   ' or self._plansza._plansza[self._wspolrzedne[0]][self._wspolrzedne[1]+i] == ' * ':
            #             litery_na_planszy += ' '
            #         else:
            #             litery_na_planszy += self._plansza._plansza[self._wspolrzedne[0]][self._wspolrzedne[1]+i][1]
            # elif self._kierunek == 'dol':
            #     for i in range(len(self._slowo)):
            #         if self._plansza._plansza[self._wspolrzedne[0]+i][self._wspolrzedne[1]] == '   ' or self._plansza._plansza[self._wspolrzedne[0]+i][self._wspolrzedne[1]] == ' * ':
            #             litery_na_planszy += ' '
            #         else:
            #             litery_na_planszy += self._plansza._plansza[self._wspolrzedne[0]+i][self._wspolrzedne[1]][1]

            #  Sprawdzenie czy podane slowo pokrywa sie z polozonymi na planszy plytkami
            for i in range(len(self._slowo)):
                if litery_na_planszy[i] == ' ':
                    potrzebne_plytki += self._slowo[i]
                elif litery_na_planszy[i] != self._slowo[i]:
                    return 'Podane slowo nie pokrywa sie z plytkami na planszy. Prosze sprobowac ponownie.'

            #  Sprawdzenie czy podane slowo jest polaczone z innym polozonym slowem
            if (self._numer_rundy != 1 or (self._numer_rundy == 1 and self._gracz != self._gracze[0])) and litery_na_planszy == ' ' * len(self._slowo):
                return 'Podane slowo musi byc polaczone z innym slowem'

            #  Sprawdzenie czy podane slowo styka sie z innymi slowami w tym samym kierunku
            if self._numer_rundy != 1 or (self._numer_rundy == 1 and self._gracz != self._gracze[0]):
                stykajace_litery = 0

                if self._kierunek == 'prawo':
                    for numer, litera in enumerate(self._slowo):
                        if self._wspolrzedne[0] != 0 and self._plansza._plansza[self._wspolrzedne[0]-1][self._wspolrzedne[1]+numer] != '   ':
                            stykajace_litery += 1
                        if self._wspolrzedne[0] != 14 and self._plansza._plansza[self._wspolrzedne[0]+1][self._wspolrzedne[1]+numer] != '   ':
                            stykajace_litery += 1
                        if stykajace_litery > 2:
                            return 'Podane slowo blednie styka sie z innym slowem.'
                if self._kierunek == 'dol':
                    for numer, litera in enumerate(self._slowo):
                        if self._wspolrzedne[1] != 0 and self._plansza._plansza[self._wspolrzedne[0]+numer][self._wspolrzedne[1]-1] != '   ':
                            stykajace_litery += 1
                        if self._wspolrzedne[1] != 14 and self._plansza._plansza[self._wspolrzedne[0]+numer][self._wspolrzedne[1]+1] != '   ':
                            stykajace_litery += 1
                        if stykajace_litery > 2:
                            return 'Podane slowo blednie styka sie z innym slowem.'

            #  Sprawdzenie czy slowo nie laczy sie z innymi plytkami na tej samej linii
            if self._kierunek == 'prawo':
                for numer, litera in enumerate(self._slowo):
                    if self._wspolrzedne[1] != 0 and self._plansza._plansza[self._wspolrzedne[0]][self._wspolrzedne[1]-1] != '   ':
                        return 'Podane slowo blednie laczy sie z polozonym w tej lini slowem.'
                    if self._wspolrzedne[1]+len(self._slowo)-1 != 14 and self._plansza._plansza[self._wspolrzedne[0]][self._wspolrzedne[1]+len(self._slowo)] != '   ':
                        return 'Podane slowo blednie laczy sie z polozonym w tej lini slowem.'
            if self._kierunek == 'dol':
                for numer, litera in enumerate(self._slowo):
                    if self._wspolrzedne[0] != 0 and self._plansza._plansza[self._wspolrzedne[0]-1][self._wspolrzedne[1]] != '   ':
                        return 'Podane slowo blednie laczy sie z polozonym w tej lini slowem.'
                    if self._wspolrzedne[0]+len(self._slowo)-1 != 14 and self._plansza._plansza[self._wspolrzedne[0]+len(self._slowo)][self._wspolrzedne[1]] != '   ':
                        return 'Podane slowo blednie laczy sie z polozonym w tej lini slowem.'

            #  Sprawdzenie czy gracz posiada potrzebne plytki
            for litera in potrzebne_plytki:
                if litera not in str(self._gracz._stojak) or potrzebne_plytki.count(litera) > str(self._gracz._stojak).count(litera):
                    return 'Brakuje plytek do ulozenia podanego slowa.'

            #  Sprawdzenie czy pierwsze slowo przechodzie przez (7, 7)
            if self._numer_rundy == 1 and self._gracz == self._gracze[0]:
                if self._kierunek == 'prawo':
                    bledne_wspolrzedne = 0
                    if self._wspolrzedne[0] != 7:
                        return 'Pierwsze slowo musi przechodzic przez srodek planszy.'
                    for numer, litera in enumerate(self._slowo):
                        if self._wspolrzedne[1]+numer != 7:
                            bledne_wspolrzedne += 1
                    if bledne_wspolrzedne == len(self._slowo):
                        return 'Pierwsze slowo musi przechodzic przez srodek planszy.'

                if self._kierunek == 'dol':
                    bledne_wspolrzedne = 0
                    if self._wspolrzedne[1] != 7:
                        return 'Pierwsze slowo musi przechodzic przez srodek planszy.'
                    for numer, litera in enumerate(self._slowo):
                        if self._wspolrzedne[0]+numer != 7:
                            bledne_wspolrzedne += 1
                    if bledne_wspolrzedne == len(self._slowo):
                        return 'Pierwsze slowo musi przechodzic przez srodek planszy.'

            return True

        else:
            if self._numer_rundy == 1 and self._gracz == self._gracze[0]:
                return 'Prosze nie pomijac pierwszej rundy. Prosze podac slowo.'
            wybor = input('Na pewno chcesz pominac ture? (t/n) ').upper()
            while wybor != 'T' and wybor != 'N':
                wybor = input('Podano bledna odpowiedz. Na pewno chcesz pominac ture? (t/n)').upper()
            if wybor == 'T':
                return True
            else:
                return 'Prosze podac slowo.'

    def obliczenie_wyniku_slowa(self):
        wynik = 0
        for litera in self._slowo:
            wynik += Plytka(litera)._wartosc
        self._gracz.dodaj_do_wyniku(wynik)


def wczytaj_caly_slownik():
    slownik = []
    try:
        with open('slowa.txt', 'r') as handle:
            for slowo in handle:
                slowo = slowo.rstrip('\n')
                slownik.append(slowo)
    except FileNotFoundError:
        raise NieZnalezionoPlikuSlownikError('Brak pliku slownik.txt')
    except PermissionError:
        raise BrakDostepuError('Nie mozna odczytac pliku (brak dostepu)')
    return slownik


def czy_slowo_ze_slownika(slowo):
    slownik = wczytaj_caly_slownik()
    if slowo.lower() not in slownik:
        return False
    else:
        return True


def litery_z_planszy(slowo, kierunek, plansza, wspolrzedne):
    litery_na_planszy = ''
    if kierunek == 'prawo':
        for i in range(len(slowo)):
            if plansza._plansza[wspolrzedne[0]][wspolrzedne[1]+i] == '   ' or plansza._plansza[wspolrzedne[0]][wspolrzedne[1]+i] == ' * ':
                litery_na_planszy += ' '
            else:
                litery_na_planszy += plansza._plansza[wspolrzedne[0]][wspolrzedne[1]+i][1]
    elif kierunek == 'dol':
        for i in range(len(slowo)):
            if plansza._plansza[wspolrzedne[0]+i][wspolrzedne[1]] == '   ' or plansza._plansza[wspolrzedne[0]+i][wspolrzedne[1]] == ' * ':
                litery_na_planszy += ' '
            else:
                litery_na_planszy += plansza._plansza[wspolrzedne[0]+i][wspolrzedne[1]][1]
    return litery_na_planszy


def tura(aktualny_gracz, plansza, pula_liter, numer_rundy, pominiete_tury, gracze):
    najmniej_plytek = 7
    for gracz in gracze:
        if gracz.stojak().ilosc_plytek() < najmniej_plytek:
            najmniej_plytek = gracz.stojak().ilosc_plytek()
    if (pominiete_tury == len(gracze)*2) or (len(pula_liter.plytki()) == 0 and najmniej_plytek == 0):
        zakoncz_gre(gracze)
    else:
        print('\nRunda numer ' + str(numer_rundy) + ': ' + 'Teraz kolej gracza ' + aktualny_gracz.nazwa() + '\n')
        print(str(plansza))
        if type(aktualny_gracz) == Bot:
            wprowadzane_slowo, wspolrzedne, kierunek, aktualny_gracz, pula_liter = aktualny_gracz.dodaj_slowo(plansza, pula_liter, numer_rundy, pominiete_tury, gracze)
            slowo = Slowo(aktualny_gracz, plansza, numer_rundy, gracze, wprowadzane_slowo, wspolrzedne, kierunek)
        else:
            print('\nStojak gracza ' + aktualny_gracz.nazwa() + ': ' + str(aktualny_gracz.stojak()))

            slowo = Slowo(aktualny_gracz, plansza, numer_rundy, gracze)
            sprawdzone_slowo = False
            while sprawdzone_slowo is not True:
                wprowadzane_slowo = input('Podaj slowo, ktore chcesz utworzyc (zostaw puste, aby pominac ture): ')
                slowo.set_slowo(wprowadzane_slowo)
                kolumna = input('Podaj numer kolumny: ')
                try:
                    kolumna = int(kolumna)
                except ValueError:
                    kolumna = input('Nie podano numeru. Podaj numer kolumny: ')
                while kolumna not in [x for x in range(15)]:
                    kolumna = int(input('Podano zly numer. Podaj numer kolumny: '))
                wiersz = int(input('Podaj numer wiersza: '))
                while wiersz not in [x for x in range(15)]:
                    wiersz = int(input('Podano zly numer. Podaj numer kolumny: '))
                wspolrzedne = (wiersz, kolumna)
                slowo.set_wspolrzedne(wspolrzedne)
                kierunek = input('Podaj kierunek wprowadzanego slowa(prawo/dol): ')
                while kierunek != 'prawo' and kierunek != 'dol':
                    kierunek = input('Nieprawidlowy kierunek. Podaj kierunek wprowadzanego slowa(prawo/dol): ')
                slowo.set_kierunek(kierunek)
                sprawdzone_slowo = slowo.sprawdz_slowo()
                if sprawdzone_slowo is not True:
                    print(sprawdzone_slowo)

        if slowo._slowo == '':
            print('Tura zostala pominieta.')
            pominiete_tury += 1
        else:
            plansza.dodaj_slowo(wprowadzane_slowo, wspolrzedne, kierunek, aktualny_gracz, pula_liter)
            slowo.obliczenie_wyniku_slowa()
            pominiete_tury = 0

        print('\nAktualny wynik gracza ' + aktualny_gracz._nazwa + ' wynosi: ' + str(aktualny_gracz._wynik))

        if gracze.index(aktualny_gracz) != len(gracze)-1:
            aktualny_gracz = gracze[gracze.index(aktualny_gracz)+1]
        else:
            aktualny_gracz = gracze[0]
            numer_rundy += 1

        tura(aktualny_gracz, plansza, pula_liter, numer_rundy, pominiete_tury, gracze)


def rozpocznij_gre():
    plansza = Plansza()
    pula_liter = PulaLiter()

    tryb_gry = int(input('Rozpoczac gre lokalna(1), czy gre z botem(2)? '))
    while tryb_gry != 1 and tryb_gry != 2:
        tryb_gry = int(input('Podano niepoprawna liczbe. Rozpoczac gre lokalna(1), czy gre z botem(2)? '))

    if tryb_gry == 1:
        liczba_graczy = int(input('Podaj liczbe graczy (2-4): '))
        while liczba_graczy < 2 or liczba_graczy > 4:
            liczba_graczy = int(input('Podano niepoprawna liczbe graczy. Podaj liczbe graczy (2-4): '))

        gracze = []
        for i in range(liczba_graczy):
            nazwa = input('Podaj nazwe ' + str(i+1) + '. gracza: ')
            gracze.append(Gracz(nazwa, pula_liter))

        numer_rundy = 1
        pominiete_tury = 0
        aktualny_gracz = gracze[0]

        tura(aktualny_gracz, plansza, pula_liter, numer_rundy, pominiete_tury, gracze)

    else:
        gracze = []
        nazwa = input('Podaj swoja nazwe: ')
        gracze.append(Gracz(nazwa, pula_liter))
        gracze.append(Bot('BOT', pula_liter))

        numer_rundy = 1
        pominiete_tury = 0
        aktualny_gracz = gracze[0]

        tura(aktualny_gracz, plansza, pula_liter, numer_rundy, pominiete_tury, gracze)


def zakoncz_gre(gracze):
    najwyzszy_wynik = 0
    for gracz in gracze:
        if gracz._wynik > najwyzszy_wynik:
            najwyzszy_wynik = gracz._wynik
            zwyciezca = str(gracz._nazwa)
    #  sprawdzenie czy jest remis
    zwyciezcy = []
    for gracz in gracze:
        if gracz._wynik == najwyzszy_wynik:
            zwyciezcy.append(gracz)
    if len(zwyciezcy) > 1:
        zwyciezcy_str = ''
        for gracz in zwyciezcy:
            zwyciezcy_str += gracz._nazwa
            zwyciezcy_str += ', '
        print('\nKoniec gry! Rozgrywka zakonczona remisem. Gracze ' + zwyciezcy_str[:-2] + ' zdobyli po ' + str(najwyzszy_wynik) + ' punktow.')
    else:
        print('\nKoniec gry! Zwyciezca: ' + zwyciezca + '. Zdobyte punkty: ' + str(najwyzszy_wynik))

    if input('Chcesz zagrac ponownie? (t/n) ').upper() == 'T':
        rozpocznij_gre()


if __name__ == '__main__':
    rozpocznij_gre()
