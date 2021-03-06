# -*-coding:utf-8 -*-
from test_api.api.maillist import MailList
import pytest, allure
import yaml, os, time
import random


class Test_MailList:

    def setup_class(self):
        print("this is Test_MailList setup")
        with open(os.getcwd().split("TestDevelopmentTime")[0]+"TestDevelopmentTime\\test_api\\datas\\test_maillist.yml") as f:
            self.datas = yaml.safe_load(f)

    @pytest.fixture(scope="class")
    def ids_(self):
        self.name = "小A"
        self.id = str(float(time.time())*100000)
        self.mobile = str("155"+"%08d" % random.randint(1, 10000))
        return self.id, self.mobile

    @pytest.mark.dependency(depends=["a"])
    def test_creatmemberagen(self, ids_):
        userid = ids_[0]
        mobile = ids_[1]
        re = MailList().creatmember(userid, mobile).json()
        print(re)
        assert 'created' not in re["errmsg"]

    @pytest.mark.run(order=0)
    @pytest.mark.dependency(name="a")
    def test_creatmember(self, ids_):
        userid = ids_[0]
        mobile = ids_[1]
        re = MailList().creatmember(userid, mobile).json()
        print(re)
        assert 'created' == re["errmsg"]

    @allure.feature("查看模块")
    def test_readmember(self):
        userid = self.datas["test_readmember"]["userid"]
        re = MailList().readmember(userid).json()
        print(re)

    @allure.feature("查看模块")
    def test_readmember1(self):
        userid = self.datas["test_readmember1"]["userid"]
        re = MailList().readmember(userid).json()
        print(re)

    @allure.feature("非礼模块")
    def test_readmember2(self):
        userid = self.datas["test_readmember2"]["userid"]
        re = MailList().readmember(userid).json()
        print(re)

    @allure.feature("非礼模块")
    def test_readmember3(self):
        userid = self.datas["test_readmember2"]["userid"]
        re = MailList().readmember(userid).json()
        print(re)