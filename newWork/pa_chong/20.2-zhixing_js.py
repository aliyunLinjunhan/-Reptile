from selenium import webdriver
import time

# 创建浏览器对象
path = r'C:\Users\m1552\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(executable_path = path)

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
browser.get(url)

time.sleep(3)
with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\douban.html', 'w', encoding = 'utf8') as fp:
	fp.write(browser.page_source)

js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(3)
with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\douban2.html', 'w', encoding = 'utf8') as fp:
	fp.write(browser.page_source)

browser.quit()



