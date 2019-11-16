'''
ajax：
post方式
'''

import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

city = input("请输入您要查询的城市:")
page = input("请输入您要查询的页数:")
size = input("请输入您要查询的个数: ")

form = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': page,
    'pageSize': size,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

request = urllib.request.Request(post_url, headers=headers)
form = urllib.parse.urlencode(form)
response = urllib.request.urlopen(post_url, data=form.encode())

print(response.read().decode())
