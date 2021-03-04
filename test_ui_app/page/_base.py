import time

from appium.webdriver.webdriver import WebDriver
from unittest import TestCase
from appium.webdriver.common.touch_action import TouchAction
from mytools.mylog import Mylog
import yaml,json
from mytools.smalltool import highlight

class BasePage:
    """
    初始化driver
    定义基本操作
    """
    def __init__(self, driver: WebDriver = None):
        self._caseparam = {}
        self.driver = driver
        self.mylog = Mylog()

    def steps(self, **args):
        if ('do' in args) and (args['do'] == 'N'):
            print(f"跳过步骤： {args['note']}")
            return self
        # 延时处理
        if args['later'] is not None:
            time.sleep(int(args['later']))
        print(args)
        print(f"执行步骤：{args['note']}")
        try:
            # 按照步骤描述执行操作， 需根据特定格式
            if args['action'] == 'click':
                self.mylog.info("点击元素：" + args['by'] + "/" + args['locator'])
                self.click(args['by'], args['locator'])
            elif args['action'] == 'send_keys':
                self.sendkeys(args['value'], args['by'], args['locator'])
            elif args['action'] == 'gettext':
                return self.gettext(args['by'], args['locator'])
            else:
                self.mylog.info(f"没有能够执行你要的操作: " +args['note']+'/' + args['by']+'/' + args['locator']+'/' + args['action'])

        except Exception as e:
            self.mylog.info(f"steps 报错: {e}")
        return self

    def find(self, *value):
        # 查找单个元素专用
        ele = None
        try:
            ele = self.driver.find_element(*value)
        except Exception as e:
            self.mylog.info(f"查找元素异常，报错为{e}")
        # highlight(ele, self.driver)
        return ele

    def finds(self, *value):
        return self.driver.find_elements(*value)

    def click(self, *value):
        return self.find(*value).click()

    def keyboseed(self, *value):
        return self.find(*value).click()

    def sendkeys(self, keys, *value):
        return self.find(*value).send_keys(keys)

    def getsource(self):
        time.sleep(2)
        return self.driver.page_source

    def gettext(self, *value):
        # time.sleep(1)
        return self.find(*value).get_attribute("text")

    def getelementstext(self, *value):
        elements = self.finds(*value)
        textlist = []
        templen = len(elements)
        i = 0
        while i < templen:
            textlist.append(elements[i].get_attribute("text"))
            i += 1
        return textlist

    def moveup(self, *value):
        thsize = self.driver.get_window_size()
        x1, y1, x2, y2 = int(thsize['width']*0.5), int(thsize['height']*0.9), int(thsize['width']*0.5), int(thsize['height']*0.5)
        self.driver.swipe(x1, y1, x2, y2)

    # def pressmoveup(self, thtype, value1, value2):
    #     e1 = self.find(thtype, value1)
    #     e2 = self.find(thtype, value2)
    #
    #     temp = TouchAction(self.driver)
    #     temp.long_press(x=359, y=1279, duration=1).move_to(e1).release().perform()

    def pressXymoveup(self):
        thsize = self.driver.get_window_size()
        x1, y1, x2, y2 = int(thsize['width'] * 0.5), int(thsize['height'] * 0.8), int(thsize['width'] * 0.5), int(
            thsize['height'] * 0.2)
        temp = TouchAction(self.driver)
        temp.long_press(x=x1, y=y1, duration=1).move_to(x=x2, y=y2).release().perform()

    def pageShoot(self, paname):
        self.driver.save_screenshot(paname)
