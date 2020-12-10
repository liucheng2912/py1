import json

import requests

from service.base_api import BaseApi


class Tag(BaseApi):
    def __init__(self):
        super().__init__()

    def find_id_by_name(self, group_name):
        # 如果group_name 存在 返回他对应的ID
        for group in self.list().json()['tag_group']:
            if group_name in group["group_name"]:
                return group['group_id']
        # 不存在 返回空值
        print('group name not in group')
        return ""

    def is_group_id_exist(self, group_id):
        # 如果group_name 存在 返回他对应的ID
        for group in self.list().json()['tag_group']:
            if group_id in group["group_id"]:
                return True
        # 不存在 返回空值
        print('group id not in group')
        return False

    def add(self, group_name, tag, **kwargs):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                "params": {"access_token": self.token},
                "json": {"group_name": group_name, "tag": tag, **kwargs}}
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    # 添加前判断是否已经存在 已经存在的话 先删除 再添加
    def add_and_detect(self, group_name, tag, **kwargs):
        r = self.add(group_name, tag, **kwargs)
        # 如果元素存在 删除
        if r.json()['errcode'] == 40071:
            group_id = self.find_id_by_name(group_name)
            if not group_id:
                return ""
            self.delete_groupid([group_id])
            self.add(group_name, tag, **kwargs)
        result = self.find_id_by_name(group_name)
        if not result:
            print('add not success')
        return result

    def delete_tagid(self, tag_id):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                "params": {"access_token": self.token},
                "json": {"tag_id": tag_id}}
        r = self.send(data)
        return r

    def delete_groupid(self, group_id):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                "params": {"access_token": self.token},
                "json": {"group_id": group_id}}
        r = self.send(data)
        return r

    # 删除前 确认元素是否存在 不存在 新建一个元素
    def delete_and_detect_group(self, group_ids):
        delete_group_id = []
        r = self.delete_groupid(group_ids)
        for group_id in group_ids:
            if r.json()['errcode'] == 40068:
                # 如果标签不存在 就新生成一个标签，放到标签组里
                if not self.is_group_id_exist(group_id):
                    groupid_tmp = self.add_and_detect('A123', [{'name': 'Tag1'}, {'name': 'Tag2'}, {'name': 'Tag3'}])
                    delete_group_id.append(groupid_tmp)
                else:
                    # 如果标签存在，直接放到标签组里
                    delete_group_id.append(groupid_tmp)
        r = self.delete_groupid(delete_group_id)
        return r

    def update(self, id, name):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                "params": {"access_token": self.token},
                "json": {"id": id, "name": name}}
        r = self.send(data)
        return r

    def list(self):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                "params": {"access_token": self.token},
                "json": {"tag_id": []}}
        r = self.send(data)
        return r
