from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转换成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 修改第一支股票的名称
        name1 = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] = name1 * 2
        data['data']['items'][2]['quote']['name'] = ''
        # 把修改后的内容 赋值给response原始数据格式
        flow.response.text = json.dumps(data)
