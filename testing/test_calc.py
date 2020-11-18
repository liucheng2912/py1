from pthoncode.calculator import Calculator


class TestCalc:

    # def setup(self):
    #     self.calc = Calculator()
    #     print("计算开始")
    #
    # def teardown(self):
    #     print("计算结束")

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    def test_add(self):
        # calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2

    def test_add1(self):
        # calc = Calculator()
        result = self.calc.add(100, 100)
        assert result == 200

    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(0.1, 0.1)
        assert result == 0.2
