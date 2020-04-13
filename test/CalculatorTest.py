from code import Calculator
from pytest import fixture


@fixture
def calc():
    return Calculator.Calculator()


def test_add(calc):
    assert 300 == calc.add(10,20)
