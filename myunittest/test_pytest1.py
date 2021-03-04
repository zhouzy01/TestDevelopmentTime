# -*- coding:utf-8 -*-

import pytest
import logging
import yaml
import allure
import sys
import os
thdir = os.getcwd().split("TestDevelopmentTime")[0]+"TestDevelopmentTime"
sys.path.append(thdir)

def work(a):
    print("work()")
    return a


@pytest.fixture()
def sehello():
    print("hello start a case")


class Test_Pytest1:
    def setup(self):
        logging.basicConfig(level=logging.INFO, format= "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        logging.info("-setup-")
        print("here is setup")

    @pytest.mark.parametrize('a, b', [(1, 1), (2, 3), ('a', 'a')])
    def test_work(self, a, b):
        assert work(a) == b

    @pytest.mark.parametrize('a, b', yaml.safe_load(open(thdir+"/myunittest/test_pytest1.yml")))
    def test_work_1(self, a, b):
        print(yaml.safe_load(open("./test_pytest1.yml")))
        assert work(a) == b

    @allure.severity(allure.severity_level.NORMAL)
    def test_work_3(self, sehello):
        print("need to login: test fixture")