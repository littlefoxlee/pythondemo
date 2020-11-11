# print("Hello world")

# c)以下为导入要用的包
import sys
import json
import urllib.request as HttpUtils
from bs4 import BeautifulSoup

# 设定函数名
def gethtml(page):
    # 获取指定页码的网页数据
    url = 'http://www.greenpeace.org.cn/news/releases/'
    values = {
        'page': page
    }
    # 使用 DebugLog 获得调试内容
    # httphandler = HttpUtils.HTTPHandler(debuglevel=1)
    # httpshandler = HttpUtils.HTTPSHandler(debuglevel=1)
    # opener = HttpUtils.build_opener(httphandler, httpshandler)
    # HttpUtils.install_opener(opener)

    # d)请求目标网页
    request = HttpUtils.Request(url + 'page/' + str(page))
    request.get_method = lambda: 'GET'
    
    # e)获取目标网页内容
    response = HttpUtils.urlopen(request, timeout=10)
    
    # g)创建csv文件保存数据
    htmlfile = open("output.csv","w",encoding='utf_8_sig')
    # f)解析html页面内容
    soup = BeautifulSoup(response, 'html.parser')
    # f)解析新闻标题，循环输出
    for news in soup.find_all("h3", class_="teaser-title title"):
        htmlfile.write(news.a.get_text()+'\r\n')
    # g)关闭文件保存
    htmlfile.close()

    return

# a)调用函数
gethtml(3)