'''
post
    【注】表单数据的处理：from_data = urllib.parse.urlencode(from_data)
    fiddle抓包上,一个本子上有一个箭头，代表的就是post请求

'''
import urllib.request
import urllib.parse

# 获取posturl的地址
post_url = 'https://fanyi.baidu.com/sug'
word = input("请输入您要查询的英文单词：")

# 构建post表单数据
from_data = {
    'kw': word,
}

# 发送请求的过程
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)

# 处理表单数据
from_data = urllib.parse.urlencode(from_data)

# 发送请求
response = urllib.request.urlopen(request, data=from_data.encode())

print(response.read().decode())
