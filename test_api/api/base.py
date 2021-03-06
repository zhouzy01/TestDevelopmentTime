# -*- coding:utf-8 -*-
import requests
import json

class BaseApi:
    casedata = {}

    def sedrequst(self, **data):
        temp = json.dumps(data)
        for key, value in self.casedata.items():
            temp = temp.replace("+{"+key+"}", value)
        data = json.loads(temp)
        print(f"待执行数据：{data}")
        return requests.request(**data)