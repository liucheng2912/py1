import pytest
import yaml

from homework.calculator import Calculator


@pytest.fixture(autouse=True, scope="module")
def get_calc():
    calc = Calculator()
    yield calc


def get_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    return [add_datas, add_ids]


def get_float_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add_float']['datas']
    return [add_datas]


def get_sub_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    sub_datas = datas['sub']['datas']
    return [sub_datas]


def get_mul_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    mul_datas = datas['mul']['datas']
    return [mul_datas]


def get_mulfloat_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    mul_datas = datas['mul_float']['datas']
    return [mul_datas]


def get_div_datas():
    with open('E:/py1/testing/datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    div_datas = datas['div']['datas']
    return [div_datas]


class Test_calc:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_float_datas()[0])
    def test_addfloat(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert expect == round(result, 2)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_sub_datas()[0])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert expect == result

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_mul_datas()[0])
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert expect == result

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b,expect', get_mulfloat_datas()[0])
    def test_mulfloat(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert expect == round(result, 2)

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a,b,expect', get_div_datas()[0])
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert expect == result

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a,b', [[1, 0], [0.1, 0]])
    def test_div(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)
