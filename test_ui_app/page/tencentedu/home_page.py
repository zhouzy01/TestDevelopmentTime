from test_ui_app.page._base import BasePage
from test_ui_app.page.tencentedu.my_page import MyPage
from appium.webdriver.common.mobileby import By


class HomePage(BasePage):

    def go_to_mypage(self):
        self.click(By.XPATH, "//*[@content-desc='我的']")
        return MyPage(self.driver)

