from appium import webdriver
import time
from test_ui_app.tools.smalltools import projectname


class MoblieWebInit():
    def start(self):
        """
        启动app
        :return:
        """
        caps = {}
        caps["platformName"] = "android"  # 系统
        caps["deviceName"] = "Mumu"
        caps["browserName"] = "Browser"  # 浏览器
        caps["noReset"] = "true"  # 不重置
        caps["chromedriverExecutable"] = "E:\\python\\python\\appiumchromedriver.exe"

        # 1)与server 建立连接,2)初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        time.sleep(2)
        return self.driver
