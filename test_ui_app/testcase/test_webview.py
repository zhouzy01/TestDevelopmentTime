from test_ui_app.page.mobilewebinit import MoblieWebInit


class Test_homepage:
    def setup_class(self):
        self.start = MoblieWebInit()

    def setup(self):
        self.homepage = self.start.start()

    def teardown_class(self):
        self.start.stop()