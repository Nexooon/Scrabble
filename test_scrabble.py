from scrabble import Plytka, PulaLiter


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
    def bez_mieszania(l):
        return
    monkeypatch.setattr('scrabble.shuffle', bez_mieszania)
    pula = PulaLiter()
    assert len(pula.plytki()) == 100
    plytka = pula.wez_plytke()
    assert len(pula.plytki()) == 99
    assert plytka.litera() == '#'
    assert plytka.wartosc() == 0
