from test_ui_app.page._base import BasePage
from appium.webdriver.common.mobileby import By
import time


class DownLoadFileListPage(BasePage):
    """
    课程列表
    """
    def getpage(self):
        time.sleep(2)
        return self.driver.page_source

    def getalltext(self):
        namelist = self.getelementstext(By.ID, "com.tencent.edu:id/ae6")
        datalist = self.getelementstext(By.ID, "com.tencent.edu:id/aak")
        return namelist, datalist

    def tomoveup(self):
        # 滑动屏幕
        return self.moveup(By.XPATH, "//android.widget.ListView")

    # def elemoveup(self, xpathstr1,  xpathstr2):
    #     # 滑动屏幕
    #     return self.pressmoveup(By.XPATH, xpathstr1, xpathstr2)

    def xymoveup(self):
        # 滑动屏幕
        return self.pressXymoveup()
