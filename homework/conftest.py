import pytest

from homework.calculator import Calculator


@pytest.fixture(autouse=True, scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")
