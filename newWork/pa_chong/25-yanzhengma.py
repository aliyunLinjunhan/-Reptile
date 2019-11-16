'''
解决验证码思路：
1.获取图片手动输入验证码
2.使用tesseract，光学识别
	代码测试：
		pip install pytesseract
		pip install pillow
3.使用第三方人工打码平台
'''
import requests
from lxml import etree

def down_code(s):
	url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
	content = s.get(url)
	tree = etree.HTML(content.text)
	yanzhengma_url = tree.xpath('//img[@id="imgCode"]/@src')[0]
	img_url = 'https://so.gushiwen.org' + yanzhengma_url
	content_code = s.get(img_url)
	with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\code.png', 'wb') as fp:
		fp.write(content_code.content)


def main():
	# 创建会话
	s = requests.Session()
	# 将验证码图片挡下来
	down_code(s)
	# 开始爬取网页
	paqu_code(s)

main()


