# -*- coding:utf-8 -*-
from test_ui_app.page._base import BasePage
from test_ui_app.page.marketdetail_page import MarketDetailPage
from test_ui_app.tools.smalltools import pagesteps, projectname

step: dict = pagesteps(projectname+"\\test_ui_app\\datafile\\xueqiudatafor_page.yml")


class FindMorePage(BasePage):  # 综合查询页面
    # 点击查询出来的内容（股票），进入股票详情
    def gotoMarketDetailPage(self):
        self.steps(**(step['HomePage']['findMarkect4']))
        return MarketDetailPage(self.driver)