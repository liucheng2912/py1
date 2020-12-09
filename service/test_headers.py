import requests


# 通过header传递，header中增加Cookie参数
def test_headers():
    url = "http://httpbin.testing-studio.com/cookies"
    header = {"Cookie": "liucheng", 'User-Agent': 'levi'}
    r = requests.get(url, headers=header)
    print(r.request.headers)


# 通过cookie传递，可以传递多个cookie
def test_cookie():
    url = "http://httpbin.testing-studio.com/cookies"
    header = {'User-Agent': 'levi'}
    cookie_data = {'liucheng': 'test', 'levi': 'test1'}
    r = requests.get(url, headers=header, cookies=cookie_data)
    print(r.request.headers)
