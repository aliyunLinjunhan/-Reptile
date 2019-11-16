# coding=gbk
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
from lxml import etree
from selenium import webdriver
import time
import os


# 伪装UA头
headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
}


def get_page_index(offset, keyword):
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        # 'timestamp': '1554432736605',
    }
    url = 'https://www.toutiao.com/api/search/content/?'
    try:
        response = requests.get(url, headers=headers, params=data)
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except RequestException:
        print("响应请求失败")



def parse_page_index(html):
    data = json.loads(html)
    urls = []
    if data and 'data' in data.keys():
        for article_url in data.get('data'):
            if article_url.get('article_url') != None:
               urls.append(article_url.get('article_url'))
    return urls


def parse_img(url):
    print("网站url:")
    print(url)
    path = r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    browser = webdriver.PhantomJS(executable_path=path)
    browser.get(url)
    time.sleep(2)

    # 让网页滚动到最下面
    js = 'document.body.scrollTop=10000'
    browser.execute_script(js)
    time.sleep(3)
    # browser.save_screenshot(r'E:\datas\test\jiepai3.png')
    html = browser.page_source
    with open('jiepai.html', 'w', encoding='utf-8') as fp:
        fp.write(html)
    tree = etree.HTML(html)
    img_urls = tree.xpath("//div[@class='article-content']//img/@src")
    img_names = tree.xpath("//div[@class='article-content']//img/@alt")
    n = 0
    for a, b in zip(img_urls, img_names):
        response = requests.get(a)
        name = str(str(b) + str(n) + '.png')
        n = n + 1
        path = r'E:\datas\shishang\{}'.format(name)
        print(path)
        try:
            with open(path, 'wb') as fp:
                fp.write(response.content)
        except IOError as err:
            print("文件写入失败")



if __name__ == '__main__':
    index = 60
    while(index  <= 120):
        print("开始爬取第{}到{}的网站..............".format(index, index+20))
        html = get_page_index(index, "时尚")
        article_urls = parse_page_index(html)
        print("共有{}个网站".format(article_urls.__len__()))
        print(article_urls)
        n = 1
        for article_url in article_urls:
            print("开始爬取第{}个网站.................".format(n))
            parse_img(article_url)
            print("结束爬取第{}个网站.................".format(n))
            n = n + 1
        print("结束爬取第{}到{}的网站...............".format(index, index + 20))
        index = index + 20