'''
1.爬虫概念：
在互联网上抓取数据。
2.哪些语言可以做爬虫？
（1）php，可以做，但是多进程，多线程支持的不好
（2）java，也可以做爬虫，但是代码冗余量大，重构成本大
（3）c、c++ 需要高能力，并非是好的选择
（4）python 语法简单，代码优美，学习成本低，支持的模块多，非常强大的框架scrapy。
通用爬虫：百度、360、搜狐、谷歌、必应
原理：
    （1）抓取网页
    （2）采集数据
    （3）数据处理
    （4）提供检索服务
    爬虫：baiduspider
    如何抓取新网站？
    （1）主动提交url
    （2）设置友情链接
    （3）百度会和DNS服务商合作，抓取新网站
    检索排名：
        竞价排名
        根据pagerrank值、访问量、点击量（SEO）
    robots.txt
        不想让百度爬取，可以编写robots.txt 自己写的程序不需要遵守这个协议
聚焦爬虫：
    根据特定的需求，抓取指定的数据
    思路：
        代替浏览器上网
        网页的特点：
            （1）网页都有自己唯一的url
            （2）网页的内容都是html结构
            （3）使用的都是http、https协议
        爬虫步骤
        （1）给一个url
        (2）写程序，模拟浏览器访问url
        （3）解析内容 ，提取数据
3.http协议
    什么是协议？双方规定的传输形式
    http协议：网站原理
        应用层的协议  ftp（21）
    http(80)\https(443) SSH(22)
    HTTP 和 HTTPS的区别主要如下：
    1、https协议需要到ca申请证书，一般免费证书比较少，因而需要一定费用
    2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议
    https=http+ssl
4、fiddler
    1、配置
        tools==>options==>https
        选中：
    2、抓包
        <> : html内容
        {json}:json数据，很有可能是个接口
        {css}:css文件
        {js}:js文件

        停止抓取：file==》capture  点击就切换

        点击请求，右边选中Inspectors
        右上：http请求信息
            raw：请求头部的详细信息
            webforms:请求所带参数
        右下：http响应信息
            点击黄色条进行解码
            raw：响应的所有信息
            header：响应头
            json：接口返回的内容、
        左下黑框，输入指令
            clear：清除所有请求
            select json：快速选择所有json请求
            select image：图片请求
            select html：html请求
            内容：搜索包括这个内容的所有请求。
5、urllib库：
    模拟浏览器发送请求的库，python自带
    python2：urllib  urllib2
    python3：urllib.request  urllib.parse

    字符串==》 二进制字符串之间的转化
        encode()   编码
        decode()    解码
            括号里面不写默认是utf-8
            写的话就写 GBK

    urllib.request
        urlopen（url)
        urlretrieve(url,image_path)
    urllib.parse
    	quote	url编码函数
    	unquote		url解码函数
    	urlencode 	给一个字典，将字典拼接为query_string,并且实现了编码的功能（详见2）
    response
        read()       读取想要的内容，内容是字节类型
        geturl()        根据响应内容获取请求的url
        getheaders()    获取头部信息
        getcode()       获取状态码
        readlines()     按行获取

5、get方式
6、构建请求头部信息（反爬第一部）
	伪装自己的UA，让服务器认为是浏览器请求
'''

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# url = 'http://www.baidu.com'
# respond = urllib.request.urlopen(url)
#
# print(respond.getheaders())
img_url = 'https://i.meizitu.net/2018/12/28d08.jpg'

# response = urllib.request.urlopenimg_url)
# print(response.read())
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                   ' Chrome/69.0.3497.100 Safari/537.36',
}

ret_url = urllib.request.Request(url=img_url, headers=headers)

# with open('qing', 'wb') as fp:
# 	fp.write(response.read())
# print(ret_url.get_full_url())
urllib.request.urlretrieve(ret_url.get_full_url(), 'chun3.jpg')