import requests

'''
headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': 'http://www.renren.com/969499615/profile',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'anonymid=ju5cz9y6529uv5; depovince=GUZ; _r01_=1; JSESSIONID=abcMES0eSN-k_7aYhnYNw; ick_logi'
              'n=c6b77452-01c4-4ead-9da7-c132f5bc6333; jebecookies=e8cc8e94-5c4c-410e-84fe-43e83916855b|||'
              '||; _de=9061F4BBA90AC7E232540B3EF7654E2A; p=ecaade8a87f50daab11931461adb49ee5; first_login_f'
              'lag=1; ln_uact=15521093428; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=5836'
              'a141936692af38e9be04adc579205; societyguester=5836a141936692af38e9be04adc579205; id=96949961'
              '5; xnsid=d98c747; ver=7.0; loginfrom=null; jebe_key=7445034c-e778-40aa-a48e-3318bc9f6e41%7C1'
              '95f1926f11e580b33a17dd9cef3228d%7C1554550047845%7C1%7C1554550050033; wp_fold=0'

}

url = 'https://www.renren.com/969499615/profile'
r = requests.get(url, headers=headers)

with open('renrenwang.html', 'wb') as fp:
    fp.write(r.content)
'''

s = requests.Session()

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019361928772'

dataform = {
    'captcha_type': 'web_login',
    'domain': 'renren.com',
    'email': '15521093428',
    'f': 'http%3A%2F%2Fwww.renren.com%2F969499615%2Fprofile',
    'icode': '',
    'key_id': '1',
    'origURL': 'http://www.renren.com/home',
    'password': '2fe404190c0347f305f59cf8701bfe257a64ff09c95f504ac0f25a865e0f3d81',
    'rkey': 'e37cf7c04307ba10c1b50a9a887570ca',
}

r = s.post(post_url, data=dataform)

r = s.get('http://www.renren.com/969499615')

with open('renrenwang2.html', 'wb') as fp:
    fp.write(r.content)
