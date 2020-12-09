import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={'h': 'liucheng'})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "liucheng"

    def test_get_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))
