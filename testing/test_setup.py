# 方法不在类中
def test_case1():
    print("case1")


def test_case2():
    print("case2")


# 只会对类外面的方法生效
def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo:
    def test_demo1(self):
        print("demo1")

    def test_demo2(self):
        print("demo1")

    # 类中起始和结束执行一次
    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    # 类中每个方法都会调用
    def setup(self):
        print("setup method")

    def teardown(self):
        print("teardown method")


class TestDemo1:
    def test_demo11(self):
        print("demo1")

    def test_demo22(self):
        print("demo1")


# 整个模块起始和结束时执行一次
def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")
