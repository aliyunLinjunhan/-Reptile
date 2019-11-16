import requests
from lxml import etree
from requests.exceptions import RequestException
import time
import re

url = 'https://www.gushiwen.org/'

headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
}


def second_parse(url):
    if url.startswith('https'):
        pass
    else:
        url = "https://so.gushiwen.org" + url
    try:
        source_code = requests.get(url, headers=headers)
        if source_code.status_code == 200:
            pattren = re.compile('<div class="contson" id="(.*?)">')
            id = pattren.findall(source_code.text)
            # print(id[0])
            tree = etree.HTML(source_code.content)
            # 解析诗文名称
            title = tree.xpath('//div[@class="cont"]/h1/text()')
            # 解析朝代
            dynasty = tree.xpath('//div[@class="cont"]/p/a/text()')[0]
            # 解析作者
            author = tree.xpath('//div[@class="cont"]/p/a/text()')[1]
            # 解析诗文内容
            content = tree.xpath('//div[@id="' + id[0] + '"]//text()')
            print(content)
            # 解析译文和注释
            translation = tree.xpath('//div[@class="sons"]/div[@class="contyishang"]/p/text()')
            # 爬取点赞量
            good_amount = tree.xpath('//div[@class="good"]/a/span/text()')[0]
            pattren2 = re.compile('([0-9]+)')
            good_amount = pattren2.findall(good_amount)[0]
            # # 解析赏析
            # appreciation = tree.xpath('')
            message = {}
            message["诗文名称"] = title[0]
            message["点赞量"] = good_amount
            message["诗文朝代"] = dynasty
            message["诗文内容"] = content
            message["诗文作者"] = author
            message["诗文译文和注释"] = translation
            print(message)
            try:
                with open('siwen_message.txt', 'a+', encoding="utf-8") as fp:
                    fp.write(str(message) + '\n')
            except IOError as err:
                print("文件写入失败")
    except RequestException:
        print("响应请求失败")


def first_parse(url):
    try:
        source_code = requests.get(url, headers=headers)
        if source_code.status_code == 200:
            tree = etree.HTML(source_code.content)
            second_type = tree.xpath('//div[@class="typecont"]/span/a/text()')
            print(second_type)
            second_url = tree.xpath('//div[@class="typecont"]/span/a/@href')
            print(second_url)
            # i = 0
            # while (i < 10):
            #     del second_type[0]
            #     del second_url[0]
            #     i = i + 1
            print(len(second_type))
            print(len(second_url))
            for a, b in zip(second_url, second_type):
                print(a + "    " + b)
                print("开始爬取{}".format(b))
                time.sleep(0.3)
                second_parse(a)
    except RequestException:
        print("响应请求失败")


if __name__ == "__main__":
    try:
        url = 'https://www.gushiwen.org/shiwen/'
        source_code = requests.get(url, headers=headers)
        if source_code.status_code == 200:
            tree = etree.HTML(source_code.content)
            gushiwen_type = tree.xpath('//div[@class="cont"]/a/text()')
            print(gushiwen_type)
            print(len(gushiwen_type))
            gushiwen_url = tree.xpath('//div[@class="cont"]/a/@href')
            print(gushiwen_url)
            print(len(gushiwen_url))
            i = 0
            while(i < 50  ):
                del gushiwen_type[0]
                del gushiwen_url[0]
                i = i + 1
            print("处理后.......")
            print(gushiwen_type)
            print(len(gushiwen_type))
            print(gushiwen_url)
            print(len(gushiwen_url))



            for type, url in zip(gushiwen_type, gushiwen_url):
                print(".....................开始爬取{}......................".format(type))
                first_parse(url)
                print(".....................结束爬取{}....................".format(type))

        # first_parse(url)
    except RequestException:
        print("响应请求失败")
    # with open('gushiwen.html', 'wb') as fp:
    #     fp.write(source_code.content)
