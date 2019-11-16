'''
有时候仅仅伪装User-Agent(简称UA）是不够的，还需要伪装全部的原生信息
'''

import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
word = input("请输入您要查询的英文单词：")
from_data = {
    'from': 'en',
    'to': 'zh',
    'query': 'wolf',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '275695.55262',
    'token': '5eb650ac4d089f39824c985a5be3eddf',
}

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/63.0.3239.132 Safari/537.36',
# }

headers = {
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '120',
    'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 这是数据包可接受的压缩方式，一般情况下将其去掉不做压缩
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=68393D21286EBF4A001B4E0FCA70F07F:FG=1; PSTM=1539614412; BIDUPSID=A4E0DC66251C305F80AB5BA6B0624EA5;',
}

request = urllib.request.Request(url=post_url, headers=headers)

from_data = urllib.parse.urlencode(from_data)

response = urllib.request.urlopen(request, data=from_data.encode())

print(response.read().decode())
