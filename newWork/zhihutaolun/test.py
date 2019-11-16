from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree
import requests
import pymysql.cursors
import re

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

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--headless')
header = {
    'authority': 'www.zhihu.com',
    'method': 'GET',
    'path': '/question/266230601/answer/351033170',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_zap=eb71d42f-6553-40cd-bcb9-69946faafe8a; _xsrf=RNDcHfvfWqqbWUhaiieyOosV9UthceX5; d_c0="ALAlveTvPQ-PTp9G5DWOJV2Wrof-AtzmXbA=|1554634565"; q_c1=739ebf665d454bdfbdb2b6623bd62e38|1554634679000|1554634679000; __gads=ID=27f02d11ec5d42a8:T=1554634693:S=ALNI_MZJHKprs3g_BJJ6pMbibqUlU2Jzeg; tst=h; l_n_c=1; n_c=1; __utmc=51854390; __utmz=51854390.1555655262.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utma=51854390.233604258.1555655944.1555655944.1555655944.2; l_cap_id="ZGJmYjA3NWZhYWQzNGUzNWEwZDEyMzM3YTliOGExMWQ=|1555685314|ee49d6db972442045243bc2ba1cb25c4b73e1713"; r_cap_id="N2NhZTM5YTg0YTI0NDNlZTliNTUyMjIwNGQxZjkyMzQ=|1555685314|672b97f78b7ee722ea96a64d88900b0603ac25cf"; cap_id="OTI0MGIyZTQzZjE5NDQxMzk5NWNmOWM3ZjFmNGY1YWU=|1555685314|d9af429dff44eb1fc806d2260ab173aa6307b83c"; capsion_ticket="2|1:0|10:1555685392|14:capsion_ticket|44:NDg4ZGQ0OGZiZGVhNGY1OGIyMGFkNjU1YzllZDcwOTg=|ebe1e765ae96aba30742b549fb7b00607f69470098d0182bf7eb476000674a3f"; tgw_l7_route=116a747939468d99065d12a386ab1c5f',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
}


def parse_xiangqing(url):
    # 驱动路径
    path = r'C:\Users\Administrator\Desktop\chromedriver.exe'

    # 创建浏览器对象
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    browser.get(url)
    time.sleep(1)
    tree_p = etree.HTML(browser.page_source)
    browser.quit()
    # 提取详情
    xiangqing_p = tree_p.xpath('//span[@class="RichText ztext"]/text()')
    if len(xiangqing_p) > 0:
        return xiangqing_p[0]


if __name__ == "__main__":
    # 驱动路径
    path = r'C:\Users\Administrator\Desktop\chromedriver.exe'

    # 创建浏览器对象
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    for it in open('zhuti.txt'):
        # 上网
        url = 'https://www.zhihu.com' + it + '/top-answers'
        print(url)
        browser.get(url)
        time.sleep(1)

        # # 让browser执行简单的JS代码，模拟滚动条滚动到底部

        js = 'document.body.scrollTop=10000000'
        browser.execute_script(js)

        time.sleep(1)

        browser.save_screenshot(r'sheying.png')
        with open('sheying.html', 'w', encoding="utf8") as fp:
            fp.write(browser.page_source)
        tree = etree.HTML(browser.page_source)
        # browser.quit()
        # 提取话题
        topic = tree.xpath('//h2[@class="ContentItem-title"]/div/a/text()')
        print(topic)

        # 提取话题讨论数
        taolun = []
        pattren = re.compile(r'([0-9,]+)')
        Discussion_number = tree.xpath('//button[@type="button"]/text()')
        for dis_nu in Discussion_number:
            if dis_nu.endswith('条评论'):
                taolun.append(pattren.findall(dis_nu)[0])
        print(taolun)

        # 提取话题链接
        urls = tree.xpath('//h2[@class="ContentItem-title"]/div/a/@href')
        print(urls)
        string_xiangqing = ''
        string_class = ''
        # 提取时间
        now_time = time.asctime(time.localtime(time.time()))
        for t, d, u in zip(topic, taolun, urls):
            u = 'https://www.zhihu.com' + u
            # 提取话题详情
            # s = requests.get(u, headers=header)
            # s.encoding = "utf8"
            # with open('taolun.html', 'wb') as fp:
            #     fp.write(s.content)

            # print(u)

            browser.get(u)
            time.sleep(2)
            browser.save_screenshot(r'sheying2.png')
            tree2 = etree.HTML(browser.page_source)
            # 提取标题详情
            xiangqing = tree2.xpath('//div[@class="QuestionHeader-detail"]//text()')
            for xq in xiangqing:
                string_xiangqing = string_xiangqing + xq
            # 提取标题分类
            classes = tree2.xpath('//span[@class="Tag-content"]//text()')
            for cs in classes:
                string_class = string_class + ' ' + cs

            # 执行sql语句
            try:
                with connection.cursor() as cursor:
                    # 执行sql语句，插入记录
                    sql = "INSERT INTO zhihuTopic (topics, categories, discussion_number, details_url, now_time, keywords) VALUES (%s, %s, %s, %s, %s, %s);"
                    cursor.execute(sql, (t, string_class, d, string_xiangqing + u, now_time, ''))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                pass

    browser.close()
    connection.close()
