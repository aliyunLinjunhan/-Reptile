import urllib.request
import urllib.parse
from lxml import etree
import os

def handel_request(url, page):
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36'
	}
	url = url + str(page) + '/'
	return urllib.request.Request(url, headers=headers)

def parse_response(response):
	tree = etree.HTML(response)
	articles = tree.xpath('//article')
	for article in articles:
		title = article.xpath('./div/h1//text()')
		content = article.xpath('.//p//text()')
		final_content = title[0] + '\n' + '\t'.join(content) + '\n'
		with open('duanzi.html', 'a') as fp:
			fp.write(final_content)

def main():
	url = 'http://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/'
	start_page = int(input("请输入您要搜索的开始页码："))
	end_page = int(input("请输入您要搜索的结束页码："))
	for page in range(start_page, end_page + 1):
		request = handel_request(url, page)
		response = urllib.request.urlopen(request).read().decode()
		parse_response(response)

main()