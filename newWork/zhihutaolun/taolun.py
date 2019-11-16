import requests
from lxml import etree
import urllib.parse


header_post = {
    'authority': 'www.zhihu.com',
    'method': 'POST',
    'path': '/node/TopicsPlazzaListV2',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '90',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_zap=eb71d42f-6553-40cd-bcb9-69946faafe8a; _xsrf=RNDcHfvfWqqbWUhaiieyOosV9UthceX5; d_c0="ALAlveTvPQ-PTp9G5DWOJV2Wrof-AtzmXbA=|1554634565"; q_c1=739ebf665d454bdfbdb2b6623bd62e38|1554634679000|1554634679000; __gads=ID=27f02d11ec5d42a8:T=1554634693:S=ALNI_MZJHKprs3g_BJJ6pMbibqUlU2Jzeg; tst=h; __utma=51854390.1888928663.1554634706.1554634706.1555655262.2; __utmc=51854390; __utmz=51854390.1555655262.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; l_n_c=1; n_c=1; __utmv=51854390.000--|2=registration_date=20171102=1^3=entry_date=20190407=1; capsion_ticket="2|1:0|10:1555655535|14:capsion_ticket|44:NjlkOTJjOGJhYzQ3NDMxYjkyZDkzYmM5Y2JiOWM0MGY=|bb31e10e559f39f09df6dc96825f1a50b946fe4898a4bd0a075a5bba1c136ff5"; tgw_l7_route=060f637cd101836814f6c53316f73463; l_cap_id="YzcwZTY3YzQwZGZjNDUwN2FhNDNlOGRiODk2YzI2YWE=|1555673594|5f2178620b8323158490967244e0cfccb7890e84"; r_cap_id="YWU1N2QyNTY0ZDAyNDAxZTk0MTllYjM3Y2EwNGY3M2Y=|1555673594|e0a70d856443e04b1e0c8f2dc5debf89b4c7e0e2"; cap_id="Njg5OTMzY2ZiOTg4NDcyNGJiN2I3ZjhiODhhNGRjNzk=|1555673594|f5e3c1da5fa2432b515c6c4273739b5f056b29b3"',
    'origin': 'https://www.zhihu.com',
    'referer': 'https://www.zhihu.com/topics',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrftoken': 'RNDcHfvfWqqbWUhaiieyOosV9UthceX5',
}

# 提取分类
'''
header = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_zap=eb71d42f-6553-40cd-bcb9-69946faafe8a; _xsrf=RNDcHfvfWqqbWUhaiieyOosV9UthceX5; d_c0="ALAlveTvPQ-PTp9G5DWOJV2Wrof-AtzmXbA=|1554634565"; q_c1=739ebf665d454bdfbdb2b6623bd62e38|1554634679000|1554634679000; __gads=ID=27f02d11ec5d42a8:T=1554634693:S=ALNI_MZJHKprs3g_BJJ6pMbibqUlU2Jzeg; tst=h; tgw_l7_route=116a747939468d99065d12a386ab1c5f; __utma=51854390.1888928663.1554634706.1554634706.1555655262.2; __utmb=51854390.0.10.1555655262; __utmc=51854390; __utmz=51854390.1555655262.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; l_n_c=1; l_cap_id="NjljNzM4NGMwY2Q5NDYxYjk5M2ZiYTA4NmIzNDgxZTg=|1555655521|2321ec19c1a2efaee7f3f32c4e8e5348c55dc5b6"; r_cap_id="MGQxOWIxN2VkMzZlNDFkYjhiODQ4Mjk0OTM2MDBjNDI=|1555655521|3174db6902dcf5e1bc0bbe1a186614e359409126"; cap_id="MTA2NTA1MzQzMTE1NGU2NGJiOWJlMTA4Zjc2OGVjZWU=|1555655521|1ad2c78aab6323a32065205ebfa3aacb7c8af79c"; n_c=1; __utmv=51854390.000--|2=registration_date=20171102=1^3=entry_date=20190407=1; capsion_ticket="2|1:0|10:1555655535|14:capsion_ticket|44:NjlkOTJjOGJhYzQ3NDMxYjkyZDkzYmM5Y2JiOWM0MGY=|bb31e10e559f39f09df6dc96825f1a50b946fe4898a4bd0a075a5bba1c136ff5"',

}

url = 'https://www.zhihu.com/topics'
source_code = requests.get(url, headers=header)
source_code.encoding = 'utf-8'
tree = etree.HTML(source_code.content)
# 提取分类
classification = tree.xpath('//ul[@class="zm-topic-cat-main clearfix"]/li/@data-id')
for it in classification:
    print(it)
    with open('fenlei.txt', 'a',  encoding="utf8") as fp:
        fp.write(it + '\n')
# with open('taolun.html', 'w', encoding="gbk") as fp:
#     fp.write(source_code.text)
'''

'''
# 提取关注号名称和链接
header = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_zap=eb71d42f-6553-40cd-bcb9-69946faafe8a; _xsrf=RNDcHfvfWqqbWUhaiieyOosV9UthceX5; d_c0="ALAlveTvPQ-PTp9G5DWOJV2Wrof-AtzmXbA=|1554634565"; q_c1=739ebf665d454bdfbdb2b6623bd62e38|1554634679000|1554634679000; __gads=ID=27f02d11ec5d42a8:T=1554634693:S=ALNI_MZJHKprs3g_BJJ6pMbibqUlU2Jzeg; tst=h; tgw_l7_route=116a747939468d99065d12a386ab1c5f; __utma=51854390.1888928663.1554634706.1554634706.1555655262.2; __utmb=51854390.0.10.1555655262; __utmc=51854390; __utmz=51854390.1555655262.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; l_n_c=1; l_cap_id="NjljNzM4NGMwY2Q5NDYxYjk5M2ZiYTA4NmIzNDgxZTg=|1555655521|2321ec19c1a2efaee7f3f32c4e8e5348c55dc5b6"; r_cap_id="MGQxOWIxN2VkMzZlNDFkYjhiODQ4Mjk0OTM2MDBjNDI=|1555655521|3174db6902dcf5e1bc0bbe1a186614e359409126"; cap_id="MTA2NTA1MzQzMTE1NGU2NGJiOWJlMTA4Zjc2OGVjZWU=|1555655521|1ad2c78aab6323a32065205ebfa3aacb7c8af79c"; n_c=1; __utmv=51854390.000--|2=registration_date=20171102=1^3=entry_date=20190407=1; capsion_ticket="2|1:0|10:1555655535|14:capsion_ticket|44:NjlkOTJjOGJhYzQ3NDMxYjkyZDkzYmM5Y2JiOWM0MGY=|bb31e10e559f39f09df6dc96825f1a50b946fe4898a4bd0a075a5bba1c136ff5"',

}


def first_parse(url):
    source_code = requests.get(url, headers=header)
    source_code.encoding = "utf8"
    with open('guanhzuhao.html', 'wb') as fp:
        fp.write(source_code.content)
    tree = etree.HTML(source_code.content)
    # 提取关注号名称
    titles = tree.xpath('//div[@class="zh-general-list clearfix"]/div/div/a/strong/text()')
    print(titles)
    # 提取关注号链接
    url = tree.xpath('//div[@class="zh-general-list clearfix"]/div/div[@class="blk"]/a[@target="_blank"]/@href')
    print(url)
    for it in url:
        url_all = 'https://www.zhihu.com' + it + '/top-answers'
        print(url_all)
'''

if __name__ == "__main__":
    for it in open('fenlei.txt', 'r'):
        data = {
            'method': 'next',
            'params': {"topic_id": it, "offset": 0, "hash_id": ""},
            # 'method': 'next',
            # 'params': '%7B%22topic_id%22%3A1538%2C%22offset%22%3A0%2C%22hash_id%22%3A%22%22%7D',
        }
        url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
        json_code = requests.post(url, data=urllib.parse.urlencode(data), headers=header_post)
        print(json_code.status_code)
        print(json_code.content)
        break
        # url = 'https://www.zhihu.com/topics' + str
        # 解析网站中的前20名公众号的名称和链接
        # first_parse(url)
        # first_parse('https://www.zhihu.com/topics#%E7%AF%AE%E7%90%83')
