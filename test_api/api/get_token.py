# -*-coding:utf-8 -*-

import requests
import pytest


# @pytest.fixture(scope="module")
def get_token():
    qyid = 'ww893fe21550f5e1d1'
    secret = 'cGH49djACs0X3xYfrjIx2CliAkRPNospBMKGBVJil80'

    re = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+qyid+"&corpsecret=" + secret)
    # print(re)
    # print(re.json())
    return re.json()['access_token']


@pytest.mark.parametrize("get_token", {("a", "a"),  ("b", "b")}, indirect=True)
def test_1(get_token):
    print("test_1")
    print(get_token)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index, item in enumerate(nums):
        if (target - item) in hashmap.keys():
            return hashmap[target - item], index
        hashmap[item] = index


def myfilelock():
    pass


if __name__ =="__main__":
    print(twoSum([2, 4, 2, 3, 7], 10))



