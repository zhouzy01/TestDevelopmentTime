# -*- coding:utf-8 -*-
from test_ui_app.page._appinit import App
import pytest,allure,sys,time
from test_ui_app.tools.smalltools import projectname


@allure.feature("app 模块")
class Test_homepage:
    def setup_class(self):
        self.start = App()

    def setup(self):
        self.homepage = self.start.start().gotoHomePage()

    def teardown_class(self):
        self.start.stop()

    @pytest.mark.parametrize(('a' ), {'600673', })
    def test_findmarket(self, a):
        temp = self.homepage.gotoFindMarketIdPage().togofindmorepage(a).gotoMarketDetailPage().getmarketid()
        assert a == temp

    @pytest.mark.parametrize(('a' ), {'600673', })
    def test_marketdetaildata(self, a):

        tempname = projectname + "\\test_ui_app\\picture\\" + sys._getframe().f_code.co_name + "_" + str(int(time.time())) + '.png'
        self.start.driver.save_screenshot(tempname)
        print("已经截屏咯=========0")
        time.sleep(2)
        self.start.driver.get_screenshot_as_file(tempname)
        print("已经截屏咯=========1")
        # allure.attach("进入百度以后",  name=tempname, attachment_type=allure.attachment_type.PNG)
        allure.attach.file(tempname, name=tempname, attachment_type=allure.attachment_type.PNG)
        temp = self.homepage.gotoFindMarketIdPage().togofindmorepage(a).gotoMarketDetailPage().intomarkectdetaildata().getmarkectdetailtaital()
        assert "行情数据" == temp

    def test_mytest(self):
        assert "w" == "w"

    def test_mytest1(self):
        assert "a" == "w"

    def test_mytest2(self):
        assert "w" == "w"

    def test_mytest3(self):
        assert "w" == "w"

    def test_mytest4(self):
        assert "w" == "w"