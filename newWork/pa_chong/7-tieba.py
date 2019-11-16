'''
复杂的get:
'''

import urllib.request
import urllib.parse
import os

url = 'http://tieba.baidu.com/f?ie=utf-8&'

ba_name = input("请输入您要查找的吧名：")
start_page = int(input("请输入您要查找的起始页数"))
end_page = int(input("请输入您要查找的结束页数"))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)

# 在循环中依次爬取每一页的数据
for page in range(start_page, end_page + 1):
    # 利用page这个当前页拼接url的过程
    data = {
        'kw': ba_name,
        'pn': (page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    url_t = url + data
    print(url_t)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.132 Safari/537.36',
    }
    url_t = urllib.request.Request(url_t, headers=headers)
    print("第%s页开始下载......" % page)
    response = urllib.request.urlopen(url_t)
    filename = ba_name + '_' + str(page) + '.html'
    filepath = ba_name + '/' + filename

    with open(filepath, 'wb') as fp:
        fp.write(response.read())
    print("第%s页下载完毕......" % page)