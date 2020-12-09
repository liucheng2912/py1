import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww30594f100b43f521'
        corpsecret = 'RGY10DrDguAHzESitXZDO1rMWaHadG-Bi_ppPCO4LW4'

        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']

        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={'access_token': token}, json={"tag_id": []})
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        return token

    def add(self, group_name, tag_name):
        for i in tag_name:
            order = 0
            r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                              params={'access_token': self.token},
                              json={"group_name": group_name,
                                    "tag": [{"name": i, order: order}]})
            order += 1
        return r

    def delete_tagid(self, tag_id):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={"tag_id": tag_id})
        return r

    def delete_groupid(self, group_id):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={"group_id": group_id})
        return r

    def update(self, id, name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={'access_token': self.token},
                          json={"id": id, "name": name})
        return r

    def list(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={'access_token': self.token}, json={"tag_id": []})
        return r
