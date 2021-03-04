# -*- coding:utf-8 -*-
from test_ui_app.page._base import BasePage
from test_ui_app.tools.smalltools import pagesteps, projectname
from test_ui_app.page.findmore_page import FindMorePage

step: dict = pagesteps(projectname+"\\test_ui_app\\datafile\\xueqiudatafor_page.yml")


class FindMarketIdPage(BasePage):

    def togofindmorepage(self, a):
        step['HomePage']['findMarkect1']['value'] = a

        self.steps(**(step['HomePage']['findMarkect1']))
        self.steps(**(step['HomePage']['findMarkect2']))
        self.steps(**(step['HomePage']['findMarkect3']))
        return FindMorePage(self.driver)