import pytest

from pthoncode.calculator import Calculator


@pytest.fixture(scope="function", params=['tom', 'jerry'])
# 相当于setup和teardown
# 使用params 必须传递request参数 固定用法 request.param 会根据传递的参数生成对应的测试用例
def login(request):
    print("登录操作")
    username = request.param
    yield username
    # yield前代表setup 后代表teardown yield相当于return操作
    print("登出操作")


# autouse 自动使用，默认范围是方法都要使用 不需要调用 默认是false
# 假如想使用返回值 还是需要在参数中假如fixture的名字
# scope 表示作用域 module表示作用域整个模块即整个py文件，在所有方法开始前和结束后执行一次
@pytest.fixture(autouse=True, scope="module")
def con_db():
    print("完成数据库连接")


@pytest.fixture()
def con_db1():
    print("完成数据库连接1")


# session作用于整个项目 在整个项目开始和结束前执行
@pytest.fixture(scope='session', autouse=True)
def con_db2():
    print("完成数据库连接2")


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
