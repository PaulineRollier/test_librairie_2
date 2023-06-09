from mathematique.OperationsBasiques import OperationsBasiques


def test_addition():
    ob = OperationsBasiques()
    result = ob.addition(1, 2)
    assert result == 3


def test_soustraction():
    ob = OperationsBasiques()
    result = ob.soustraction(3, 2)
    assert result == 1


def test_multiplication():
    ob = OperationsBasiques()
    result = ob.multiplication(2, 3)
    assert result == 6


def test_division():
    ob = OperationsBasiques()
    result = ob.division(float(3), 4)
    assert result == 0.75
