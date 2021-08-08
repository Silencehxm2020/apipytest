# 将不同的请求整合成一种请求
import requests

from tools.my_logging import LOG


class Http_request:
    def __init__(self, url, method, data=None, header=None):
        self.url = url
        self.method = method
        self.data = data
        self.header = header

    def do_request(self):
        try:
            LOG.info("正在请求HTTP")
            if self.method.lower() == 'get':
                res = requests.get(self.url, params=self.data, headers=self.header)
                LOG.info("正在进行get请求：请求地址：{}，请求参数：{}，请求头为：{}".format(self.url, self.data, self.header))
            elif self.method.lower() == 'post':
                res = requests.post(self.url, json=self.data, headers=self.header)
                LOG.info("正在进行post请求：请求地址：{}，请求参数：{}，请求头为：{}".format(self.url, self.data, self.header))
            else:
                LOG.error("暂时请求方式只有get，post，如需添加请联系胡晓明,现请求方式为{}".format(self.method))
        except Exception as e:
            LOG.error("请求出现异常信息为：{}".format(e))
            raise e
        return res.json()


if __name__ == '__main__':
    url = "https://apity.bndxxf.com/company/sys/pc/login"
    dat = {"telephone": "18806644815",
           "password": "kwicOYe1ZHRPwapWtHRw8LlSuP2++T7Tc826GdZV6t6tTAdg2YxNm6e17MYtfQBKOb268xGth1YEy2L4FbOrfRZjnsZyxRskTRj6rFDYjiy8cEnC+eC1G2s5inhXbQJLLtGmE0uB2IgNTGOoAKG0UP/zdus1D6MXayuQgVjyo1c=",
           "rememberMe": 0}
    res = Http_request(url, 'post', dat).do_request()
    print(res)
