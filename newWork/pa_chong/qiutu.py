import urllib.request
import urllib.parse
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}


def down_img(url):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)".*?>.*?</div>', re.S)
    lt = pattern.findall(response.read().decode())
    # print(lt)
    if not os.path.exists('qiutu'):
        os.mkdir('qiutu')
    for it in lt:
        url_t = 'https:' + it[0]
        # request = urllib.request.Request(url_t, headers=headers)
        # response = urllib.request.urlopen(request)
        print("图片开始下载.....")
        filename = it[1]
        urllib.request.urlretrieve(url_t, 'qiutu/'+filename+'.jpg')
        print("图片结束下载.....")


def main():
    url = 'https://www.qiushibaike.com/hot/page/'
    start_page = int(input("请输入您要下载的开始页数："))
    end_page = int(input("请输入您要下载的最后页数"))
    for page in range(start_page, end_page + 1):
        url_t = url + str(page) + '/'
        # print(url_t)
        print("第%s页开始下载", str(page))
        down_img(url_t)


main()
