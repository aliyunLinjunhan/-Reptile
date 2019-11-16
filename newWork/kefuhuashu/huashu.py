import re
import pymysql
import requests

# source_code = requests.get('http://www.gjknj.com/duwu/3889.html')
# source_code.encoding = "gb2312"
# with open('huashu.html', 'w', encoding="gb2312") as fp:
#     fp.write(source_code.text)


# 设置数据库连接数据
config = {
'host': '203.195.244.169',
        'port': 3306,
        'user': 'root',
        'password': 'Wissen123**',
        'db': 'gushi',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
}
# 连接数据库
connection = pymysql.connect(**config)


keywords = '发票类'
# pattren = re.compile(r'商家[A-Z]：(.*?[；？！。】~）])')
pattren = re.compile(r'<p>(.*?)</p>')
for it in open('huashu.txt', 'r'):
    # print(it)
    ret = pattren.findall(it)
    print(ret)
    if len(it) > 0:
        # print(ret)
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = "INSERT INTO kefuhuashu (sentence, keywords) VALUES (%s, %s)"
                cursor.execute(sql, (ret[0], keywords))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            pass
connection.close()


