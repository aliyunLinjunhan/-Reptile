import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = 'https://sou.zhaopin.com/?p=3&jl=%E5%B9%BF%E5%B7%9E&sf=0&st=0&kw=Python&kt=3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
with open('zhilian.html', 'w') as fp: 
    fp.write(response.read().decode())
print(response.read().decode())
