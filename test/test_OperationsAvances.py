from mathematique.OperationsAvances import OperationsAvances


def test_puissance():
    oa = OperationsAvances()
    result = oa.puissance(2, 3)
    assert result == 8


def test_racine_x():
    oa = OperationsAvances()
    result = oa.racine_x(float(8), 3)
    assert result == 2
