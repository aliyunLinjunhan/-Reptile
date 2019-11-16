from selenium import webdriver
import time


if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    browser = webdriver.PhantomJS(executable_path = path)

    url = "https://www.toutiao.com/a6676384961219527181/"
    browser.get(url)
    # # 查找input输入框
    # my_input = browser.find_element_by_id('kw')
    # # 往框里面写文字
    # my_input.send_keys("NBA图")

    time.sleep(2)
    # # 查看搜索按钮
    # button = browser.find_element_by_class_name('s_btn')
    # button.click()
    # time.sleep(2)

    # 让网页滚动到最下面
    js = 'document.body.scrollTop=10000'
    browser.execute_script(js)
    time.sleep(5)

    browser.save_screenshot(r'E:\datas\test\jiepai3.png')
    html = browser.page_source
    with open('jiepai.html', 'w', encoding='utf-8') as fp:
        fp.write(html)

    time.sleep(1)
    browser.quit()

