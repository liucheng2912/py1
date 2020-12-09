import requests
from requests.auth import HTTPBasicAuth


def test_oauth():
    r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/banana/123", auth=HTTPBasicAuth("banana", "123"))
    print(r.text)
