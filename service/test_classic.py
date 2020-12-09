import datetime
import json

import requests


def test_tag():
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

    tag_name = 'tag1_new' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                      params={'access_token': token},
                      json={"id": "eteTbfCwAAkiQsjOWc6j8_oQCyF8-Xhw", "name": tag_name})

    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                      params={'access_token': token}, json={"tag_id": []})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tag = [tag
           for group in r.json()['tag_group'] if group['group_name'] == 'test'
           for tag in group['tag'] if tag['name'] == tag_name]
    assert tag != []
