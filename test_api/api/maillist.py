# -*-coding:utf-8 -*-

import requests
from test_api.api.get_token import get_token
from test_api.api.base import BaseApi
from test_api.api.get_token import get_token
import yaml,os



class MailList(BaseApi):
    """
    get,一般放在params中就好
    post一般可以放在json = you dict
    """
    def __init__(self):
        self.casedata["token"] = get_token()
        with open(os.getcwd().split("TestDevelopmentTime")[0]+"TestDevelopmentTime\\test_api\\api\\maillist.yml") as f:
            self.data = yaml.safe_load(f)
            # print(type(self.data))
            # print(self.data)

    def creatmember(self, userid, mobile):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        data:
        :return:
        """
        self.casedata["userid"] = userid
        self.casedata["mobile"] = mobile
        data = self.data["creatmember"]
        return self.sedrequst(**data)

    def readmember(self, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        get
                data:
                :return:
                """
        self.casedata["userid"] = userid
        data = self.data["readmember"]
        return self.sedrequst(**data)

    def updatemember(self, userid, name, position, mobile):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        data:
        :return:
        """
        self.casedata["userid"] = userid
        self.casedata["name"] = name
        self.casedata["position"] = position
        self.casedata["mobile"] = mobile
        data = self.data["updatemember"]
        return self.sedrequst(**data)

    def detelmember(self, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID

                data:
                :return:
        """
        self.casedata["userid"] = userid
        data = self.data["detelmember"]
        return self.sedrequst(**data)

    def alloff(self, get_token):
        """
        集成性测试，上边是单接口测试
        :return:
        """
        userid = "testuser"
        mobile = "+86 15555555555"
        name = "帅气"
        position = "高级测试工程师"
        try:
            assert "" == self.creatmember(get_token, userid=userid, mobile=mobile)[""]
        except Exception as e:
            self.detelmember(get_token, userid=userid)
            self.creatmember(get_token, userid=userid, mobile=mobile)
        self.readmember(get_token, userid=userid)
        self.updatemember(get_token, userid=userid, name=name, position=position, mobile=mobile)
        self.detelmember(get_token, userid=userid)
