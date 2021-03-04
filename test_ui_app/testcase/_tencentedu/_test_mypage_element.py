import sys
sys.path.append("E:\python\Workspace\TestDevelopmentTime")
from test_ui_app.page._appinit import App


class Test_download_filelist:
    def setup(self):
        self.start = App()
        self.home = self.start.start().gotoHomePage()

    # 进入离线下载页面
    def test_goin_filelistpage(self):
        self.home.go_to_mypage().go_to_download()
        assert "余额" in self.home.go_to_mypage().gettext()