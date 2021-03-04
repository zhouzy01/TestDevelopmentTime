# -*- coding:utf-8 -*-
from test_ui_app.page._base import BasePage
from test_ui_app.tools.smalltools import pagesteps, projectname


step: dict = pagesteps(projectname+"\\test_ui_app\\datafile\\xueqiudatafor_page.yml")


class MarketDetailPage(BasePage):

    def getmarketid(self):
        return self.steps(**(step['MarketDetailPage']['getmarketid']))

    def intomarkectdetaildata(self):
        self.steps(**(step['MarketDetailPage']['intomarkectdetaildata']))
        return self

    def getmarkectdetailtaital(self):
        return self.steps(**(step['MarketDetailPage']['getmarkectdetailtaital']))
