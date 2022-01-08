from scrabble import Plytka, PulaLiter, Stojak, Gracz
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


# def test_plytka_bledna_litera():
#     pass


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


def test_dodaj_do_wyniku():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula, 10)
    assert gracz.wynik() == 10
    gracz.dodaj_do_wyniku(5)
    assert gracz.wynik() == 15


def test_dodaj_do_wyniku_ujemne():
    pula = PulaLiter()
    gracz = Gracz('Adam', pula, 10)
    assert gracz.wynik() == 10
    with pytest.raises(UjemnePunktyError):
        gracz.dodaj_do_wyniku(-3)
