import pytest
import yaml


def get_datas():
    with open("E:/py1/testing/datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas, add_ids)
    return [add_datas, add_ids]


class TestCalc:

    # def setup(self):
    #     self.calc = Calculator()
    #     print("计算开始")
    #
    # def teardown(self):
    #     print("计算结束")

    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("计算开始")
    #
    # def teardown_class(self):
    #     print("计算结束")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert expect == result

    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
