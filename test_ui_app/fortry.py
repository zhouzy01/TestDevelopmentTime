# -*- coding-utf-8 -*-
import sys


def aaa():
    print(sys._getframe().f_code.co_name)
    print("in aaa")

def bbb():
    aaa()

bbb()