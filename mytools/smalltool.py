# -*- coding:utf-8 -*-


def highlight(element, driver):
    def apply_style(element, driver):
        js = "arguments[0].style.border='6px solid red'"

        # 实现的方式很简单，就是定位到元素后，执行js样式
        driver.execute_script(js, element)
        return element

    # @wraps(func)  # 抄袭
    # def wrapper(self, *args, **kwargs):
    #     element = func(self, *args, **kwargs)
    #
    #     apply_style(element)
    #     return element

    return apply_style(element, driver)
