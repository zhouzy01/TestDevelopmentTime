from appium import webdriver
from test_ui_app.page.home_page import HomePage
from test_ui_app.page._base import BasePage
import time


class App(BasePage):
    # def __init__(self):
    #     self.driver = None

    def start(self):
        """
        启动app
        :return:
        """
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"  # 系统
            caps["deviceName"] = "Mumu"
            caps["appPackage"] = "com.xueqiu.android"  # 包名
            caps["appActivity"] = ".view.WelcomeActivityAlias"  # 活动名
            caps["noReset"] = "true"  # 不重置
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            # caps['dontStopAppOnReset'] = 'true'  # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0

            # 1)与server 建立连接,2)初始化一个driver 创建session,返回一个sessionid
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            time.sleep(2)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
            # self.driver.find_element().send_keys()
        self.driver.implicitly_wait(20)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def gotoHomePage(self):
        return HomePage(self.driver)


if __name__ == '__main__':
    myapp = App()
    myapp.start()