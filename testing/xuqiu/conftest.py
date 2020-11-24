# session作用于整个项目 在整个项目开始和结束前执行
import pytest


@pytest.fixture()
def con_db():
    print("完成数据库连接aaaaaa")
    yield "database"
    print("关闭数据库连接aaaaaa")
