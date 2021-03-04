from test_ui_app.page._base import BasePage
from test_ui_app.page.tencentedu.download_list_page import DownLoadFileListPage
from appium.webdriver.common.mobileby import By
import time


class DownLoadPage(BasePage):
    """
    离线下载页面 （列表）
    """
    def goto_downloadlist_page(self):
        self.click(By.XPATH, "//*[@text='第14期  霍格沃兹测试学院']")
        return DownLoadFileListPage(self.driver)

    def get_pagesours(self):
        time.sleep(2)
        return self.gettext()
