'''
安装：pip install requests
官方文档：
	http://www.python-request.org/
用来做什么：
	和urllib在同一个位置

post请求
get请求
ajax get post
定制头部：
	request.get(url, headers=headers, params=data)
响应对象：
	r.text  字符串形式查看响应内容
	r.content   字节类型查看响应内容
	r.encoding   查看或者设置编码类型
	r.status_code    查看状态码
	r.headers  	查看响应头部
	r.url 		查看所请求的url
	r.json 		查看json格式数据

post 请求:
	必应翻译：
	formdata:是一个原生字典
	r = requests.post(url=url, headers=headers, data=formdata)
ajax get post
	和上面的一样
代理：
	r = requests.post(url=url, headers=headers, proxies=proxies)
	proxies = {
		'http': 'http://代理号'
	}
cookie:
	实现人人网登陆
chinaunix:
	登陆思路：
	1.get
	2.post
	3.get
	由于在第二步post中，表单数据每一次访问网站都不一样，所以要先通过get来获取想要的表单值

'''
import requests

url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36'
}
response = requests.get(url, headers=headers)
# print(response)
response.encoding = 'utf-8'
with open(r'requests.txt', 'w', encoding = 'utf-8') as fp:
	fp.write(response.text)



# # # 带参数的get
# url = 'https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD'
# data = {
# 	'wd':'%E4%B8%AD%E5%9B%BD',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/63.0.3239.132 Safari/537.36'
# }
#
# # parameters参数
# response = requests.get(url, headers=headers, params=data)
# response.encoding = 'utf-8'
# print(response.content)
#
# # # 把结果写入到文件
# # with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\baidu.html', 'wb') as fp:
# # 	fp.write(response.content)
#
#
#
# # post 请求
# import json
# url = 'https://cn.bing.com/ttranslationlookup?&IG=DF5310683E534917A8E04ECAF4BE95D7&IID=translator.5038.4'
# data = {
# 	'from':'en',
# 	'to':'zh-CHS',
# 	'text':'computer',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/63.0.3239.132 Safari/537.36'
# }
#
# response = requests.post(url=url, headers=headers, data=data)
#
# with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\computer.txt', 'w', encoding='utf8') as fp:
# 	fp.write(json.dumps(response.json()))