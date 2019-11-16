'''
cookie是什么？
    http 协议，无状态
    网站登录时候的问题，用来记录身份的模拟登录，相当于给用户的一套身份证。

    模拟登录
    重点：在合适的请求响应中获取cookie，一般在点击涉及用户信息的请求中可以获取用户的cookie。
'''
import urllib.request
import urllib.parse

url = 'http://www.renren.com/969499615/profile'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie': 'anonymid=jr3mavy6-2yhg7z; depovince=ZGQT; _r01_=1; _ga=GA1.2.1316689756.1547911144; _'
              'gid=GA1.2.1818004214.1547911144; JSESSIONID=abcrFAr_Sa7fPe-QRsPHw; ick_login=39446524-'
              '260f-4714-a3d6-8bdb9ff6a681; wp_fold=0; ick=5535a436-9f63-4ed5-94ce-0174d2c49a68; jebec'
              'ookies=3ff6473a-f7f1-4105-8c9d-74715ff4c090|||||; _de=9061F4BBA90AC7E232540B3EF7654E2A; '
              'p=e4a38e1cefd35bd2e1bb5e462b25d9265; first_login_flag=1; ln_uact=15521093428; ln_hurl=ht'
              'tp://head.xiaonei.com/photos/0/0/men_main.gif; t=bdb9b7e1fe466769655943e20e4384d35; socie'
              'tyguester=bdb9b7e1fe466769655943e20e4384d35; id=969499615; xnsid=966de04a; ver=7.0; loginf'
              'rom=null; jebe_key=4b6c9289-4279-4d5b-a730-8bb81705b3f4%7C195f1926f11e580b33a17dd9cef3228d'
              '%7C1547959411717%7C1%7C1547959421472',
    'GET': 'http://www.renren.com/969499615/profile HTTP/1.1'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(url)

# print(response.read().decode())
# print('--'*100)
# print(response.read().decode())

with open('renrenwang1.html', 'wb') as fp:
    fp.write(response.read())
