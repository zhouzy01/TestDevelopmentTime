from test_ui_app.page.mobilewebinit import MoblieWebInit
import allure


@allure.feature("webview 模块")
class Test_homepage:
    def setup_class(self):
        self.driver = MoblieWebInit().start()

    def setup(self):
        self.driver.get("https://www.baidu.com")

    def teardown_class(self):
        self.driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    def test_baidu(self):
        assert "百度一下" in self.driver.page_source