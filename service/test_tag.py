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

    @pytest.mark.parametrize("group_name,tag", [
        ['testlc123', [{'name': '1'}, {'name': '2'}, {'name': '3'}]],
        ['test中文123', [{'name': '你好'}, {'name': 'hello'}, {'name': '你好hi'}]],
        ['test_中文123', [{'name': 'tag1[中文]'}, {'name': 'testliucheng'}]]
    ])
    # 添加用户
    def test_add(self, group_name, tag):
        # group_name = group_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        r = self.tag.add(group_name, tag)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("group_name,tag", [
        ['testlc123', [{'name': '1'}, {'name': '2'}, {'name': '3'}]],
        ['test中文123', [{'name': '你好'}, {'name': 'hello'}, {'name': '你好hi'}]],
        ['test_中文123', [{'name': 'tag1[中文]'}, {'name': 'testliucheng'}]]
    ])
    # 添加用户
    def test_add_and_detect(self, group_name, tag):
        # group_name = group_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        r = self.tag.add_and_detect(group_name, tag)
        assert r

    # 删除标签 通过tagid
    def test_delete_tagid(self):
        tag_id = ['eteTbfCwAAj5NKwvQi6K836Nac-KIcfA']
        r = self.tag.delete_tagid(tag_id)

    # 删除标签 通过groupid
    def test_delete_groupid(self):
        group_id = ['eteTbfCwAAyMz2fkubaFi-XbCwyM2OeQ']
        r = self.tag.delete_groupid(group_id)

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["eteTbfCwAAfN8_nUnj1hasyLJpPpYR6A"])
        assert r.json()['errcode'] == 0
