import requests
import urllib.request
import re

pattren = re.compile(r"http://[a-z]+[0-9].sinaimg.cn/bmiddle/[a-zA-Z0-9.]+(\.[a-z]+)")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}
path = r"C:\Users\Administrator\PycharmProjects\newWork\wenzishibie\name.txt"
fp = open(path, 'a+')
n = 1
for url in open(r"pictures2.txt"):
    print(url)
    name = pattren.findall(url)
    print(name)
    if len(name) > 0:
        name = name[0]
        print(name)

        # response = requests.get(url)
        fp.write(str(n) + name + '\n')
        n = n + 1
