import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww30594f100b43f521'
        corpsecret = 'RGY10DrDguAHzESitXZDO1rMWaHadG-Bi_ppPCO4LW4'
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r
