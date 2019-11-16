'''
将网站的标题和内容爬取下来
'''

import urllib.request
import urllib.parse
import re


def get_text(url, title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.132 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read().decode()
    # 写一个正则移除网页中的全部图片
    # pattern_s = re.compile(r'<img src=".*?" title=".*?" alt=".*?" .*?>')
    # pattern_s.sub('', response)
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    lt = pattern.findall(response)
    # print(lt)
    with open('lizhi.html', 'a', encoding='utf8') as fp:
        fp.write(title + '\n\n\n' + lt[0])


def response_buile(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.132 Safari/537.36',
    }
    # 构建请求
    request = urllib.request.Request(url=url, headers=headers)
    # 获取响应
    response = urllib.request.urlopen(request).read().decode()
    # print(response)
    # 构建正则表达式进行筛选
    pattern = re.compile(r'<li>.*?<a href="(.*?).html">(.*?)</a>.*?</li>', re.S)
    lt = pattern.findall(response)
    # print(lt)
    for it in lt:
        url_g = 'http://www.yikexun.cn' + it[0] + '.html'
        # print(url_g)
        get_text(url_g, it[-1])


def main():
    url = 'http://www.yikexun.cn/niandujingdianyulu/2013yulu/list_60_'
    # 构建请求网页中共同的部分http://www.yikexun.cn/niandujingdianyulu/2013yulu/list_60_1.html
    print("一点点语录网爬取！！")
    start_page = int(input("请输入需要爬取的起始页码："))
    end_page = int(input("请输入需要爬取的结束页码："))
    for page in range(start_page, end_page + 1):
        print("正在爬取第%s页", str(page))
        # 构建完整的url
        url_t = url + str(page) + '.html'
        # print(url_t)
        # 根据url构建请求获取响应
        response_buile(url_t)


main()
