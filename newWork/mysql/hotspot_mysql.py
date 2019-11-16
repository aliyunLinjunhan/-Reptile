import re
import pymysql.cursors

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

pattren = re.compile('"(.*?)"')
for str in open(r'C:\Users\Administrator\Desktop\mysql_data\zhihuTopic.txt', 'r',
                encoding='UTF-8'):
    print(str)
    ret = pattren.findall(str)
    print(ret)
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = "INSERT INTO zhihuTopic2 (topics, categories, discussion_number, details_url, now_time, keywords) VALUES (%s, %s, %s, %s, %s, %s);"
            cursor.execute(sql, (ret[0], ret[1], ret[2], ret[3], ret[4], ret[5]))
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        pass
connection.close()
