import requests

# 如果碰到会话相关的问题，要首先创建一个会话。
# 往下所有的操作都通过s进行访问 s.get() s.post()
s = requests.Session()

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191009575'

fromdata = {
	'email':'15521093428',
	'icode':'',
	'origURL':'http://www.renren.com/home',
	'domain':'renren.com',
	'key_id':'1',
	'captcha_type':'web_login',
	'password':'3c493a9b58fc672420b168275078df37bd0b51e3c424cec1e5928d37d3005a4d',
	'rkey':'2de811fa2fc149ce4704d89fcdb84777',
	'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1pi5EUYGZKK9a8cdrLgTUtcEDhxgrPP8IhzTf_vmIsy%26wd%3D%26eqid%3Dd710580c0002a94a000000035c5efa51',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36'
}

response = s.post(url=post_url, headers=headers, data = fromdata)

# print(response.text)

get_url = 'http://www.renren.com/969499615/profile'
response2 = s.get(url = get_url, headers=headers)
print(response2.text)