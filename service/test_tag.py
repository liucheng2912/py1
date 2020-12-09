import datetime

import pytest
from jsonpath import jsonpath
from service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id,tag_name", [
        ['eteTbfCwAAkiQsjOWc6j8_oQCyF8-Xhw', 'tag1_new_'],
        ['eteTbfCwAAkiQsjOWc6j8_oQCyF8-Xhw', 'tag1中文'],
        ['eteTbfCwAAkiQsjOWc6j8_oQCyF8-Xhw', 'tag1[中文]']
    ])
    # 修改标签
    def test_tag(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

        r = self.tag.list()
        r = self.tag.update(tag_id, tag_name)
        r = self.tag.list()

        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    # 删除标签 通过tagid
    def test_delete_tagid(self):
        tag_id = ['eteTbfCwAAj5NKwvQi6K836Nac-KIcfA']
        r = self.tag.delete_tagid(tag_id)
        r = self.tag.list()
        r.json()['errcode'] == 0

    # 删除标签 通过groupid
    def test_delete_groupid(self):
        group_id = ['eteTbfCwAAyMz2fkubaFi-XbCwyM2OeQ']
        r = self.tag.delete_groupid(group_id)
        r = self.tag.list()
        r.json()['errcode'] == 0

        for i in r.json()['tag_group'][0]['group_id']:
            if i == group_id:
                assert False
                break
        assert True

    @pytest.mark.parametrize("group_name,tag_name", [
        ['testlc', ['1', '2', '3']],
        ['test中文', ['你好', 'hello', '你好hi']],
        ['test_中文', ['tag1[中文]', 'testliucheng']]
    ])
    # 添加用户
    def test_new(self, group_name, tag_name):
        group_name = group_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        r = self.tag.add(group_name, tag_name)
        print(r.json())
