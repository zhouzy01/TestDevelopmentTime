import sys
import time
import allure
sys.path.append("E:\python\Workspace\TestDevelopmentTime")
from test_ui_app.page._appinit import App


class Test_download_filelist:
    poto = None

    def setup(self):
        self.start = App()
        self.home = self.start.start().gotoHomePage()

    # 进入离线下载页面
    @allure.feature("文件下载页面")
    def test_goin_filelistpage(self):
        # self.home.go_to_mypage().go_to_download()
        thpage = self.home.go_to_mypage().go_to_download()
        time.sleep(2)
        self.poto = "E:\python\Workspace\TestDevelopmentTime\\test_ui_app\pictures" + __name__ + time.strftime("%Y%m%d%H%M%S", time.localtime())+".png"
        self.start.pageShoot(self.poto)
        allure.attach.file(self.poto, attachment_type=allure.attachment_type.PNG)
        assert "离线下载" in thpage.get_pagesours()