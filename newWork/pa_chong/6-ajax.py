'''

ajax
    get:
'''
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

pag = int(input("请输入您要看到的页数:"))
number = 20

# 构建get参数
data = {
    'start': (pag - 1) * 20,
    'limit': number,
}

# 将gei参数转化为query_string
query_string = urllib.parse.urlencode(data)
print(query_string)

url += query_string

# 伪装UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode())