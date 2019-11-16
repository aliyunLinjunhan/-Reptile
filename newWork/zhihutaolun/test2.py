#
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# from lxml import etree
#
# # 创建一个参数对象，用来控制chrome以无界面模式打开
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--headless')
#
# # 驱动路径
# path = r'C:\Users\Administrator\Desktop\chromedriver.exe'
#
# # 创建浏览器对象
# browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
# url = 'https://www.zhihu.com/question/20034722/answer/238650965'
# browser.get(url)
# time.sleep(1)
#
#
# button = browser.find_elements_by_class_name('Button QuestionRichText-more Button--plain')
# button.click()
#
# time.sleep(1)
# browser.save_screenshot(r'jietu.png')
# browser.close()


from selenium import webdriver
import time

# 创建浏览器对象
path = r'C:\Users\m1552\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(executable_path=path)

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
browser.save_screenshot(r'jietu.png')
# time.sleep(2)

# 获取网页的源代码，保存到文件中
html = browser.page_source
# print(html)

with open(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\jingdong.txt', 'w',
          encoding="utf8") as fp:
    fp.write(html)
