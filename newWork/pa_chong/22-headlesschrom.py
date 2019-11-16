from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--headless')

# 驱动路径
path = r'C:\Users\m1552\Desktop\chromedriver.exe'

# 创建浏览器对象
browser = webdriver.Chrome(executable_path = path, chrome_options = chrome_options)

# 上网
url = 'http://www.baidu.com'
browser.get(url)
time.sleep(2)

browser.save_screenshot(r'C:\Users\m1552\PycharmProjects\newWork\pa_chong\screenshot_pictures\baidu.png')

browser.quit()