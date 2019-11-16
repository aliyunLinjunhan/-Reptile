import requests
from lxml import etree
import re
from lxml import etree
from requests.exceptions import RequestException
import urllib.parse
import time
import datetime

import pymysql.cursors

headers = {
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Cache - Control': 'max - age = 0',
    'Connection': 'keep - alive',
    'Cookie': 'SINAGLOBAL = 4747041472152.871.1554634074236;UOR =, , www.baidu.com;_s_tentry = login.sina.com.cn;Apache = 2835606734306.604.1555035576531;ULV = 1555035576537:4: 4:4: 2835606734306.604.1555035576531: 1554898888543;cross_origin_proto = SSL;login_sid_t = 4ebc9942b026cf8610ec8d5ed412e488;_ga = GA1.2.1588348663.1555036309;_gid = GA1.2.1615807437.1555036309;__gads = ID = 12d9cdcfb9478682: T = 1555036310:S = ALNI_MY8834FGIA6Mz8WjdnkG_zF - hyMQg;SCF = AplKWTd95vcEaLQ6pUaSkC5gEZNzZsDmg9qGDM5AtgEd1jR41RxXbJA4F7 - VRpIcXpflUSRgsSzYmEIBQ3GhA7s.;SUB = _2A25xq4j2DeThGeFO7FcS - C3MyjiIHXVSwP0 - rDV8PUNbmtBeLVSikW9NQUScKzpyAwXOrrVwKxGszW5nj45IrK2R;SUBP = 0033WrSXqPxfM725Ws9jqgMF55529P9D9WWPAAc1_5K_8gyKNv0vk1995JpX5KzhUgL.FoM7S0 - 01he7eKB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNehMfe0n0eh2X;SUHB = 0laVDmJv5bkueo;ALF = 1586572325;SSOLoginState = 1555036326;wvr = 6;webim_unReadCount = % 7B % 22time % 22 % 3A1555040131042 % 2C % 22dm_pub_total % 22 % 3A1 % 2C % 22chat_group_pc % 22 % 3A0 % 2C % 22allcountNum % 22 % 3A2 % 2C % 22msgbox % 22 % 3A0 % 7D;WBStorage = 201904121135 | undefined',
    'Host': 's.weibo.com',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36',
}

headers_resou = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encodin': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'SINAGLOBAL=4747041472152.871.1554634074236; _ga=GA1.2.1588348663.1555036309; __gads=ID=12d9cdcfb9478682:T=1555036310:S=ALNI_MY8834FGIA6Mz8WjdnkG_zF-hyMQg; _s_tentry=cn.club.vmall.com; UOR=,,club.huawei.com; login_sid_t=f2f1cf1ade353e0fa34be7d5c4a9794f; cross_origin_proto=SSL; Apache=1525126225624.247.1558361021726; ULV=1558361021736:29:8:2:1525126225624.247.1558361021726:1558269487022; SCF=AplKWTd95vcEaLQ6pUaSkC5gEZNzZsDmg9qGDM5AtgEdNnDhCBdD8CFFig21x3GxoiPOCDneJVLIpCA8aGsjdGo.; SUB=_2A25x5sOCDeRhGeNN71UU-CjJzzuIHXVSlbJKrDV8PUNbmtBeLRDCkW9NSaUNzhLEMU-glT-oqUfTUyJGKk7GDvKv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh_ypyvNd-aI0YNU2RF_1gh5JpX5KzhUgL.Fo-0ShMf1hqfShM2dJLoIpeLxKBLBonLBo9QIgxLPcy49Giy; SUHB=0jB4m0VP-AhKHM; ALF=1589897042; SSOLoginState=1558361042; wvr=6; wb_view_log_5347586547=1920*10801.25; webim_unReadCount=%7B%22time%22%3A1558361065185%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; YF-Page-G0=7f483edf167a381b771295af62b14a27|1558361065|1558361016',
    # 'Host': 'd.weibo.com',
    # 'Referer': 'https://d.weibo.com/231650?cfs=920&Pl_Discover_Pt6Rank__4_filter=&Pl_Discover_Pt6Rank__4_page=2',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',

    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'SINAGLOBAL=4747041472152.871.1554634074236; _ga=GA1.2.1588348663.1555036309; __gads=ID=12d9cdcfb9478682:T=1555036310:S=ALNI_MY8834FGIA6Mz8WjdnkG_zF-hyMQg; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh_ypyvNd-aI0YNU2RF_1gh5JpX5KMhUgL.Fo-0ShMf1hqfShM2dJLoIpeLxKBLBonLBo9QIgxLPcy49Giy; ALF=1589978495; SSOLoginState=1558442496; SCF=AplKWTd95vcEaLQ6pUaSkC5gEZNzZsDmg9qGDM5AtgEdAVLODNo0cc-eP62xFRqVZxXczfmSNvIDG96c_28zIqM.; SUB=_2A25x54JRDeRhGeNN71UU-CjJzzuIHXVSlPSZrDV8PUNbmtBeLWP4kW9NSaUNzmacGz1QGv5mfkajLc9IYY-muAPk; SUHB=0N2Fty4HB1kekN; YF-Page-G0=6affec4206bb6dbb51f160196beb73f2|1558442499|1558442494; wb_view_log_5347586547=1920*10801.25; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=4072875775960.4404.1558442501157; ULV=1558442501183:30:9:3:4072875775960.4404.1558442501157:1558361021736; webim_unReadCount=%7B%22time%22%3A1558442533287%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
    # 'Host': 'd.weibo.com',
    # 'Referer': 'https://d.weibo.com/231650?cfs=920&Pl_Discover_Pt6Rank__4_filter=&Pl_Discover_Pt6Rank__4_page=1',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=4747041472152.871.1554634074236; _ga=GA1.2.1588348663.1555036309; __gads=ID=12d9cdcfb9478682:T=1555036310:S=ALNI_MY8834FGIA6Mz8WjdnkG_zF-hyMQg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh_ypyvNd-aI0YNU2RF_1gh5JpX5KMhUgL.Fo-0ShMf1hqfShM2dJLoIpeLxKBLBonLBo9QIgxLPcy49Giy; UOR=,,login.sina.com.cn; ALF=1590670693; SSOLoginState=1559134694; SCF=AplKWTd95vcEaLQ6pUaSkC5gEZNzZsDmg9qGDM5AtgEdYWoAKKxWTwCnSWyJzhA1_AvpT_NBD-S5zc_FDHA1IQE.; SUB=_2A25x6vG3DeRhGeNN71UU-CjJzzuIHXVSnmR_rDV8PUNbmtBeLVjHkW9NSaUNzjWUcnV6bXW8Lhs5uSYlXINSOuPT; SUHB=0P18qHpBeTj3-t; _s_tentry=login.sina.com.cn; Apache=7070124880816.729.1559134698411; ULV=1559134698420:31:10:1:7070124880816.729.1559134698411:1558442501183; YF-Page-G0=e57fcdc279d2f9295059776dec6d0214|1559134698|1559134692; wb_view_log_5347586547=1920*10801.25; webim_unReadCount=%7B%22time%22%3A1559134710265%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
    'Host': 'd.weibo.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',

}
os_path = r"C:\Users\Administrator\Desktop\mysql_data\redian_beifneg\redian{}.txt".format(
    datetime.datetime.now().strftime('%Y-%m-%d'))


def parse_readAmount_time(readAmount_time):
    """
    用来解析提取时间和阅读量
    :param readAmount_time:
    :return: 时间和阅读量
    """
    pattren = re.compile('(.*?2019) (.*)([\u4e00-\u9fa5])')
    it = pattren.findall(readAmount_time)
    # print(it)
    amount = float(it[0][1])
    if it[0][2] == "万":
        amount = amount * 10000
    else:
        amount = amount * 100000000
    # print(int(amount))
    time_now = it[0][0]
    # print(time_now)
    return int(amount), str(time_now)


def parse_url_content(content):
    # print(content)
    pattren_o = re.compile('(.*?)([a-zA-z]+://[^\s]*)')
    it = pattren_o.findall(content)
    # print(it)
    return str(it[0][0]), str(it[0][1])


def second_parse(title):
    '''
    获取热点详细信息
    :param title:
    :return:
    '''
    for it in title:
        time.sleep(5)
        redian = {}
        redian["热点"] = it
        url = 'https://s.weibo.com/weibo?q=%23{}%23'.format(urllib.parse.quote(it))
        pattern = re.compile('[\u4e00-\u9fa5]+(.*?[\u4e00-\u9fa5])')
        print(url)
        try:

            source_code = requests.get(url, headers=headers)
            if source_code.status_code == 200:
                # with open('redian.html', 'wb') as fp:
                #     fp.write(source_code.content)
                tree = etree.HTML(source_code.text)
                # 爬取该热点阅读量
                Reading_volume = tree.xpath('//span/text()')
                if len(Reading_volume) != 0:
                    Reading_volume = Reading_volume[0]
                if len(Reading_volume) != 0:
                    Reading_volume = pattern.findall(Reading_volume)
                if len(Reading_volume) > 0:
                    Reading_volume = Reading_volume[0]
                # if len(Reading_volume) > 0:
                #     Reading_volume = Reading_volume[0]
                redian["阅读量"] = Reading_volume
                # 爬取热点讨论数
                # discuss_amount = tree.xpath('//span/text()')[1]
                # discuss_amount = pattern.findall(discuss_amount)[0]
                # # if len(discuss_amount) > 0:
                # #     discuss_amount = discuss_amount[0]
                # redian["讨论数"] = discuss_amount
                # 记录爬取时间
                redian["时间"] = time.asctime(time.localtime(time.time()))
                # 爬取热点导语内容
                content = tree.xpath('//div[@class="card-wrap"]/div/p/text()')
                if len(content) > 0:
                    content = content[0] + url
                else:
                    content.append(url)
                if isinstance(content, list):
                    redian["热点导语"] = content[0]
                else:
                    redian["热点导语"] = content

                print(redian)

                try:
                    with open(os_path, 'a+', encoding="utf-8") as fp:
                        fp.write(str(redian) + '\n')
                except IOError as err:
                    print("文件写入失败")
                amount, time_now = parse_readAmount_time(redian['时间'] + ' ' + redian['阅读量'])
                content, url_c = parse_url_content(redian["热点导语"])
                title = it
                # 执行sql语句 redian['时间'] + ' ' + redian['阅读量']
                try:
                    with connection.cursor() as cursor:
                        delSql = "DELETE FROM Hotspot WHERE title = %s"
                        sql = "INSERT INTO Hotspot (title, amount, daytime, content, url, keywords) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(delSql, (title))
                        cursor.execute(sql, (title, amount, time_now, content, url_c, ''))
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    pass
        except RequestException:
            print("响应请求失败")


def first_parse(content):
    '''
    爬取微博热搜版的话题名称
    :param content:
    :return:
    '''
    # print(content)
    # tree = etree.HTML(content)
    # 爬取热点标题
    # print(content)
    pattren = re.compile('#([\u4e00-\u9fa5]+)#')
    title = pattren.findall(content)
    quchong_title = list(set(title))
    print(quchong_title)
    return quchong_title


# python C:\Users\Administrator\PycharmProjects\newWork\paqu_gushiwen\weibo.py
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
    i = 1
    while i <= 7:

        print("开始爬第{}页".format(i))
        url = "https://d.weibo.com/231650?cfs=920&Pl_Discover_Pt6Rank__4_filter=&Pl_Discover_Pt6Rank__4_page={}#Pl_Discover_Pt6Rank__4".format(
            i)
        try:
            source_code = requests.get(url, headers=headers_resou)
            # with open('redian.html', 'wb') as fp:
            #     fp.write(source_code.content)
            if source_code.status_code == 200:
                title = first_parse(source_code.text)
                second_parse(title)
            else:
                print(source_code.status_code)

            i = i + 1
            time.sleep(60)
        except RequestException:
            print("响应请求失败")

    connection.close()
