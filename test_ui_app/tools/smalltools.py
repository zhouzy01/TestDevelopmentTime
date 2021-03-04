import sys, os
import yaml

projectname = (lambda : os.getcwd().split("TestDevelopmentTime")[0]+"TestDevelopmentTime")()


def pagesteps(filename):
    with open(filename, encoding='utf-8') as f:
        steps = yaml.safe_load(f)
        print(f"-- 进入读取{filename}文件 --")
        print(steps)
    return steps