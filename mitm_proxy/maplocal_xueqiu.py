"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("E:/ck/quote.json", encoding="utf-8") as f:
            # 创造一个response
            flow.response = http.HTTPResponse.make(
                200,
                # 读取文件中的内容作为返回内容
                f.read(),
                # 指定返回的数据类型
                {"Content-Type": "application/json"}
            )
