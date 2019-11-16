'''
Phantomjs 是一款浏览器，是无界面的浏览器：
selenium+phantomjs 就是爬虫终极解决问题

下拉滚动条到底部
	豆瓣电影下拉
图片加载:
	获取网页的源代码：page_source
'''
from selenium import webdriver 
import time

# 创建浏览器对象
path = r'C:\Users\m1552\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(executable_path = path)

# url = 'http://www.baidu.com/'
# browser.get(url)

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
browser.get(url)

time.sleep(2)
browser.save_screenshot(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\douban.png')
time.sleep(2)

# # 让browser执行简单的JS代码，模拟滚动条滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(3)
browser.save_screenshot(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\douban2.png')
# time.sleep(2)

# 获取网页的源代码，保存到文件中
html = browser.page_source
# print(html)

with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\jingdong.txt', 'w', encoding="utf8") as fp:
	fp.write(html)

browser.quit()