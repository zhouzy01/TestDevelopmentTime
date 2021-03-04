import time

from test_ui_app.page._appinit import App


def getnameselement(filelistpage):
    lastlist = []
    long = 0
    while True:
        time.sleep(0.5)
        namelist, datalist = filelistpage.getalltext()
        print(namelist)
        print(datalist)
        filelistpage.moveup()

        i = 0
        for temp in namelist:
            if temp.split(" ")[0][-1:] == "节":
                i += 1
        if (len(namelist) - i) != len(datalist):
            print("获取数据错误")
            return "获取数据错误"
        else:
            times = len(datalist)
            i, j = 0, 0
            while times > 0:
                if namelist[j].split(" ")[0][-1:] == "节":
                    j += 1
                namelist[j] = [namelist[j], datalist[i]]
                j += 1
                i += 1
                times -= 1
        thlen = len(namelist)
        i = 0
        while i < thlen:
            if namelist[i] not in lastlist:
                lastlist.append(namelist[i])
            i += 1
        temp = long
        long = len(lastlist)
        if temp == long:
            break
    return lastlist


def getnamesSources(filelistpage):
    lastlist = []
    len1 = 0
    while True:
        source = filelistpage.getpage().split("\n")
        thlen = len(source)
        j = 0
        thistimelist = list()
        while j < thlen:
            if (('<android.widget.TextView index="0" package="com.tencent.edu" class="android.widget.TextView" text="' in source[j]) or
                ('<android.widget.TextView index="1" package="com.tencent.edu" class="android.widget.TextView" text="' in source[j])) and \
                 (source[j].split('text="')[1].split('" resource-id=')[0] not in lastlist) and ('软件测试/Python 测试开发实战进阶班' not in source[j]):
                lastlist.append(source[j].split('text="')[1].split('" resource-id=')[0])
            # # 获取本次元素text列表
            # if (('<android.widget.TextView index="0" package="com.tencent.edu" class="android.widget.TextView" text="' in source[j]) or
            #     ('<android.widget.TextView index="1" package="com.tencent.edu" class="android.widget.TextView" text="' in
            #      source[j])) and ('软件测试/Python 测试开发实战进阶班' not in source[j]):
            #     thistimelist.append(source[j].split('text="')[1].split('" resource-id=')[0])
            j += 1

        templen = len1
        len1 = len(lastlist)
        print(lastlist)
        if len1 == templen:
            break
        # filelistpage.moveup()
        # myapp.mylog.info('送两个元素的xpath用于appium滑动操作：' + thistimelist[0] + '&' + thistimelist[-1])
        # filelistpage.elemoveup("//*[@text=\'" + thistimelist[0] + "\']", "//*[@text=\'" + thistimelist[-1] + "\']")
        filelistpage.xymoveup()
        time.sleep(1)
        # i += 1
    return lastlist


def getnameslast(lastlist):
    headlinelist, titlesdict = [], {}
    i = 0
    j = 0
    thlen = len(lastlist)
    tempstr = None
    thx = 0
    while i < thlen:

        if lastlist[i].split(' ')[0][-1:] == '节':
            headlinelist.append(lastlist[i])
            thx = int(lastlist[i].split(' ')[0][:-1])
            j = 0
        elif lastlist[i][-2:] == 'MB':
            j += 1
            if lastlist[i].split('/')[0] not in titlesdict.keys():
                titlesdict[lastlist[i].split('/')[0]] = str(round(thx+j*0.01, 2))+' '+tempstr
            else:
                titlesdict[lastlist[i].split('/')[0]+'_'+str(i)] = str(round(thx + j * 0.01, 2)) + ' ' + tempstr
        tempstr = lastlist[i]
        i += 1
    return headlinelist, titlesdict


if __name__ == "__main__":
    myapp = App()   # 初始化
    myapp.mylog.info("safes ahhhhh")
    #     \启动           \去首页        \去我的页       \去下载页        \去下载列表页           \获取资源
    # print(myapp.start().gotoHomePage().go_to_mypage().go_to_download().goto_downloadlist_page().getpage())
    filelistpage = myapp.start().gotoHomePage().go_to_mypage().go_to_download().goto_downloadlist_page()
    lastlist = getnamesSources(filelistpage)
    print(len(lastlist))
    headlinelist, titlesdict = getnameslast(lastlist)
    print(len(headlinelist))
    print(headlinelist)
    print(titlesdict)





