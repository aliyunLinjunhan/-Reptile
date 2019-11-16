import requests
from lxml import etree
import re
import pymysql.cursors


a = set()
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


def second_parse(url):
    '''

    :param url:
    :param titles:
    :return:
    '''
    source_code = requests.get(url)
    source_code.encoding = "utf8"
    tree = etree.HTML(source_code.text)
    sentences = tree.xpath('//div[@class="artCon"]/p/text()')
    print(sentences)
    for it in sentences:
        a = re.sub(r"\n", '', it)
        b = re.sub(r"\r", '', a)
        c = re.sub(r"\t", '', b)
        # print(it)
        if c[:1].isdigit():
            sentence = re.sub('\w+[、.]', '', c)
            print(sentence)
            if len(sentence) > 4:
                # 执行sql语句
                try:
                    with connection.cursor() as cursor:
                    # 执行sql语句，插入记录
                        sql = "INSERT INTO qinghua (sentence, keywords) VALUES (%s, %s)"
                        cursor.execute(sql, (str(sentence), ''))
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                except Exception:
                    print("插入异常")
                finally:
                    pass


def first_parse(url):
    """
    提取网页的主题和地址
    :param url:
    :return:
    """
    source_code = requests.get(url)
    source_code.encoding = "utf8"
    tree = etree.HTML(source_code.text)
    # with open('QQ.html', 'w', encoding="utf8") as fp:
    #     fp.write(source_code.text)
    # 提取主页名称
    titles = tree.xpath('//a[@class="wz_tit"]//text()')
    print(titles)
    # 提取主页地址
    url_titles = tree.xpath('//a[@class="wz_tit"]//@href')
    print(url_titles)
    for a, b in zip(titles, url_titles):
        print("................开始爬取{}...............".format(a))
        second_parse(b)
        print("...............结束爬取{}..................".format(a))



if __name__ == "__main__":
    i = 1
    while i <= 11:
        print("开始爬取第{}页。。。。。。。。。。。。。。。。。".format(i))
        url = 'https://www.wowoqq.com/juzi/qinghua/list_{}.html'.format(i)
        first_parse(url)
        i = i + 1
    connection.close()
