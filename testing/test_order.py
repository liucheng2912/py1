import pytest


# 第二个执行
@pytest.mark.run(order=2)
def test_case1():
    print("用例1")


# 最后一个执行
@pytest.mark.run(order=-1)
def test_case2():
    print("用例2")


# 第一个执行
# @pytest.mark.run(order=1)
@pytest.mark.first
def test_case3():
    print("用例3")


def test_case4():
    print("用例4")


def test_case5():
    print("用例5")


def test_case6():
    print("用例6")
