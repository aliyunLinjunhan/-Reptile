import requests
from lxml import etree
import re
import pymysql.cursors
key = '二维码'
key2 = '相关阅读'

def second_parse(url, title, xiao_title):
    url_t = "http://www.glook.cn" + url
    source_code = requests.get(url_t)
    source_code.encoding = "utf8"
    tree = etree.HTML(source_code.text)
    # 解析字符串
    pattren = re.compile('<p>(.*?)</p>')
    sentences = pattren.findall(source_code.text)
    # print(sentences)
    print(len(sentences))
    for it in sentences:
        it1 = re.sub('[a-zA-Z]', '', it)
        it2 = re.sub('<', '', it1)
        it3 = re.sub('=', '', it2)
        it4 = re.sub('/', '', it3)
        it5 = re.sub('[0-9]', '', it4)
        it6 = re.sub('>', '', it5)
        it7 = re.sub('"', '', it6)
        it8 = re.sub('_', '', it7)
        it9 = re.sub('#', '', it8)
        it10 = re.sub('-', '', it9)
        it11 = re.sub('', '', it10)
        it12 = re.sub('&;', '', it11)
        it13 = re.sub(':', '', it12)
        it14 = re.sub('/.', '', it13)
        it15 = re.sub('[*.]+', '', it14)
        if it15.endswith("：") or key in it15 or key2 in it15:
            pass
        else:
            try:
                with connection.cursor() as cursor:
                    # 执行sql语句，插入记录
                    sql = "INSERT INTO jierizhufu (zhufuyu, keywords) VALUES (%s, %s)"
                    cursor.execute(sql, (it15, title + ' ' + xiao_title))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                pass


def parse_content(title, url):
    print(url, title)
    source_code = requests.get(url)
    source_code.encoding = "utf8"
    tree = etree.HTML(source_code.text)
    # 提取内容
    content = tree.xpath('//div[@id="artlist"]/p/a/text()')
    # 提取网址
    url_c = tree.xpath('//div[@id="artlist"]/p/a/@href')
    for a, b in zip(content, url_c):
        print("开始爬取{}".format(a))
        second_parse(b, title, a)
        print("结束爬取{}".format(a))




if __name__ == "__main__":
    # 连接配置信息
    config = {
        'host': '203.195.244.169',
        'port': 3306,
        'user': 'root',
        'password': 'Wissen123**',
        'db': 'gushi',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 创建连接
    connection = pymysql.connect(**config)
    url = 'http://www.glook.cn/index.html'
    source_code = requests.get(url)
    source_code.encoding = "utf8"
    with open('jieri.html', 'w', encoding="utf8") as fp:
        fp.write(source_code.text)
    tree = etree.HTML(source_code.text)
    # 提取节日类型
    jieri_titles = tree.xpath('//div[@id="hleftdh"]/a/text()')
    # 提取节日相应的url
    jieri_url = tree.xpath('//div[@id="hleftdh"]//a/@href')
    for a, b in zip(jieri_titles, jieri_url):
        print("................开始爬取{}........................".format(a))
        parse_content(a, b)
        print("................结束爬取{}........................".format(a))

    connection.close()
