import urllib.request
import urllib.parse
import http.cookiejar

# 模拟真实的浏览器，当发生完post请求的时候，将cookie保存到代码中
cj = http.cookiejar.CookieJar()
# 通过 cookiejar 创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 通过handler创建opener
opener = urllib.request.build_opener(handler)

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019001240179'
data = {
    'email': '15521093428',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '86043d5b0132f5f5d3f461d6d5ccf4d4b3b40d557828f70e8b08de02dcb01ecf',
    'rkey': '4a08d7117a9b2c2e1ad82f6c5dad748b',
    'f': 'http%3A%2F%2Fguide.renren.com%2Ffillinfonew',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

data = urllib.parse.urlencode(data).encode()
request = urllib.request.Request(post_url, headers=headers)

response = opener.open(request, data=data)

url = 'http://www.renren.com/969499615/profile'

request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
with open('renrenwang2.html', 'wb') as fp:
    fp.write(response.read())