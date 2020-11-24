import pytest


# 执行到错误的地方后续步骤不会再执行
def test_case1():
    assert 1 == 1
    assert False
    assert True


# 遇到错误也会继续执行 知道执行完毕一条测试用例
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)
