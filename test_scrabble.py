from scrabble import Plytka, PulaLiter, Stojak, Gracz, Plansza, Slowo, Bot
from scrabble import wczytaj_caly_slownik, litery_z_planszy
from scrabble import NazwaError, UjemnyWynikError, UjemnePunktyError
import pytest


def test_plytka_init():
    plytka = Plytka('A')
    assert plytka.litera() == 'A'
    assert plytka.wartosc() == 1


def test_plytka_mala_litera():
    plytka = Plytka('ą')
    assert plytka.litera() == 'Ą'
    assert plytka.wartosc() == 5


def test_pula_liter_init():
    pula = PulaLiter()
    assert len(pula.plytki()) == 100


def test_pula_liter_wez_plytke(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    assert len(pula.plytki()) == 100
    plytka = pula.wez_plytke()
    assert len(pula.plytki()) == 99
    assert plytka.litera() == '#'
    assert plytka.wartosc() == 0


def test_stojak_init():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert len(stojak.plytki()) == 7
    assert stojak.ilosc_plytek() == 7


def test_stojak_str(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert str(stojak) == '#, #, Ż, Ź, Z, Z, Z'


def test_stojak_wez_i_dodaj_plytke_z_puli(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    plytka = stojak.plytki()[3]
    stojak.wez_plytke(plytka)
    assert stojak.ilosc_plytek() == 6
    assert str(stojak) == '#, #, Ż, Z, Z, Z'
    stojak.dodaj_plytke_z_puli(pula)
    assert stojak.ilosc_plytek() == 7
    assert str(stojak) == '#, #, Ż, Z, Z, Z, Z'


def test_stojak_dodaj_plytke_z_puli_7_plytek():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    stojak.dodaj_plytke_z_puli(pula)
    assert stojak.ilosc_plytek() == 7


def test_stojak_dodaj_plytke():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    plytka = stojak.plytki()[3]
    stojak.wez_plytke(plytka)
    assert stojak.ilosc_plytek() == 6
    plytka = Plytka('A')
    stojak.dodaj_plytke(plytka)
    assert stojak.ilosc_plytek() == 7
    assert plytka in stojak.plytki()


def test_stojak_wymien_plytki(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert str(stojak) == '#, #, Ż, Ź, Z, Z, Z'
    stojak.wymien_plytki('#ŻZ', pula)
    assert str(stojak) != '#, #, Ż, Ź, Z, Z, Z'
    assert len(stojak._plytki) == 7


def test_stojak_wymien_plytki_brak_plytek(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert str(stojak) == '#, #, Ż, Ź, Z, Z, Z'
    with pytest.raises(ValueError):
        stojak.wymien_plytki('ABC', pula)


def test_stojak_dodaj_plytke_7_plytek():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    plytka = Plytka('A')
    stojak.dodaj_plytke(plytka)
    assert stojak.ilosc_plytek() == 7


def test_gracz_init():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula, 10)
    assert gracz.nazwa() == 'Adam'
    assert gracz.wynik() == 10
    assert gracz.stojak().ilosc_plytek() == 7


def test_gracz_init_domyslny_wynik():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    assert gracz.nazwa() == 'Adam'
    assert gracz.wynik() == 0
    assert gracz.stojak().ilosc_plytek() == 7


def test_gracz_init_brak_nazwy():
    pula = PulaLiter()
    with pytest.raises(NazwaError):
        Gracz('', pula)


def test_gracz_init_ujemny_wynik():
    pula = PulaLiter()
    with pytest.raises(UjemnyWynikError):
        Gracz('Adam', pula, -12)


def test_gracz_init_brak_puli():
    with pytest.raises(ValueError):
        Gracz('Adam', None)


def test_gracz_set_nazwa():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    assert gracz.nazwa() == 'Adam'
    gracz.set_nazwa('Maciej')
    assert gracz.nazwa() == 'Maciej'


def test_gracz_set_nazwa_pusta():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    with pytest.raises(NazwaError):
        gracz.set_nazwa('')


def test_gracz_set_wynik():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    assert gracz.wynik() == 0
    gracz.set_wynik(20)
    assert gracz.wynik() == 20


def test_gracz_set_wynik_ujemny():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    assert gracz.wynik() == 0
    with pytest.raises(UjemnyWynikError):
        gracz.set_wynik(-11)


def test_gracz_dodaj_do_wyniku():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula, 10)
    assert gracz.wynik() == 10
    gracz.dodaj_do_wyniku(5)
    assert gracz.wynik() == 15


def test_gracz_dodaj_do_wyniku_ujemne():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula, 10)
    assert gracz.wynik() == 10
    with pytest.raises(UjemnePunktyError):
        gracz.dodaj_do_wyniku(-3)


def test_bot_init():
    pula = PulaLiter()
    bot = Bot('Franek', pula)
    assert len(bot._slownik_punkty) > 0
    assert bot._slownik_punkty['BANAN'] == 7


def test_bot_slowa_do_dodania():
    pula = PulaLiter()
    bot = Bot('Franek', pula)
    mozliwe_slowa = bot.slowa_do_dodania()
    assert len(mozliwe_slowa) > 0


def test_bot_slowa_do_dodania_konkretne_litery(monkeypatch):
    pula = PulaLiter()

    def pusty_stojak(f, k):
        return
    monkeypatch.setattr('scrabble.Stojak.uzupelnij_stojak', pusty_stojak)
    stojak = Stojak(pula)
    a = Plytka('A')
    b = Plytka('B')
    n = Plytka('N')

    stojak.dodaj_plytke(a)
    stojak.dodaj_plytke(b)
    stojak.dodaj_plytke(a)
    stojak.dodaj_plytke(n)
    stojak.dodaj_plytke(n)
    stojak.dodaj_plytke(a)
    stojak.dodaj_plytke(a)
    assert str(stojak) == 'A, B, A, N, N, A, A'
    bot = Bot('Franek', pula)
    bot.set_stojak(stojak)
    mozliwe_slowa = bot.slowa_do_dodania()
    assert len(mozliwe_slowa) > 0
    assert 'BANAN' in mozliwe_slowa
    assert 'ANA' in mozliwe_slowa
    assert mozliwe_slowa['BANAN'] == 7
    assert mozliwe_slowa['ANA'] == 3


def test_plansza_init():
    plansza = Plansza()
    assert len(plansza.plansza()) == 15
    assert plansza.plansza()[7][7] == ' * '


def test_plansza_dodaj_slowo():
    plansza = Plansza()
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    plansza.dodaj_slowo('TEST', (0, 0), 'prawo', gracz, pula)
    assert plansza.plansza()[0][0] == ' T '
    assert plansza.plansza()[0][1] == ' E '
    assert plansza.plansza()[0][2] == ' S '
    assert plansza.plansza()[0][3] == ' T '
    assert gracz.stojak().ilosc_plytek() == 7


def test_slowo_init():
    plansza = Plansza()
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    gracze = [gracz]
    numer_rundy = 0
    slowo = Slowo(gracz, plansza, numer_rundy, gracze, 'marchew', (4, 7), 'prawo')
    assert slowo.slowo() == 'MARCHEW'
    assert slowo.wspolrzedne() == (4, 7)
    assert slowo.gracz() == gracz
    assert slowo.kierunek() == 'prawo'
    assert slowo.plansza() == plansza
    assert slowo.numer_rundy() == 0


def test_slowo_set():
    plansza = Plansza()
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    gracze = [gracz]
    numer_rundy = 0
    slowo = Slowo(gracz, plansza, numer_rundy, gracze, 'marchew', (4, 7), 'prawo')
    assert slowo.slowo() == 'MARCHEW'
    assert slowo.wspolrzedne() == (4, 7)
    assert slowo.gracz() == gracz
    assert slowo.kierunek() == 'prawo'
    assert slowo.plansza() == plansza
    assert slowo.numer_rundy() == 0
    slowo.set_wspolrzedne((7, 3))
    assert slowo.wspolrzedne() == (7, 3)
    slowo.set_slowo('ananas')
    assert slowo.slowo() == 'ANANAS'
    slowo.set_kierunek('dol')
    assert slowo.kierunek() == 'dol'


def test_slowo_obliczenie_wyniku():
    plansza = Plansza()
    pula = PulaLiter()
    gracz = Gracz('Adam', pula)
    gracze = [gracz]
    numer_rundy = 0
    slowo = Slowo(gracz, plansza, numer_rundy, gracze, 'marchew', (4, 7), 'prawo')
    slowo.obliczenie_wyniku_slowa()
    assert gracz.wynik() == 11


def test_wczytaj_caly_slownik():
    slownik = wczytaj_caly_slownik()
    assert len(slownik) > 0


def test_litery_z_planszy():
    pula = PulaLiter()
    plansza = Plansza()
    numer_rundy = 1
    gracz = Gracz('jan', pula)
    gracze = [gracz]
    slowo = Slowo(gracz, plansza, numer_rundy, gracze, 'TEST', (7, 7))
    litery = litery_z_planszy(slowo.slowo(), slowo.kierunek(), plansza, slowo.wspolrzedne())
    assert litery == '    '
