# import urllib.request
# import urllib.parse
# import base64
import re

#
#
# access_token = '24.f8df6de321b3f200a6937d4ec6565262.2592000.1557662876.282335-16006299'
# url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# # 二进制方式打开图文件
# f = open(r'0.jpg', 'rb')
# # 参数image：图像base64编码
# img = base64.b64encode(f.read())
# f.close()
# img = str(img, encoding = "utf-8")
# img.replace("\n", "")
#
#
# params = {"image": img}
#
# params = urllib.parse.urlencode(params).encode(encoding='UTF8')
# request = urllib.request.Request(url, params)
# request.add_header('Content-Type', 'application/x-www-form-urlencoded')
# response = urllib.request.urlopen(request)
# content = response.read()
# if (content):
#     print(content)

from aip import AipOcr
import pymysql.cursors
import os

""" 读取图片 """
pattren = re.compile('(.*?)\n')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# a = set()
i = []
n = 1
if __name__ == "__main__":
    names = []
    fa = open(r'name.txt')
    for str in fa:
        str2 = pattren.findall(str)[0]
        names.append(str2)
    print(len(names))
    print(names)


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

    """ 你的 APPID AK SK """
    APP_ID = '16006299'
    API_KEY = 'npQm5T7oh7jicQeT92YvmIYR'
    SECRET_KEY = 'GsGgl8ev8iwDoRbEz5BAvRpkbmMe256k'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    while n <= 523:
        if os.path.exists(r'lihai_biaoqingbao/{}.bmp'.format(n)):
            image = get_file_content(r'lihai_biaoqingbao/{}.bmp'.format(n))

            """ 调用通用文字识别, 图片为远程url图片 """
            # res=client.basicGeneralUrl(url)

            """ 调用通用文字识别, 图片为本地图片 """
            res = client.basicGeneral(image)

            word = res['words_result']
            final_word = ""
            for it in word:
                final_word = final_word + it['words']
            print(final_word)
            try:
                with connection.cursor() as cursor:
                    # 执行sql语句，插入记录
                    sql = "INSERT INTO emoticon(pictures_name, content, keywords) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (names[n-1], final_word, ''))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                pass
            n = n + 1

    connection.close()
