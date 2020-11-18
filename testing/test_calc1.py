import pytest

from pthoncode.calculator import Calculator


class TestCalc1:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [1000000, 1000000, 2000000], [-1, -1, -2], [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'minus_case', 'zero_case'])
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.2, 0.3], [0.1, 0.1, 0.2]
    ])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        # round对浮点数四舍五入 第二个参数表示保留小数点后几位
        assert expect == round(result, 2)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [10000, 10, 1000]
    ])
    def test_div(self, a, b, expect):
        if b == 0:
            print("除数不能为0")
        else:
            result = self.calc.div(a, b)
            assert expect == result

    @pytest.mark.parametrize('a,b', [
        [1, 0], [0.1, 0]
    ])
    def test_div_zero(self, a, b):
        # 如果没有抛出ZeroDivisionError 异常 或者抛出其他异常 这条用例也会失败 可以用来判断抛出的异常是否正确
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)
        # try:
        #     result = self.calc.div(1, 0)
        # except ZeroDivisionError:
        #     print("除数为0")
