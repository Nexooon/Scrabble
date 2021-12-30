from scrabble import Plytka, PulaLiter, Stojak


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
    assert stojak.__str__() == '#, #, Ż, Ź, Z, Z, Z'


def test_wez_i_dodaj_plytke_z_puli(monkeypatch):
    def bez_mieszania(k):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    plytka = stojak.plytki()[3]
    stojak.wez_plytke(plytka)
    assert stojak.ilosc_plytek() == 6
    assert stojak.__str__() == '#, #, Ż, Z, Z, Z'
    stojak.dodaj_plytke_z_puli(pula)
    assert stojak.ilosc_plytek() == 7
    assert stojak.__str__() == '#, #, Ż, Z, Z, Z, Z'


def test_dodaj_plytke_z_puli_7_plytek():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    stojak.dodaj_plytke_z_puli(pula)
    assert stojak.ilosc_plytek() == 7


def test_dodaj_plytke():
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


def test_dodaj_plytke_7_plytek():
    pula = PulaLiter()
    stojak = Stojak(pula)
    assert stojak.ilosc_plytek() == 7
    plytka = Plytka('A')
    stojak.dodaj_plytke(plytka)
    assert stojak.ilosc_plytek() == 7
