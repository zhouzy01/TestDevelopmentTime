from test_ui_app.page._base import BasePage
from test_ui_app.page.tencentedu.download_page import DownLoadPage


class MyPage(BasePage):
    """
    我的 页面
    """
    def go_to_download(self):
        # self.click(By.XPATH, "//*[@text='下载管理']")
        self.steps("E:\python\Workspace\TestDevelopmentTime\\test_ui_app\datafile\datafor_page.yml", "my_page.go_to_download")
        return DownLoadPage(self.driver)

    def get_pagesource(self):
        pagesource = self.gettext()
        return pagesource

    def get_eletext(self):
        # self.click(By.XPATH, "//*[@text='下载管理']")
        self.steps("..\\datafile\\xueqiudatafor_page.yml", "my_page.go_to_download")
        return DownLoadPage(self.driver)