from mitmproxy import http
import json

# 修改规则模型
rule = [0, 1, 3, 5, 100]

# 统计url
url_index = dict()


def response(flow: http.HTTPFlow):
    url = flow.request.url.split('.json')[0]
    # 如果url不在url_index字典的key中
    if url not in url_index.keys():
        # 把对应的key赋值为0
        url_index[url] = 0
    else:
        url_index[url] += 1

    seed = url_index[url] % len(rule)

    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转换成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 对数据进行批量修改
        data_new = json_travel(data, num=rule[seed])

        # 把修改后的内容 赋值给response原始数据格式
        flow.response.text = json.dumps(data_new)


# 实现数据批量修改
# dict list string num(int float)
def json_travel(data, array=None, text=1, num=1):
    """
    完成json数据的倍数操作
    :param data: 要修改的内容
    :param array: 列表的修改规则，为None默认不修改
    :param text: 字符串的修改规则，为1默认不修改
    :param num: 整数或者浮点数的修改，为1默认不修改
    :return: date_new
    """""
    # 定义返回的数据
    data_new = None
    # 判断传入data的类型
    if isinstance(data, dict):
        # 把修改后的数据定义为一个空字典
        data_new = dict()

        # 对传入的响应数据进行遍历 每一个k对应的value。继续json_travel处理
        for k, v in data.items():
            data_new[k] = json_travel(v, array, text, num)

    # 如果是列表，对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()
        # 遍历列表中的所有元素
        for item in data:
            item_new = json_travel(item, array, text, num)

        # 如果传入array为空，对列表元素不做处理
        if array is None:
            data_new.append(item_new)
        else:
            # 判断传入的array修改规则，是否可以正常修改
            if isinstance(array, int) and array >= 0:
                for i in range(array):
                    data_new.append(item_new)
            else:
                data_new = data

    # 如果是字符串
    # 对字符串做加倍操作
    elif isinstance(data, str):
        # 如果text为正整数
        if isinstance(text, int) and text >= 0:
            data_new = data * text
        else:
            data_new = data

    # 如果是int或者float这样的数字
    # 对数字做乘积操作
    elif isinstance(data, int) or isinstance(data, float):
        data_new = data * num

    # 其他类型保持原样
    else:
        data_new = data

    return data_new
