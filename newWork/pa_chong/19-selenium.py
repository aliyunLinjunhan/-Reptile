'''
selenium:
selenium是python的一个第三方库，对外提供的接口可以操作你的浏览器，
然后让浏览器完成自动化操作。
使用selenium：
	安装selenium库：pip install selenium
	安装驱动：操作谷歌浏览器，首先必须有谷歌浏览器的一个驱动。
	驱动安装网址：
	http://chromedriver.storage.googleapis.com/index.html
	驱动与浏览器映射关系：
	http://blog.csdn.net/huilan_same/article/details/51896672
browser = webdriver.Chrome(path)
browser.get()
browser.quit()


1.id定位：find_element_by_id(self, id_)
2.name定位：find_element_by_name(self, name)
3.class定位：find_element_by_class_name(self, name)
4.tag定位：find_element_by_tag_name(self, name)
5.link定位：find_element_by_link_text(self, link_text)
6.partial_link定位find_element_by_partial_link_text(self, link_text)
7.xpath定位：find_element_by_xpath(self, xpath)
8.css定位：find_element_by_css_selector(self, css_selector）


9.id复数定位find_elements_by_id(self, id_)
10.name复数定位find_elements_by_name(self, name)
11.class复数定位find_elements_by_class_name(self, name)
12.tag复数定位find_elements_by_tag_name(self, name)
13.link复数定位find_elements_by_link_text(self, text)
14.partial_link复数定位find_elements_by_partial_link_text(self, link_text)
15.xpath复数定位find_elements_by_xpath(self, xpath)
16.css复数定位find_elements_by_css_selector(self, css_selector


'''
from selenium import webdriver
import time

# 模拟创建一个浏览器对象，然后通过对象去操作浏览器对象。
path = r'C:\Users\Administrator\Desktop\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)
url = 'http://www.baidu.com/'
browser.get(url)

time.sleep(2)
# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写文字
my_input.send_keys("NBA图")

time.sleep(2)
# 查看搜索按钮
button = browser.find_element_by_class_name('s_btn')
button.click()

# 找到指定的标题
title = browser.find_elements_by    
title.click()

# title.click()
time.sleep(3)
# 关闭浏览器，退出浏览器
browser.quit()

