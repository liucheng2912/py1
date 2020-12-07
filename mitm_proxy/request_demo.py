from mitmproxy import http


# request 方法名称不能修改
def request(flow: http.HTTPFlow):
    # 增加请求的头信息中的字段
    flow.request.headers["myheader"] = "liucheng"
    print(flow.request.headers)
