import requests

"""
大奉可用地址
http://www.xbiquge.la/56/56564/
https://www.bqg5.cc/131_131878/
https://www.boquge.com/book/121554/

大周
https://www.9biquge.com/11/11617/
"""
result = requests.get("https://www.9biquge.com/11/11617/")
result.encoding = "utf-8"
x = result.text
print(x)

print("----look-----")

y = x.find("最后更新")


#### 类型B，一个子内容在一行
pp = x[y: y+300]
print(pp)
pplist = pp.split("\n")

for ppstr in pplist:
    tmpstr = str(ppstr).split(" ")
    try:
        if tmpstr[-2].find("第") and tmpstr[-2].find("章"):
            print(tmpstr)
    except Exception:
        pass

#### 类型A，一个内容在一行
# pp = x[y: y+300].split("\n")[1].strip()
# theurl = pp.split("<a href=\"")[1].split("\">")[0]
# theallname = pp.split("\">")[1].split("</a>")[0]
# themath = theallname.split(" ")[0]
# thename = theallname.split(" ")[-1]
# print(pp)
# print(theurl)
# print(theallname)
# print(themath)
# print(thename)

# print(x)
# print("你好吗")
# https://www.jpxs.org/24_24179/
# print(result)

