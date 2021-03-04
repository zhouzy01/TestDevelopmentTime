from test_ui_app.page._base import BasePage
from test_ui_app.tools.smalltools import pagesteps, projectname
from test_ui_app.page.hangqing_page import HangqingPage
from test_ui_app.page.findmarketid_Page import FindMarketIdPage

step: dict = pagesteps(projectname+"\\test_ui_app\\datafile\\xueqiudatafor_page.yml")


class HomePage(BasePage):
    def gotoHangqing(self):
        self.steps(**(step['HomePage']['gotoHangqing']))
        return HangqingPage(self.driver)

    # 找到股票代码并进入股票搜索界面
    def gotoFindMarketIdPage(self):
        self.steps(**(step['HomePage']['findMarkect0']))
        return FindMarketIdPage(self.driver)