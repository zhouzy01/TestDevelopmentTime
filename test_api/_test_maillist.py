# -*-coding:utf-8 -*-

import requests
from test_api.api.get_token import get_token


class TestMailList:
    """
    get,一般放在params中就好
    post一般可以放在json = you dict
    """
    # def setup(self):
    #     self.thtoken = get_token()

    def test_creatmember(self, get_token, userid, mobile):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        data:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token="+get_token
        request_body = {
            "userid": userid,
            "name": "lisi",
            "alias": "lis",
            "mobile": mobile,
            "department": [1, 2],
        }
        re = requests.post(url, json=request_body)
        print(re.json())
        print(re.request.body)
        return re.json()

    def test_readmember(self, get_token, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        get
                data:
                :return:
                """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        request_body = {
            "access_token": get_token,
            "userid": userid,
        }
        re = requests.get(url, params=request_body)
        print(re.content)
        print(re.json())
        return re.json()

    def test_updatemember(self, get_token, userid, name, position, mobile):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        data:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token="+get_token
        request_body = {
            "userid": userid,
            "name": name,
            "department": [1],
            "order": [10],
            "position": position,
            "mobile": mobile,
        }
        re = requests.post(url, json=request_body)
        print(re.json())
        return

    def test_detelmember(self, get_token, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID

                data:
                :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        request_body = {
            "access_token":  get_token,
            "userid": userid,
        }
        re = requests.get(url, params=request_body)
        print(re.json())
        return re.json()

    def test_alloff(self, get_token):
        """
        集成性测试，上边是单接口测试
        :return:
        """
        userid = "testuser"
        mobile = "+86 15555555555"
        name = "帅气"
        position = "高级测试工程师"
        try:
            assert "" == self.test_creatmember(get_token, userid=userid, mobile=mobile)[""]
        except Exception as e:
            self.test_detelmember(get_token, userid=userid)
            self.test_creatmember(get_token, userid=userid, mobile=mobile)
        self.test_readmember(get_token, userid=userid)
        self.test_updatemember(get_token, userid=userid, name=name, position=position, mobile=mobile)
        self.test_detelmember(get_token, userid=userid)
