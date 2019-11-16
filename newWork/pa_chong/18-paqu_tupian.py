'''
俩个新的知识点：
1.懒加载：
	用户在前端浏览图片的时候不是一打开页面就全部加载，而是进入界面范围才加载
	因此，在img属性的src属性被改成src2，当js触发时才将src2变成src
2.提取基址：
	可以利用os中的 os.path.basename('地址') 提取路径中的基地址
'''
import urllib.request
import urllib.parse
import os
from lxml import etree


def handel_request(url):
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
	}
	return urllib.request.Request(url, headers=headers)


def down_img(path):
	if not os.path.exists("paqu_picters"):
		os.mkdir("paqu_picters")
	picters_name = os.path.basename(path)
	request = handel_request(path)
	response = urllib.request.urlopen(path).read()
	with open("paqu_picters/"+picters_name, 'wb') as fp:
		fp.write(response)


def parse_content(response):
	tree = etree.HTML(response)
	filepath = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
	for path in filepath:
		# print(os.path.basename(path))	
		down_img(path)


def main():
	url = 'http://sc.chinaz.com/tupian/meinvxiezhen{0}.html'
	start_page = int(input("请您输入您要开始爬取的页数："))
	end_page = int(input("请您输入您要爬取的最后页数："))
	for page in range(start_page, end_page+1):
		if(page == 1):
			url_t = url.format('')
		else:
			url_t = url.format('_'+str(page))
		request = handel_request(url_t)
		response = urllib.request.urlopen(request).read().decode()
		parse_content(response)


main()